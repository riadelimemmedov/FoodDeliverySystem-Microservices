# BUILTIN modules
from typing import Protocol


# -----------------------------------------------------------------------------
#
class IBroker(Protocol):
    """Payment Broker Interface class."""

    # !---------------------------------------------------------
    #
    async def publish(self, queue: str, message: dict):
        """Publish a message on specified RabbitMQ queue asynchronously.

        :param queue: Publishing queue.
        :param message: Message to be published.
        """

    # !---------------------------------------------------------
    #
    def is_connected(self) -> bool:
        """Return connection status."""
