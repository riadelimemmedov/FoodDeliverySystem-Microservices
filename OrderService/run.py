# Third party modules
import ujson as json
import uvicorn
from src.core.setup import config

# Local modules
from src.web.main import app


# !---------------------------------------------------------
#
def main():
    """Start uvicorn program."""
    # As soon as the SSL certificates are added, the shutdown period is
    # 30 seconds, unless the "timeout_graceful_shutdown" below is used.
    uv_config = {
        "log_level": config.service_log_level,
        "ssl_keyfile": "certs/private-key.pem",
        "ssl_certfile": "certs/public-cert.pem",
        "app": "src.web.main:app",
        "port": 8000,
        "timeout_graceful_shutdown": 1,
        "reload": True,
        "log_config": {"disable_existing_loggers": False, "version": 1},
    }
    """ uvicorn startup parameters. """

    # So you can se test the handling of different log levels.
    app.logger.info(f"{config.name} v{config.version} is initializing...")

    # Log config values for testing purposes.
    app.logger.trace(f"config: {json.dumps(config.model_dump(), indent=2)}")

    uvicorn.run(**uv_config)


if __name__ == "__main__":
    main()
