# Package / Application

## Environment setup

!!! hint

    To know how to setup environment please click [here](contribute.md#Environment setup).

Then install the project and dependencies:

```bash
poetry install
```

Then update the project and dependencies:

```bash
poetry update
```

Activate the virtual environment created automatically by Poetry:

```bash
poetry shell
```

## Quick start

```bash
nox
```


## References

<div class="center-table" markdown>

| **Task / Session**                | **Description**                                         |
|-----------------------------------|---------------------------------------------------------|
| `poetry install`                  | Install the package and its dependencies                |
| `poetry update`                   | Update the package and its dependencies                 |
| `poetry shell`                    | Activate the virtual environment of Poetry              |
| `exit`                            | Deactivate the virtual environment of Poetry            |
| `nox`                             | Run all tasks (sessions)                                |
| `nox -s clean`                    | Clean package directory                                 |
| `nox -s initialise`               | Refresh virtual environment                             |
| `nox -s start`                    | Start the application (API)                             |
| `nox -s pre-commit`               | Pre commit hooks for Python package                     |
| `nox -s flake8`                   | Validate Python style guide across the package          |
| `nox -s flake8-diff`              | Validate Python style guide only for files changed      |
| `nox -s pylint`                   | Lint Python code across the package                     |
| `nox -s pylint-diff`              | Lint Python code only for files changed                 |
| `nox -s mypy`                     | Validate Python types                                   |
| `nox -s pytest`                   | Run tests                                               |
| `nox -s coverage`                 | Collect test coverage data and generate text report     |
| `nox -s coverage-html-report`     | Generate HTML report for test coverage                  |
| `nox -s coverage-lcov-report`     | Generate LCOV report for test coverage                  |
| `nox -s xdoctest`                 | Run examples with tests written inside code documents   |
| `nox -s safety`                   | Scan packages for vulnerabilities                       |
| `nox -s safety-report`            | Generate packages vulnerabilities report in json format |
| `nox -s bandit`                   | Scan code for vulnerabilities                           |
| `nox -s mkdocs-build`             | Generate code reference documents                       |
| `nox -s mkdocs-serve`             | Serve / Open generated code reference documents         |
| `nox -s mkdocs_deploy`            | Deploy generated code reference documents to git hub    |
| `nox -s pip-licenses`             | Generate licenses for package                           |
| `nox -s build-serverless-package` | Build serverless package                            |

</div>

!!! tip

    If you want to run specific tasks only:
    ```bash
    nox -s prettier clean initialise start
    ```

## Troubleshoot

If virtual environment already activated
```bash
source "$( poetry env list --full-path | grep Activated | cut -d' ' -f1 )/bin/activate"
```

To import and export dependencies

=== "Import (requirements.txt -> pyproject.toml)"

    ```bash
    cat requirements.txt|grep -v '#'|xargs poetry add
    ```

=== "Export (pyproject.toml -> requirements.txt)"

    ```bash
    poetry export --output requirements.txt
    ```

To add development dependency
```bash
poetry add pytest@latest --dev
```

To remove anything that’s not necessary.
```bash
poetry install --sync
```

If you can't able to run pre-commit hooks.
```bash
chmod ug+x .git/hooks/*
```

## Poetry command reference

<div class="center-table" markdown>

| Poetry Command            | Explanation                                                           |
|---------------------------|-----------------------------------------------------------------------|
| $ poetry --version        | Show the version of your Poetry installation.                         |
| $ poetry new              | Create a new Poetry project.                                          |
| $ poetry init             | Add Poetry to an existing project.                                    |
| $ poetry run              | Execute the given command with Poetry.                                |
| $ poetry add              | Add a package to pyproject.toml and install it.                       |
| $ poetry update           | Update your project’s dependencies.                                   |
| $ poetry install          | Install the dependencies.                                             |
| $ poetry show             | List installed packages.                                              |
| $ poetry lock             | Pin the latest version of your dependencies into poetry.lock.         |
| $ poetry lock --no-update | Refresh the poetry.lock file without updating any dependency version. |
| $ poetry check            | Validate pyproject.toml.                                              |
| $ poetry config --list    | Show the Poetry configuration.                                        |
| $ poetry env list         | List the virtual environments of your project.                        |
| $ poetry export           | Export poetry.lock to other formats.                                  |

</div>
To learn more about poetry click [here](https://python-poetry.org/docs/master/).
