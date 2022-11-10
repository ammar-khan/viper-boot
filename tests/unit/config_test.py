from contextlib import nullcontext as does_not_raise

import pytest

from src.viper_boot.config import Config


@pytest.mark.parametrize(
    argnames="environment, expected, exception",
    argvalues=[
        ("production", "prd", does_not_raise()),
        ("development", "dev", does_not_raise()),
        ("exception", "", pytest.raises(KeyError))
    ],
    ids=[
        "it should return settings[`PROFILE`]=`prd` when environment is set as `production`.",  # noqa
        "it should return settings[`PROFILE`]=`dev` when environment is set as `development`.",  # noqa
        "it should raise exception when there is no environment set.",
    ]
)
def test_get(environment, expected, exception) -> None:
    # Arrange
    Config().environment = environment

    #  Act
    settings = Config().get

    # Assert
    with exception:
        assert settings["PROFILE"] == expected


@pytest.mark.parametrize(
    "environment, expected",
    [
        ("production", "production"),
        ("development", "development")
    ],
    ids=[
        "it should return `production` when environment is set as `production`.",  # noqa
        "it should return `development` when environment is set as `development`.",  # noqa
    ]
)
def test_get_environment(environment, expected) -> None:
    # Arrange
    Config().environment = environment

    # Act
    env = Config().environment

    # Assert
    assert env == expected
