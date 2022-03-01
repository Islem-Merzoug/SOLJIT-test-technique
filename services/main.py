"""http entrypoint file."""

from typing import Any, Dict, Optional

import requests
from fastapi import Body, FastAPI
from requests.structures import CaseInsensitiveDict

from services.schemas import PydanticClientConnectionData

app = FastAPI()


@app.get("/")
def read_root() -> Dict[str, str]:
    """Read root function."""
    r = requests.get("https://api.github.com/users")
    return r.json()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None) -> Dict[str, Any]:
    """Read item function."""
    return {"item_id": item_id, "q": q}


@app.post("/connect")
def connect(clientConnectionData: PydanticClientConnectionData) -> Any:
    """Read item function."""
    URL = "https://login.salesforce.com/services/oauth2/token"
    DATA = clientConnectionData.dict()
    response = requests.post(url=URL, data=DATA)

    return response.json()


@app.post("/accounts")
def get_accounts(data: Dict[str, str] = Body(...)) -> Any:
    """Return all the accounts from Salesforce."""
    query = data["query"]
    base_url = data["base_url"]
    token = data["token"]

    URL = f"{base_url}/services/data/v42.0/query/?q={query}"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    resp = requests.get(url=URL, headers=headers)

    return resp.json()
