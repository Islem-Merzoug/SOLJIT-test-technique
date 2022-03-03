"""http entrypoint file."""

import json
from typing import Any, Dict

import requests
from fastapi import Body, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from requests.structures import CaseInsensitiveDict

from services.schemas import PydanticClientConnectionData
from services.utils import search_condidature

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/connect")
def connect(clientConnectionData: PydanticClientConnectionData) -> Any:
    """Connect with Salesforce."""
    URL = "https://login.salesforce.com/services/oauth2/token"
    DATA = clientConnectionData.dict()
    response = requests.post(url=URL, data=DATA)

    return response.json()


@app.get("/candidature")
def get_one_candidature(data: Dict[str, str] = Body(...)) -> Any:
    """Return all the candidatures from Salesforce."""
    id = data["id"]
    query = (
        f"SELECT First_Name__c,Last_Name__c,Year__c,Year_Of_Experience__c"
        f" FROM Candidature__c WHERE ID = '{id}' "
    )
    base_url = data["base_url"]
    token = data["token"]

    URL = f"{base_url}/services/data/v42.0/query/?q={query}"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    resp = requests.get(url=URL, headers=headers)

    return resp.json()


@app.post("/candidature")
def get_all_candidature(data: Dict[str, str] = Body(...)) -> Any:
    """Return all the candidatures from Salesforce."""
    query = "SELECT First_Name__c,Last_Name__c,Year__c,Year_Of_Experience__c FROM Candidature__c"
    base_url = data["base_url"]
    token = data["token"]

    URL = f"{base_url}/services/data/v42.0/query/?q={query}"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    resp = requests.get(url=URL, headers=headers)

    return resp.json()


@app.post("/create_candidatures")
def get_create_candidature(data: Dict[str, Any] = Body(...)) -> Any:
    """Create candidatures from Salesforce."""
    field = data["field"]
    base_url = data["base_url"]
    token = data["token"]
    body = data["body"]
    URL = f"{base_url}/services/data/v42.0/sobjects/{field}/"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    resp = requests.post(url=URL, data=json.dumps(body), headers=headers)

    return resp.json()


@app.patch("/update_candidatures")
def update_create_candidature(data: Dict[str, Any] = Body(...)) -> Any:
    """Update candidatures from Salesforce."""
    field = data["field"]
    base_url = data["base_url"]
    token = data["token"]
    body = data["body"]
    id = data["id"]
    URL = f"{base_url}/services/data/v42.0/sobjects/{field}/{id}"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    requests.patch(url=URL, data=json.dumps(body), headers=headers)

    raise HTTPException(detail=f"Record {id} has been updated successfully!", status_code=204)


@app.post("/search_candidatures")
def search_candidatures(data: Dict[str, Any] = Body(...)) -> Any:
    """Return searched candidatures from Salesforce."""
    search = data["search"]
    token = data["token"]

    resp = search_condidature(search, token)
    return resp
