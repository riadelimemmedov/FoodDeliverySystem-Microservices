# Third party modules
from motor.motor_asyncio import AsyncIOMotorClient

# Local program modules
from ..core.setup import config


# !-----------------------------------------------------------------------------
#
class Engine:
    """MongoDb database async engine class.

    :ivar client: MongoDB motor async client object.
    :type client: AsyncIOMotorClient
    """

    client: AsyncIOMotorClient = None

    # !---------------------------------------------------------
    #
    @classmethod
    async def create_db_connection(cls):
        """Initialize connection to MongoDb.

        Setting server connection timeout to 5 (default is 30) seconds.
        """
        cls.client = AsyncIOMotorClient(
            config.mongo_url,
            uuidRepresentation="standard",
            serverSelectionTimeoutMS=5000,
        )

    # !---------------------------------------------------------
    #
    @classmethod
    async def close_db_connection(cls):
        """Close MongoDB connection."""
        if cls.client:
            cls.client.close()

    # !---------------------------------------------------------
    #
    @classmethod
    async def is_db_connected(cls) -> bool:
        """Return MongoDB connection status."""
        return bool(cls.client.server_info())
