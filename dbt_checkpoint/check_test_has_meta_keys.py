import argparse
import os
import time
from pathlib import Path
from typing import Any, Dict, Optional, Sequence

from dbt_checkpoint.tracking import dbtCheckpointTracking
from dbt_checkpoint.utils import (
    JsonOpenError,
    add_default_args,
    add_meta_keys_args,
    get_dbt_manifest,
    get_filenames,
    get_tests,
    red,
    yellow,
)


def has_meta_key(
    paths: Sequence[str],
    manifest: Dict[str, Any],
    meta_keys: Sequence[str],
    allow_extra_keys: bool,
) -> Dict[str, Any]:
    status_code = 0
    sqls = get_filenames(paths, [".sql"])
    filenames = set(sqls.keys())
    # if user added schema but did not rerun
    tests = get_tests(
        manifest,
        filenames,
    )

    for test in tests:
        test_meta = set(test.node.get("meta", {}).keys())
        if allow_extra_keys:
            diff = not (set(meta_keys).issubset(test_meta))
        else:
            diff = not (set(meta_keys) == test_meta)
        if diff:
            status_code = 1
            print(
                f"{test.test_name} meta keys don't match. \n"
                f"Provided: {yellow(', '.join(list(meta_keys)))}\n"
                f"Actual: {red(', '.join(list(test_meta)))}\n"
            )
    return {"status_code": status_code}


def main(argv: Optional[Sequence[str]] = None) -> int:  # pragma: no cover
    parser = argparse.ArgumentParser()
    add_default_args(parser)
    add_meta_keys_args(parser)
    args = parser.parse_args(argv)

    try:
        manifest = get_dbt_manifest(args)
    except JsonOpenError as e:
        print(f"Unable to load manifest file ({e})")
        return 1

    start_time = time.time()
    hook_properties = has_meta_key(
        paths=args.filenames,
        manifest=manifest,
        meta_keys=args.meta_keys,
        allow_extra_keys=args.allow_extra_keys,
    )
    end_time = time.time()
    script_args = vars(args)

    tracker = dbtCheckpointTracking(script_args=script_args)
    tracker.track_hook_event(
        event_name="Hook Executed",
        manifest=manifest,
        event_properties={
            "hook_name": os.path.basename(__file__),
            "description": "Check single test has meta keys.",
            "status": hook_properties.get("status_code"),
            "execution_time": end_time - start_time,
            "is_pytest": script_args.get("is_test"),
        },
    )

    return hook_properties.get("status_code")


if __name__ == "__main__":
    exit(main())
