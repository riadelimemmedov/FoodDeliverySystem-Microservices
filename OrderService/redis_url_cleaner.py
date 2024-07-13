# BUILTIN modules
import asyncio

# Third party modules
from redis.asyncio import from_url

# Local modules
from src.core.setup import config

# Constants
URLS = {"PaymentService", "KitchenService", "DeliveryService", "CustomerService"}
""" Service dependencies."""


# !---------------------------------------------------------
#
async def cleaner():
    """Clean the redis URL cache."""
    client = from_url(config.redis_url)

    for key in URLS:
        data = await client.delete(key)
        print(f"deleting: {key}: {data}...")

    await client.aclose()


# !---------------------------------------------------------
#
if __name__ == "__main__":
    asyncio.run(cleaner())
