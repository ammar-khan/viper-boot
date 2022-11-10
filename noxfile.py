"""Nox sessions."""
import os
import shutil
import sys
import unicodedata
from pathlib import Path
from tempfile import NamedTemporaryFile
from textwrap import dedent

import nox
from pre_commit import color
from pre_commit import output


PACKAGE_NAME = "viper_boot"
PYTHON_VERSIONS = ["3.10", "3.9", "3.8", "3.7"]
SRC_FILES_PATH = f"src/{PACKAGE_NAME}"
PATH_ENVIRONMENT = {"PYTHONPATH": "src"}
LOOP_BACK_IP = "127.0.0.1"
DOC_PORT = "8000"
DOC_URL = f"http://{LOOP_BACK_IP}:{DOC_PORT}"
FOLDERS_TO_CLEAN = [
    ".reports", ".serverless", ".mypy_cache", ".nox", ".pytest_cache", "dist"
]
REPORTS_FOLDER = ".reports"
SERVERLESS_FOLDER = ".serverless"

SESSION_PASSED_COLOR = color.GREEN
SESSION_SUCCESS_COLOR = color.TURQUOISE
SESSION_WARNING_COLOR = color.YELLOW
SESSION_PASSED_STATUS = "Passed"
SESSION_SUCCESS_STATUS = "Success"
SESSION_SKIPPED_STATUS = "Skipped"

try:
    from nox_poetry import Session, session
except ImportError:
    message = f"""\
    Nox failed to import the "nox-poetry" package.
    Please install it using the following command:
    {sys.executable} -m pip install nox-poetry"""
    raise SystemExit(dedent(message)) from None

nox.options.error_on_external_run = True
nox.options.reuse_existing_virtualenvs = True
nox.options.stop_on_first_error = True

nox.options.sessions = (
    "clean",
    "initialise",
    "pre-commit",
    "mypy",
    "flake8-diff",
    "pylint-diff",
    "pytest",
    "coverage",
    "coverage-html-report",
    "coverage-lcov-report",
    "xdoctest",
    "safety",
    "safety-report",
    "bandit",
    "mkdocs-build",
    "start",
)


@session(venv_backend="none")
def clean(_session: Session) -> None:
    """Task to clean sessions.

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    for _dir in FOLDERS_TO_CLEAN:
        directory = Path(_dir)
        if directory.exists():
            shutil.rmtree(directory)

    os.makedirs(REPORTS_FOLDER)

    # Print status
    output.write(
        _full_msg(
            start_msg="clean",
            postfix='',
            end_msg=SESSION_SUCCESS_STATUS,
            end_color=SESSION_SUCCESS_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(venv_backend="none")
def initialise(_session: Session) -> None:
    """Task to initialise.

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    _session.run(
        "poetry",
        "install",
        "--sync",
        *_session.posargs,
    )
    _session.run(
        "poetry",
        "lock",
        "--no-update",
        *_session.posargs,
    )
    _session.run(
        "poetry",
        "update",
        *_session.posargs,
    )

    # Print status
    output.write(
        _full_msg(
            start_msg="initialise",
            postfix='',
            end_msg=SESSION_SUCCESS_STATUS,
            end_color=SESSION_SUCCESS_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(python=PYTHON_VERSIONS[0])
def start(_session: Session) -> None:
    """Task to start application.

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    _session.install(
        ".",
        "click",
        "dynaconf",
        "marshmallow",
        "apispec",
    )
    _session.run(
        "python",
        "-m",
        f"{PACKAGE_NAME}.__main__",
        *_session.posargs,
    )

    # Print status
    output.write(
        _full_msg(
            start_msg="start",
            postfix='',
            end_msg=SESSION_SUCCESS_STATUS,
            end_color=SESSION_SUCCESS_COLOR,
            use_color=True,
            cols=80,
        ),
    )


# For some sessions, set venv_backend="none" to simply execute scripts within
# the existing Poetry environment. This requires that nox is run
# within `poetry shell` or using `poetry run nox ...`.
@session(name="flake8-diff", venv_backend="none")
def flake8_diff(_session: Session) -> None:
    """Task to do "code linting" only changed files, using flake8.

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    # Run pyproject-flake8 entrypoint to support
    # reading configuration from pyproject.toml.
    _session.run(
        "bash",
        "-c",
        """pflake8 `git diff --name-only "$@" :^tests | grep -E ".py$"`""",
    )

    # Print status
    output.write(
        _full_msg(
            start_msg="flake8-diff",
            postfix='',
            end_msg=SESSION_PASSED_STATUS,
            end_color=SESSION_PASSED_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(venv_backend="none")
def flake8(_session: Session) -> None:
    """Task to do "code linting" using flake8.

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    # Run pyproject-flake8 entrypoint to support
    # reading configuration from pyproject.toml.
    _session.run("pflake8", f"./src/{PACKAGE_NAME}")

    # Print status
    output.write(
        _full_msg(
            start_msg="flake8",
            postfix='',
            end_msg=SESSION_PASSED_STATUS,
            end_color=SESSION_PASSED_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(venv_backend="none")
def pylint(_session: Session) -> None:
    """Task to do "code linting" using pylint.

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    _session.run("pylint", f"./src/{PACKAGE_NAME}")

    # Print status
    output.write(
        _full_msg(
            start_msg="pylint",
            postfix='',
            end_msg=SESSION_PASSED_STATUS,
            end_color=SESSION_PASSED_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(name="pylint-diff", venv_backend="none")
def pylint_diff(_session: Session) -> None:
    """Task to do "code linting" only changed files, using pylint.

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    _session.run(
        "bash",
        "-c",
        """pylint -rn `git diff --name-only "$@" :^tests | grep -E ".py$"`""",
    )

    # Print status
    output.write(
        _full_msg(
            start_msg="pylint-diff",
            postfix='',
            end_msg=SESSION_PASSED_STATUS,
            end_color=SESSION_PASSED_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(name="prettify", python=PYTHON_VERSIONS[0])
def darker(_session: Session) -> None:
    """Task to do "formatting, sorting and linting" changed files only.

    Using:
        black: to reformat the code (Default)
        isort: reorder imports
        mypy: do static type checking using
        pylint: analyze code using
        flake8: enforce the Python style guide using
        cov_to_lint.py: read .coverage and list non-covered modified lines

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    _session.install("darker", "pylint")
    _session.run(
        "darker",
        "--isort",
        "--lint",
        "pylint",
    )

    # Print status
    output.write(
        _full_msg(
            start_msg="darker",
            postfix='',
            end_msg=SESSION_PASSED_STATUS,
            end_color=SESSION_PASSED_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(python=PYTHON_VERSIONS[0])
def mypy(_session: Session) -> None:
    """Type-check using mypy.

    Parameters:
        _session (Session): Session object

    Raises:
        Runtime error

    Return:
        None
    """
    args = _session.posargs or [
        f"src/{PACKAGE_NAME}",
    ]
    _session.install(".")
    _session.install("mypy")

    _session.run(
        "mypy",
        f"--python-executable={sys.executable}",
        * args
    )

    # Print status
    output.write(
        _full_msg(
            start_msg="mypy",
            postfix='',
            end_msg=SESSION_PASSED_STATUS,
            end_color=SESSION_PASSED_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(python=PYTHON_VERSIONS[0])
def pytest(_session: Session) -> None:
    """Run the test suite.

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    args = _session.posargs or [
        "-s",
        "-v",
        "--durations=5",
        # "--picked", TODO: Need to fix error, if no test collected
        # "--testmon", TODO: Need to fix error, if no test collected
        "--xdoctest",
        f"--typeguard-packages={PACKAGE_NAME}",
        "--import-mode=importlib",
        "tests",
    ]
    _session.install(".")
    _session.install(
        "coverage[toml]",
        "pytest",
        # "pytest-picked", TODO: Need to fix error, if no test collected
        # "pytest-testmon", TODO: Need to fix error, if no test collected
        "pytest-watch",
        "pytest-randomly",
        "pytest-mock",
        "typeguard",
        "xdoctest",
        "pygments",
    )
    try:
        _session.run(
            "coverage",
            "run",
            "--parallel",
            "--branch",
            "-m",
            "pytest",
            *args,
        )
    finally:
        if _session.interactive:
            _session.notify("coverage", posargs=[])

    # Print status
    output.write(
        _full_msg(
            start_msg="pytest",
            postfix='',
            end_msg=SESSION_PASSED_STATUS,
            end_color=SESSION_PASSED_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(python=PYTHON_VERSIONS[0])
def coverage(_session: Session) -> None:
    """Combine all coverage data and report.

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    args = _session.posargs or [
        "report",
        "-m"
    ]

    _session.install("coverage[toml]")

    if not _session.posargs and any(Path().glob(".coverage.*")):
        _session.run("coverage", "combine")

    _session.run("coverage", *args)

    # Print status
    output.write(
        _full_msg(
            start_msg="coverage",
            postfix='',
            end_msg=SESSION_PASSED_STATUS,
            end_color=SESSION_PASSED_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(name="coverage-html-report", python=PYTHON_VERSIONS[0])
def coverage_html_report(_session: Session) -> None:
    """Generate HTML coverage report.

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    args = _session.posargs or [
        "html",
        "-d",
        f"{REPORTS_FOLDER}"
    ]

    _session.install("coverage[toml]")
    _session.run("coverage", *args)

    # Print status
    output.write(
        _full_msg(
            start_msg="coverage-html-report",
            postfix='',
            end_msg=SESSION_SUCCESS_STATUS,
            end_color=SESSION_SUCCESS_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(name="coverage-lcov-report", python=PYTHON_VERSIONS[0])
def coverage_lcov_report(_session: Session) -> None:
    """Generate LCOV coverage report.

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    args = _session.posargs or [
        "lcov",
        "-o",
        f"{REPORTS_FOLDER}/coverage.lcov"
    ]

    _session.install("coverage[toml]")
    _session.run("coverage", *args)

    # Print status
    output.write(
        _full_msg(
            start_msg="coeverage-lcov-report",
            postfix='',
            end_msg=SESSION_SUCCESS_STATUS,
            end_color=SESSION_SUCCESS_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(python=PYTHON_VERSIONS[0])
def xdoctest(_session: Session) -> None:
    """Run examples with xdoctest.

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    if _session.posargs:
        args = [PACKAGE_NAME, *_session.posargs]
    else:
        args = [
            f"--modname={PACKAGE_NAME}",
            "--command=all",
            "--colored=1",
        ]

    _session.install(".")
    _session.install("xdoctest[colors]")
    _session.run("python", "-m", "xdoctest", *args)

    # Print status
    output.write(
        _full_msg(
            start_msg="xdoctest",
            postfix='',
            end_msg=SESSION_PASSED_STATUS,
            end_color=SESSION_PASSED_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(python=PYTHON_VERSIONS[0])
def safety(_session: Session) -> None:
    """Scan dependencies for insecure packages.

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    requirements = _session.poetry.export_requirements()
    _session.install("safety")
    _session.run(
        "safety",
        "check",
        "--full-report",
        f"--file={requirements}",
        *_session.posargs,
    )

    # Print status
    output.write(
        _full_msg(
            start_msg="safety",
            postfix='',
            end_msg=SESSION_PASSED_STATUS,
            end_color=SESSION_PASSED_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(name="safety-report", python=PYTHON_VERSIONS[0])
def safety_report(_session: Session) -> None:
    """Report dependencies for insecure packages.

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    requirements = _session.poetry.export_requirements()
    _session.install("safety")
    _session.run(
        "bash",
        "-c",
        f"safety check --file={requirements} -o json > {REPORTS_FOLDER}/safety.json",  # noqa: E501  # pylint: disable=line-too-long
        external=True,
    )

    # Print status
    output.write(
        _full_msg(
            start_msg="safety-report",
            postfix='',
            end_msg=SESSION_SUCCESS_STATUS,
            end_color=SESSION_SUCCESS_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(venv_backend="none")
def bandit(_session: Session) -> None:
    """Scan code for vulnerabilities.

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    args = _session.posargs or [
        "-f",
        "html",
        "-o",
        f"{REPORTS_FOLDER}/bandit.html"
    ]

    _session.run(
        "bandit",
        "-c",
        "pyproject.toml",
        "-r",
        ".",
        *args,
    )

    # Print status
    output.write(
        _full_msg(
            start_msg="bandit",
            postfix='',
            end_msg=SESSION_PASSED_STATUS,
            end_color=SESSION_PASSED_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(name="mkdocs-build", venv_backend="none")
def mkdocs(_session: Session) -> None:
    """Task to generate "code reference documents".

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    _session.run("mkdocs", "build", env=PATH_ENVIRONMENT)

    # Print status
    output.write(
        _full_msg(
            start_msg="Code reference documents build",
            postfix='',
            end_msg=SESSION_SUCCESS_STATUS,
            end_color=SESSION_SUCCESS_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(name="mkdocs-serve", venv_backend="none")
def mkdocs_serve(_session: Session) -> None:
    """Task to serve "code reference documents".

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    # Open browser
    _session.run("python", "-m", "webbrowser", "-t", DOC_URL)

    _session.run(
        "bash",
        "-c",
        f"lsof -ti:{DOC_PORT} | xargs kill",
    )
    _session.run(
        "mkdocs",
        "serve",
        env=PATH_ENVIRONMENT,
    )

    # Print status
    output.write(
        _full_msg(
            start_msg="Code reference documents served",
            postfix='',
            end_msg=SESSION_SUCCESS_STATUS,
            end_color=SESSION_SUCCESS_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(name="mkdocs-deploy", venv_backend="none")
def mkdocs_deploy(_session: Session) -> None:
    """Task to deploy "code reference documents".

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    _session.run("mkdocs", "gh-deploy", "--force", env=PATH_ENVIRONMENT)

    # Print status
    output.write(
        _full_msg(
            start_msg="Code reference documents deployed",
            postfix='',
            end_msg=SESSION_SUCCESS_STATUS,
            end_color=SESSION_SUCCESS_COLOR,
            use_color=True,
            cols=80,
        ),
    )


# Note: This reuse_venv does not yet have affect due to:
#   https://github.com/wntrblm/nox/issues/488
@session(name="pip-licenses", reuse_venv=False)
def pip_licenses(_session: Session) -> None:
    """Task to generate "package licenses".

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    # Generate a unique temporary file name.
    # Poetry cannot write to the temp file directly on
    # Windows, so only use the name and allow Poetry to re-create it.
    with NamedTemporaryFile() as tmp_file:
        requirements_file = Path(tmp_file.name)

    # Install dependencies without installing the package itself:
    # @see: https://github.com/cjolowicz/nox-poetry/issues/680
    _session.run_always(
        "poetry",
        "export",
        "--without-hashes",
        f"--output={requirements_file}",
        external=True,
    )
    _session.install("pip-licenses", "-r", str(requirements_file))
    _session.run("pip-licenses", *_session.posargs)
    requirements_file.unlink()

    # Print status
    output.write(
        _full_msg(
            start_msg="Generate PIP licenses",
            postfix='',
            end_msg=SESSION_SUCCESS_STATUS,
            end_color=SESSION_SUCCESS_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(name="pre-commit", python=PYTHON_VERSIONS[0])
def pre_commit(_session: Session) -> None:
    """Pre commit hooks".

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    _session.install("pre-commit", "pycln")
    _session.run("pre-commit", "install")
    _session.run("pre-commit", "autoupdate")
    _session.run("pre-commit", "run", "--all-files")

    # Print status
    output.write(
        _full_msg(
            start_msg="pre-commit hooks",
            postfix='',
            end_msg=SESSION_SUCCESS_STATUS,
            end_color=SESSION_SUCCESS_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(name="build-serverless-package", python=PYTHON_VERSIONS[0])
def build_serverless_package(_session: Session) -> None:
    """Task to build AWS SAM package for Serverless Lambda.

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    aws_dir = Path(SERVERLESS_FOLDER)
    if aws_dir.exists():
        shutil.rmtree(aws_dir)

    os.makedirs(SERVERLESS_FOLDER)

    _session.run(
        "bash",
        "-c",
        "pip install -t dist/lambda .",
        external=True,
    )
    _session.run(
        "bash",
        "-c",
        f"zip -x '*.pyc' -r {SERVERLESS_FOLDER}/lambda.zip dist/lambda .",
        external=True,
    )

    # Print status
    output.write(
        _full_msg(
            start_msg="Build serverless package",
            postfix='',
            end_msg=SESSION_SUCCESS_STATUS,
            end_color=SESSION_SUCCESS_COLOR,
            use_color=True,
            cols=80,
        ),
    )


@session(reuse_venv=False)
def commit(_session: Session) -> None:
    """Task to commit using conventional commits.

    Parameters:
        _session (Session): Session object

    Return:
        None
    """
    # Print message
    output.write(
        _full_msg(
            start_msg="commit:",
            postfix="",
            end_msg="Add files to staging before commit.",
            end_color=SESSION_WARNING_COLOR,
            use_color=True,
            cols=80,
        ),
    )

    _session.install("pre-commit", "pycln")
    _session.run("pre-commit", "install")
    _session.run("pre-commit", "autoupdate")
    _session.run("pre-commit", "run", "--all-files")

    # Commit changes
    _session.run(
        "bash",
        "-c",
        "git cz commit",
        external=True,
    )

    # Bump the version and add it to changelog
    _session.run(
        "bash",
        "-c",
        "git cz bump --changelog",
        external=True,
    )


def _len_cjk(msg: str) -> int:
    """
    Check length of the message.

    Parameters:
        msg (str): message

    Returns:
        length of the message
    """
    widths = {"A": 1, "F": 2, "H": 1, "N": 1, "Na": 1, "W": 2}
    return sum(widths[unicodedata.east_asian_width(c)] for c in msg)


def _full_msg(
    *,
    start_msg: str,
    cols: int,
    end_msg: str,
    end_color: str,
    use_color: bool,
    postfix: str = '',
) -> str:
    """
    Check length of the message.

    Parameters:
        start_msg (str): start message
        cols (int): number of columns
        end_msg (str): end message
        end_color (str): end message color
        use_color (bool): user color or not
        postfix (str): any postfix to the message

    Returns:
        formatted message
    """
    dots = "." * (cols - _len_cjk(start_msg) - len(postfix) - len(end_msg) - 1)
    end = color.format_color(end_msg, end_color, use_color)
    return f"{start_msg}{dots}{postfix}{end}\n"
