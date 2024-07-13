# BUILTIN modules
from typing import Protocol
from uuid import UUID

# Local modules
from .models import PaymentModel


# !-----------------------------------------------------------------------------
#
class IRepository(Protocol):
    """Payment DB Interface class."""

    async def create(self, payload: PaymentModel) -> bool:
        """Create Payment.

        :param payload: New Payment payload.
        :return: DB create response.
        """

    async def read(self, key: UUID) -> PaymentModel:
        """Read Payment for matching index key.

        :param key: Index key.
        :return: Found Payment.
        """

    async def update(self, payload: PaymentModel) -> bool:
        """Update Payment.

        :param payload: Updated Order payload.
        :return: DB update result.
        """
