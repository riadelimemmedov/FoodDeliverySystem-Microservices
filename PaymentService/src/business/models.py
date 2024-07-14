# Third party modules
from pydantic import BaseModel, Field

# Local modules
from ..repository.models import Status, MetadataSchema


# !---------------------------------------------------------
#
class PaymentResponse(BaseModel):
    """Representation of a Payment Response in the system.

    :ivar metadata: Order metadata in the system.
    :ivar status: Payment state.
    """

    metadata: MetadataSchema
    status: Status = Field(send_example=Status.PAID)
