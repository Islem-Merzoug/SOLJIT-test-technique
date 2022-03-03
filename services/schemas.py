"""Schemas."""

from pydantic import BaseModel


class PydanticClientConnectionData(BaseModel):
    """Pydantic Client Connection Data class."""

    username: str
    password: str
    grant_type: str
    client_id: str
    client_secret: str
