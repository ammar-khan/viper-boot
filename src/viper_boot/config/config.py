"""Application Config Module."""
from pathlib import Path
from typing import Any

from dynaconf import Dynaconf

from src.viper_boot.utils.decorators.singleton_decorator import (
    singleton
)

PACKAGE_NAME = "viper_boot"


@singleton
class Config:
    """Application settings."""

    _CONFIG_PATH = (
        Path().absolute().joinpath("src/viper_boot/config")
    )

    _environment: str

    def __init__(self, env: str = "development") -> None:
        """
        Look into environment files and return settings based of env.

        Parameters:
            env (str): Environment

        @see https://dynaconf.readthedocs.io/en/docs_223/guides/advanced_usage.html # noqa
        """
        self._environment = env

        # Create `settings` instance
        # More options on https://www.dynaconf.com/configuration/
        self.settings = Dynaconf(
            settings_files=[  # Paths or globs to any toml|yaml|ini|json|py
                f"{self._CONFIG_PATH}/settings.toml",  # Default settings  # noqa
                f"{self._CONFIG_PATH}/settings_dev.toml",  # Dev settings
                f"{self._CONFIG_PATH}/settings_prd.toml",  # Prd settings
                f"{self._CONFIG_PATH}/.secrets.toml"  # Sensitive data (gitignored)  # noqa
            ],

            environments=True,  # Enable layered environments
            # (sections on config file for development, production, testing)

            load_dotenv=True,  # Load envvars from a file named `.env`
            # TIP: probably you don't want to load dotenv on production environments # noqa
            #      pass `load_dotenv={"when": {"env": {"is_in": ["development"]}}} # noqa

            envvar_prefix="DYNACONF",  # variables exported as `DYNACONF_FOO=bar` becomes `settings.FOO == "bar"`  # noqa
            env_switcher="ENV",  # to switch environments `export ENV=production`  # noqa

            dotenv_path="configs/.env"  # custom path for .env file to be loaded  # noqa
        )

        # NOTE: On Dynaconf 4.0.0 all the above will be also possible as a pydantic schema :)  # noqa

    @property
    def get(self) -> Any:
        """
        Getter method for settings.

        Returns:
            Application settings
        """
        return self.settings.from_env(self._environment).as_dict()

    @property
    def environment(self) -> Any:
        """
        Getter method for environment.

        Returns:
            Application environment
        """
        return self._environment

    @environment.setter
    def environment(self, value: str) -> None:
        """
        Setter method for environment.

        Parameters:
            value (str): value to set
        """
        self._environment = value
