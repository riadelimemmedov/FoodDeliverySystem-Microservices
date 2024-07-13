# BUILTIN modules
import os
import site
from os import getenv
from pathlib import Path
from ssl import SSLContext
from typing import Tuple, Type

# Third party modules
from pydantic import Field, computed_field
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)

# Constants
ENVIRONMENT = getenv("ENVIRONMENT", "dev")
""" Current platform environment. """
MISSING_SECRET = ">>> missing SECRETS file <<<"
""" Error message for missing secrets file. """
MISSING_ENV = ">>> missing ENV value <<<"
""" Error message for missing values in the .env file. """
CERT_PATH = Path(__file__).parent.parent.parent / "certs"
""" Local certificate path. """
SECRETS_DIR = (
    "/run/secrets" if os.path.exists("/.dockerenv") else f"{site.getuserbase()}/secrets"
)
""" This is where your secrets are stored (in Docker or locally). """
# noinspection PyNoneFunctionAssignment
SSL_CONTEXT = SSLContext().load_cert_chain(
    f"{CERT_PATH}/public-cert.pem", f"{CERT_PATH}/private-key.pem"
)
""" Define the SSL context certificate chain. """


# !---------------------------------------------------------
#
class Configuration(BaseSettings):
    """Configuration parameters.

    :ivar model_config: Changes default settings in the BaseSettings class.
    :type model_config: SettingsConfigDict
    :ivar name: Microservice API name.
    :ivar version: Microservice API version.
    :ivar service_name: Microservice name.
    :ivar service_log_level:  Microservice log level.
    :ivar url_timeout: Timeout values used for http/https requests.
    :ivar service_api_key: Web sservice API key.
    :ivar mongo_url: The MongoDB URL.
    :ivar redis_url: The Redis URL.
    :ivar rabbit_url: The RabbitMQ URL.
    """

    model_config = SettingsConfigDict(
        secrets_dir=SECRETS_DIR,
        env_file_encoding="utf-8",
        env_file=Path(__file__).parent / ".env",
    )

    # !OpenAPI documentation.
    name: str = MISSING_ENV
    version: str = MISSING_ENV

    # !Service parameters.
    service_name: str = MISSING_ENV
    service_log_level: str = MISSING_ENV

    # !External resource parameters.
    url_timeout: tuple = (1.0, 5.0)
    service_api_key: str = MISSING_SECRET
    mongo_url: str = Field(MISSING_SECRET, alias=f"mongo_url_{ENVIRONMENT}")
    redis_url: str = Field(MISSING_SECRET, alias=f"redis_url_{ENVIRONMENT}")
    rabbit_url: str = Field(MISSING_SECRET, alias=f"rabbit_url_root_{ENVIRONMENT}")

    @computed_field
    @property
    def hdr_data(self) -> dict:
        """Use a defined secret as a value."""
        return {
            "Content-Type": "application/json",
            "X-API-Key": f"{self.service_api_key}",
        }

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        env_settings: PydanticBaseSettingsSource,
        init_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        """Change source priority order (ignore environment values)."""
        return init_settings, dotenv_settings, file_secret_settings


# !---------------------------------------------------------
config = Configuration()
""" Configuration parameters instance. """
