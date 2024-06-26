# BUILTIN modules
import contextlib
from uuid import UUID

# Third party modules
from loguru import logger
from uuid_extensions import uuid7
from fastapi import HTTPException
from httpx import AsyncClient, ConnectError, ConnectTimeout

# Local modules
from .models import PaymentResponse
from ..broker.interface import IBroker
from ..repository.models import PaymentModel
from ..core.setup import config, SSL_CONTEXT
from ..tools.url_cache import UrlServiceCache
from ..repository.interface import IRepository
from ..web.api.models import BillingCallback, BillingPayload, PaymentPayload

# Third party services
from ..services.stripe_service import stripe_service

# Constants
HDR_DATA = {"Content-Type": "application/json"}
""" header data used for httpx requests. """
PAYMENTS_CALLBACK_URL = "http://fictitious.com/v1/payments/callback"
""" Payment callback URL. """
