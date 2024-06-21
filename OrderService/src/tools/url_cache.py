# Third party modules
from redis.asyncio import from_url

# Local modules
from ..repository.db import Engine

# Constants
EXPIRE = 60 * 60 * 24
""" Cached service URLs expire after 24h. """


# !------------------------------------------------------------------------
#
class UrlServiceCache:
    """This class handles Redis URL cache.

    Is automatically populated from MongoDB api_db.service_urls collection.

    :ivar client: Current Redis instance.
    :type client: ``redis.asyncio.Redis``
    """

    # !---------------------------------------------------------
    #
    def __init__(self, url: str):
        """The class initialize redis server async format.

        :param url: Redis connection URL.
        """
        self.client = from_url(url)

    # !---------------------------------------------------------
    #
    async def get(self, key: str) -> str:
        """Get MicroService URL from Redis.

        Populate from MongoDB api_db.service_urls collection if needed.
        All URL Keys expire after 24h in the cache.

        :param key: MicroService name.
        :return: MicroService URL.
        """
        value = await self.client.get(key)

        if not value:
            value = await Engine.client.api_db.service_urls.find_one({"_id": key})
            await self.client.set(key, value["url"], ex=EXPIRE)

        return value.decode() if isinstance(value, bytes) else value["url"]

    # !---------------------------------------------------------
    #
    async def close(self):
        """Close redis connection."""
        await self.client.close()
