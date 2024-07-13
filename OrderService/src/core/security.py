# Third party modules
from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

# local modules
from ..core.setup import config

# Constants
API_KEY_HEADER = APIKeyHeader(name="X-API-Key")
""" Using API key authentication. """

# ---------------------------------------------------------
#


def validate_authentication(api_key: str = Security(API_KEY_HEADER)):
    """Validate the authentication of the user.
    :param api_key: Authentication credentials.
    :raise HTTPException(401): When an incorrect API key is supplied.
    """
    if api_key != config.service_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
            headers={"WWW-Authenticate": "X-API-Key"},
        )
