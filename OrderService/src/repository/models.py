# BUILTIN modules
from enum import Enum
from uuid import UUID
from datetime import datetime, UTC
from typing import Optional, Callable, List

# Third party modules
from uuid_extensions import uuid7
from pydantic import BaseModel, ConfigDict, Field, conlist, PositiveInt

# Local modules
from .documentation import order_documentation as order_doc


# !---------------------------------------------------------
#
def utcnow():
    """Return the current datetime with a UTC timezone.

    :return: Current UTC datetime.
    """
    return datetime.now(UTC)


# !---------------------------------------------------------
#
# noinspection IncorrectFormatting
class Status(str, Enum):
    """Order status changes.

    CREA -> PAID/FAIL -> DISC -> DRAV -> SHED -> COOK -> PROD -> PICK -> TRAN -> DONE

    An Order can be canceled before DRAV status has been reached (finding an available
    driver sometimes takes time, so the Customer is unwilling to wait any longer).


    :ivar CREA: OrderService state.
    :ivar ORCA: OrderService state.
    :ivar PAID: PaymentService state.
    :ivar REIM: PaymentService state.
    :ivar FAIL: PaymentService state.
    :ivar DESC: DeliveryService state.
    :ivar DRAV: DeliveryService state.
    :ivar SHED: KitchenService state.
    :ivar COOK: KitchenService state.
    :ivar PROD: KitchenService state.
    :ivar PICK: KitchenService state.
    :ivar TRAN: DeliveryService state.
    :ivar DONE: DeliveryService state.
    """

    CREA = "created"
    ORCA = "orderCancelled"
    PAID = "paymentPaid"
    REIM = "reimbursed"
    FAIL = "paymentFailed"
    DESC = "deliveryScheduled"
    DRAV = "driverAvailable"
    SHED = "cookingScheduled"
    COOK = "cookingMeal"
    PROD = "cookingDone"
    PICK = "pickedUp"
    TRAN = "inTransit"
    DONE = "delivered"


# !---------------------------------------------------------
#
class Products(str, Enum):
    """Representation of valid products in the system.

    :ivar lasagna: Food product.
    :ivar cheese_burger: Food product.
    :ivar veil: Food product.
    :ivar vego_salad: Food product.
    """

    lasagna = "Lasagna"
    cheese_burger = "Double Cheeseburger"
    veil = "Veil with glazed onions and blue cheese"
    vego_salad = "Vegetarian Salad with healthy produce"


class OrderItem(BaseModel):
    """Required order item parameters.


    :ivar product: Ordered product.
    :ivar quantity: Product quantity.
    """

    product: Products
    quantity: PositiveInt = 1


class OrderItems(BaseModel):
    """A list of the ordered items.


    :ivar items: List of ordered items.
    """

    items: conlist(OrderItem, min_length=1)  # type: ignore


# !------------------------------------------------------------------------
#
class MongoBase(BaseModel):
    """
    Class that handles conversions between MongoDB '_id' key
    and our own 'id' key.

    MongoDB uses ``_id`` as an internal default index key.
    We can use that to our advantage.

    :ivar model_config: MongoBase config items.
    """

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    @classmethod
    def from_mongo(cls, data: dict) -> Callable:
        """Convert "_id" (str object) into "id" (UUID object).

        :param data: Current BaseModel object.
        """

        if not data:
            return data

        mongo_id = data.pop("_id", None)
        return cls(**dict(data, id=mongo_id))

    def to_mongo(self, **kwargs: dict) -> dict:
        """Convert "id" (UUID object) into "_id" (str object).
        :param kwargs: Current BaseModel object parameters.
        """
        parsed = self.model_dump(**kwargs)

        if "_id" not in parsed and "id" in parsed:
            parsed["_id"] = str(parsed.pop("id"))

        return parsed
