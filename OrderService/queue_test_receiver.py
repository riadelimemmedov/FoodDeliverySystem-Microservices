# BUILTIN modules
import asyncio
import contextlib

# Local modules
from src.core.setup import config
from src.tools.rabbit_client import RabbitClient

# Constants
SERVICE = "TestService"
""" Service name. """


# !---------------------------------------------------------
#
async def process_incoming_message(message: dict):
    """Print the incoming message.

    :param message: Incoming message.
    """
    print(f"Received: {message}")


# !---------------------------------------------------------
#
async def receiver():
    """Receive RabbitMQ messages."""
    print("Started RabbitMQ message queue subscription...")
    client = RabbitClient(config.rabbit_url, SERVICE, process_incoming_message)
    await client.start()
    await asyncio.create_task(client.start_subscription())

    try:
        # Wait until termination.
        await asyncio.Future()

    finally:
        await client.stop()


# !---------------------------------------------------------
#
if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(receiver())
