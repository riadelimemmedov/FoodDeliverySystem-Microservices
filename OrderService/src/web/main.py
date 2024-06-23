# BUILTIN modules
import os
import signal
import asyncio
from pathlib import Path
from contextlib import asynccontextmanager

# Third party modules
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Local modules
from ..core.setup import config
from ..repository.db import Engine
from .api import api, health_route
from .api.models import ValidStatus
from ..tools.rabbit_client import RabbitClient
from ..repository.unit_of_work import UnitOfRepositoryWork
from .order_event_adapter import OrderEventAdapter
from ..tools.custom_logging import create_unified_logger
from .api.documentation import servers, license_info, tags_metadata, description

# Constants
HDR_DATA = {
    "Content-Type": "application/json",
    "X-API-Key": f"{config.service_api_key}",
}


# !---------------------------------------------------------
#
class Service(FastAPI):
    """This class extends the FastAPI class for the OrderService API.

    The following functionality is added:
        - unified logging.
        - includes API router.
        - Instantiates a RabbitMQ client.
        - Defines a static path for images in the documentation.
        - Adds a method that handles RabbitMQ response message in a separate task.

    :ivar rabbit_client: RabbitMQ client.
    :type rabbit_client: `RabbitClient`
    :ivar logger: Unified loguru logger object.
    :type logger: loguru.logger
    """

    def __init__(self, *args: int, **kwargs: dict):
        """This class adds RabbitMQ message consumption and unified logging.

        :param args: Named arguments.
        :param kwargs: Key-value pair arguments.
        """
        super().__init__(*args, **kwargs)

        # Needed for OpenAPI Markdown images to be displayed.
        static_path = Path(__file__).parent.parent.parent.parent / "design_docs"
        self.mount("/static", StaticFiles(directory=static_path))

        self.rabbit_client = RabbitClient(
            config.rabbit_url, config.service_name, self.process_response_message
        )

        # Add declared router information.
        self.include_router(api.ROUTER)
        self.include_router(health_route.ROUTER)

        # Unify logging within the imported package's closure.
        self.logger = create_unified_logger()
