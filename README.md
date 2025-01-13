<p align="center">
 <h1 align="center">dbt-checkpoint</h1>
</p>
<p align="center">
 <a href="https://github.com/dbt-checkpoint/dbt-checkpoint/actions?workflow=CI">
 <img src="https://github.com/dbt-checkpoint/dbt-checkpoint/workflows/CI/badge.svg?branch=main" alt="CI" />
 </a>
 <a href="https://codecov.io/gh/dbt-checkpoint/dbt-checkpoint">
 <img src="https://codecov.io/gh/dbt-checkpoint/dbt-checkpoint/branch/main/graph/badge.svg"/>
 </a>
 <a href="https://github.com/psf/black">
 <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="black"/>
 </a>
 <a href="https://github.com/pre-commit/pre-commit">
 <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" alt="black"/>
 </a>
</p>

## Brought to you by your friends at Datacoves

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="images/datacoves-dark.png">
  <img alt="Datacoves" src="images/datacoves-light.png" width="150">
</picture>

The Datacoves platform helps enterprises overcome their data delivery challenges quickly using dbt and Airflow, implementing best practices from the start without the need for multiple vendors or costly consultants.

Hosted VS Code, dbt-core, SqlFluff, and Airflow, find out more at [Datacoves.com](https://datacoves.com/product).

<br>

## Goal

dbt-checkpoint provides [pre-commit](https://pre-commit.com) hooks to ensure the quality of your [dbt](https://www.getdbt.com) projects.

`dbt` is awesome, but when the number of models, sources, and macros in a project grows, it becomes challenging to maintain the same level of quality across developers. Users forget to update columns in property (yml) files or add table and column descriptions. Without automation the reviewer workload increases and unintentional errors may be missed. dbt-checkpoint allows organizations to add automated validations improving your code review and release process.

## Telemetry

dbt-checkpoint has telemetry built into some of its hooks to help the maintainers from Datacoves understand which hooks are being used and which are not to prioritize future development of dbt-checkpoint. We do not track credentials nor details of your dbt execution such as model names. We also do not track any of the dbt hooks, such as for generating documentation. The one detail we do use related to dbt is [the anonymous user_id generated by dbt](https://docs.getdbt.com/reference/artifacts/dbt-artifacts#common-metadata) to help us identify distinct projects.

By default, this is turned on – you can opt out of event tracking at any time by adding the following to your `.dbt-checkpoint.yaml` file:

```
version: 1
disable-tracking: true
```

## Setting dbt project root

You can specify a dbt project root directory for all hooks. This is particularly useful when your dbt project is not located at the root of your repository but in a sub-directory of it.

In that situation, you previously had to specify a `--manifest` flag in each hook.

Now, you can avoid repeating yourself by adding the `dbt-project-dir` key to your `.dbt-checkpoint.yaml` config file:

```yaml
version: 1
dbt-project-dir: my_dbt_project
```

This way, we will automatically look for the required manifest/catalog inside your `my_dbt_project` project folder.

## General `exclude` and per-hook excluding

Since `dbt-checkpoint 1.1.0`, certain hooks implement an implicit logic that "discover" their sql/yml equivalent for checking.

For a complete background please refer to [#118](https://github.com/dbt-checkpoint/dbt-checkpoint/issues/118).

Since the root-level `exclude` statement is handled by pre-commit, when those hooks discover their related sql/yml files, this root exclusion is omitted (dbt-checkpoint re-includes files that may have been excluded). To exclude files from being discovered by this logic, the `exclude` path/regex must be provided in each hook ([#119](https://github.com/dbt-checkpoint/dbt-checkpoint/pull/119))

## List of `dbt-checkpoint` hooks

:bulb: Click on hook name to view the details.

**Model checks:**

- [`check-column-desc-are-same`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-column-desc-are-same): Check column descriptions are the same.
- [`check-column-name-contract`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-column-name-contract): Check column name abides to contract.
- [`check-model-columns-have-desc`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-columns-have-desc): Check the model columns have description.
- [`check-model-has-all-columns`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-has-all-columns): Check the model has all columns in the properties file.
- [`check-model-has-contract`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-has-contract): Check the model has contract enabled.
- [`check-model-has-constraints`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-has-constraints): Check the model has constraints defined.
- [`check-model-has-description`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-has-description): Check the model has description.
- [`check-model-has-meta-keys`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-has-meta-keys): Check the model has keys in the meta part.
- [`check-model-has-labels-keys`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-has-labels-keys): Check the model has keys in the labels part.
- [`check-model-has-properties-file`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-has-properties-file): Check the model has properties file.
- [`check-model-has-tests-by-name`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-has-tests-by-name): Check the model has a number of tests by test name.
- [`check-model-has-tests-by-type`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-has-tests-by-type): Check the model has a number of tests by test type.
- [`check-model-has-tests-by-group`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-has-tests-by-group): Check the model has a number of tests from a group of tests.
- [`check-model-has-tests`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-has-tests): Check the model has a number of tests.
- [`check-model-name-contract`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-name-contract): Check model name abides to contract.
- [`check-model-parents-and-childs`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-parents-and-childs): Check the model has a specific number (max/min) of parents or/and children.
- [`check-model-parents-database`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-parents-database): Check the parent model has a specific database.
- [`check-model-parents-name-prefix`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-parents-name-prefix): Check the parent model names have a specific prefix.
- [`check-model-parents-schema`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-parents-schema): Check the parent model has a specific schema.
- [`check-model-tags`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-tags): Check the model has valid tags.
- [`check-model-materialization-by-childs`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-model-materialization-by-childs): Check the materialization of models given a threshold of child models.

- **Script checks:**

- [`check-script-semicolon`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-script-semicolon): Check the script does not contain a semicolon.
- [`check-script-has-no-table-name`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-script-has-no-table-name): Check the script has no table name (is not using `source()` or `ref()` macro for all tables).
- [`check-script-ref-and-source`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-script-ref-and-source): Check the script has only existing refs and sources.

**Source checks:**

- [`check-source-columns-have-desc`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-source-columns-have-desc): Check for source column descriptions.
- [`check-source-has-all-columns`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-source-has-all-columns): Check the source has all columns in the properties file.
- [`check-source-table-has-description`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-source-table-has-description): Check the source table has description.
- [`check-source-has-freshness`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-source-has-freshness): Check the source has the freshness.
- [`check-source-has-loader`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-source-has-loader): Check the source has loader option.
- [`check-source-has-meta-keys`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-source-has-meta-keys): Check the source has keys in the meta part.
- [`check-source-has-labels-keys`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-source-has-labels-keys): Check the source has keys in the labels part.
- [`check-source-has-tests-by-name`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-source-has-tests-by-name): Check the source has a number of tests by test name.
- [`check-source-has-tests-by-type`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-source-has-tests-by-type): Check the source has a number of tests by test type.
- [`check-source-has-tests`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-source-has-tests): Check the source has a number of tests.
- [`check-source-has-tests-by-group`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-source-has-tests-by-group): Check the source has a number of tests from a group of tests.
- [`check-source-tags`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-source-tags): Check the source has valid tags.
- [`check-source-childs`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-source-childs): Check the source has a specific number (max/min) of children.

**Macro checks:**

- [`check-macro-has-description`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-macro-has-description): Check the macro has description.
- [`check-macro-arguments-have-desc`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-macro-arguments-have-desc): Check the macro arguments have description.
- [`check-macro-has-meta-keys`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-macro-has-meta-keys): Check the macro has meta keys.

**Exposure checks:**

- [`check-exposure-has-meta-keys`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-exposure-has-meta-keys): Check the exposure has meta keys.

**Seed checks:**

- [`check-seed-has-meta-keys`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-seed-has-meta-keys): Check the seed has meta keys.

**Snapshot checks:**

- [`check-snapshot-has-meta-keys`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-snapshot-has-meta-keys): Check the snapshot has meta keys.

**Test checks:**

- [`check-test-has-meta-keys`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-test-has-meta-keys): Check singular tests have meta keys.

**Modifiers:**

- [`generate-missing-sources`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#generate-missing-sources): If any source is missing this hook tries to create it.
- [`generate-model-properties-file`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#generate-model-properties-file): Generate model properties file.
- [`unify-column-description`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#unify-column-description): Unify column descriptions across all models.
- [`replace-script-table-names`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#replace-script-table-names): Replace table names with `source()` or `ref()` macros in the script.
- [`remove-script-semicolon`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#remove-script-semicolon): Remove the semicolon at the end of the script.

**dbt commands:**

- [`dbt-clean`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#dbt-clean): Run `dbt clean` command.
- [`dbt-compile`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#dbt-compile): Run `dbt compile` command.
- [`dbt-deps`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#dbt-deps): Run `dbt deps` command.
- [`dbt-docs-generate`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#dbt-docs-generate): Run `dbt docs generate` command.
- [`dbt-parse`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#dbt-parse): Run `dbt parse` command.
- [`dbt-run`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#dbt-run): Run `dbt run` command.
- [`dbt-test`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#dbt-test): Run `dbt test` command.

**dbt checks:**

- [`check-database-casing-consistency`](https://github.com/dbt-checkpoint/dbt-checkpoint/blob/main/HOOKS.md#check-database-casing-consistency): compare Manifest and Catalog to ensure DB and Schemas have the same casing.

---

:exclamation:**If you have a suggestion for a new hook or find a bug, [let us know](https://github.com/dbt-checkpoint/dbt-checkpoint/issues/new).**:exclamation:

## Install

For detailed installation and usage, instructions see [pre-commit.com](https://pre-commit.com) site.

```
pip install pre-commit
```

## Setup

1. Create a file named `.pre-commit-config.yaml` in your project root folder.
2. Add [list of hooks](#list-of-dbt-checkpoint-hooks) you want to run before every commit. E.g.:

```yaml
repos:
  - repo: https://github.com/dbt-checkpoint/dbt-checkpoint
    rev: v1.2.1
    hooks:
      - id: dbt-parse
      - id: dbt-docs-generate
        args: ["--cmd-flags", "++no-compile"]
      - id: check-script-semicolon
      - id: check-script-has-no-table-name
      - id: check-model-has-all-columns
        name: Check columns - core
        files: ^models/core
      - id: check-model-has-all-columns
        name: Check columns - mart
        files: ^models/mart
      - id: check-model-columns-have-desc
        files: ^models/mart
```

3. Optionally, run `pre-commit install` to set up the git hook scripts. Once installed, `pre-commit` will run automatically on `git commit`! You can also manually run `pre-commit run` after you `stage` all files you want to run. Or `pre-commit run --all-files` to run the hooks against all the files (not just `staged` files).

## Run in CI/CD

Unfortunately, you cannot natively use `dbt-checkpoint` if you are using **dbt Cloud**. But you can run checks after you push changes into GitHub.

`dbt-checkpoint` for the most of the hooks needs `manifest.json` (see requirements section in hook documentation), that is in the `target` folder. Since this target folder is usually in `.gitignore`, you need to generate it. For that you need to run the `dbt-parse` command.
To be able to parse dbt, you also need [profiles.yml](https://docs.getdbt.com/dbt-cli/configure-your-profile) file with your credentials. **To provide passwords and secrets use GitHub Secrets** (see example).

Say you want to check that a model contains at least two tests, you would use this configuration:

```yaml
repos:
  - repo: https://github.com/dbt-checkpoint/dbt-checkpoint
    rev: v1.2.1
    hooks:
      - id: check-model-has-tests
        args: ["--test-cnt", "2", "--"]
```

To be able to run this in GitHub CI you need to modified it to:

```yaml
repos:
  - repo: https://github.com/dbt-checkpoint/dbt-checkpoint
    rev: v1.2.1
    hooks:
      - id: dbt-parse
      - id: check-model-has-tests
        args: ["--test-cnt", "2", "--"]
```

### Create profiles.yml

First step is to create [profiles.yml](https://docs.getdbt.com/dbt-cli/configure-your-profile). E.g.

```yaml
# example profiles.yml file
jaffle_shop:
  target: dev
  outputs:
    dev:
      type: snowflake
      threads: 8
      client_session_keep_alive: true
      account: "{{ env_var('ACCOUNT') }}"
      database: "{{ env_var('DATABASE') }}"
      schema: "{{ env_var('SCHEMA') }}"
      user: "{{ env_var('USER') }}"
      password: "{{ env_var('PASSWORD') }}"
      role: "{{ env_var('ROLE') }}"
      warehouse: "{{ env_var('WAREHOUSE') }}"
```

and store this file in project root `./profiles.yml`.

### Create new workflow

- inside your GitHub repository create folder `.github/workflows` (unless it already exists).
- create new file e.g. `pr.yml`
- specify your workflow e.g.:

```yaml
name: dbt-checkpoint

on:
  push:
  pull_request:
    branches:
      - main

jobs:
  dbt-checkpoint:
    runs-on: ubuntu-latest
    env:
      ACCOUNT: ${{ vars.ACCOUNT }}
      DATABASE: ${{ vars.DATABASE }}
      SCHEMA: ${{ vars.SCHEMA }}
      USER: ${{ vars.USER }}
      PASSWORD: ${{ secrets.PASSWORD }}
      ROLE: ${{ vars.ROLE }}
      WAREHOUSE: ${{ vars.WAREHOUSE }}
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Setup Python
        uses: actions/setup-python@v2

      - id: Get file changes
        uses: trilom/file-changes-action@v1.2.4
        with:
          output: " "

      - name: Run dbt checkpoint
        uses: dbt-checkpoint/action@v0.1
        with:
          extra_args: --files ${{ steps.get_file_changes.outputs.files}}
          dbt_version: 1.6.3
          dbt_adapter: dbt-snowflake
```

### Acknowledgements

Thank you to [Radek Tomšej](https://github.com/tomsej) for initial development and maintenance of this great package, and for sharing your work with the community!
