# BUILTIN modules
from uuid import UUID
from typing import Optional

# Third party modules
import stripe
from loguru import logger
from uuid_extensions import uuid7

# Local modules
from ..core.setup import config


# !------------------------------------------------------------------------
#
class StripeService:
    def __init__(self):
        stripe.api_key = config.STRIPE_SECRET_KEY

    # !------------------------------------------------------------------------
    #
    @staticmethod
    async def _charge_credit_card(
        amount: float, currency: Optional[str] = "usd"
    ) -> UUID:
        """Charge a credit card using Stripe.

        :ivar amount: Amount come for order summary.
        :itype amount: `float`.
        :ivar currency: Currency of the amount (default is 'usd').
        :itype currency: `str`.
        :return: UUID of the charge.
        :raise RuntimeError: When Stripe charge fails.
        """
        # item = {
        #         "name": str(pet[2]),
        #         "quantity": 1,
        #         "currency": "usd",
        #         "amount": round(int(pet[4]["hex"], 16) * 100),
        # }
        # line_items.append(item)

        line_items = []
        try:
            # create new checkout session for payment
            checkout_session = stripe.checkout.Session.create(
                success_url=config.DOMAIN_URL
                + "success?session_id={CHECKOUT_SESSION_ID}",
                cancel_url=config.DOMAIN_URL + "canceled",
                payment_method_types=["card"],
                mode="payment",
                line_items=line_items,
            )
            return UUID(checkout_session["id"])
        except stripe.error.StripeError as e:
            errmsg = f"Failed sending POST request to Stripe - [{e.user_message}]."
            logger.error(errmsg)
            raise RuntimeError(errmsg)


stripe_service = StripeService()
