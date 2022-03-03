"""Utils functions."""
from typing import Any

import requests
from requests.structures import CaseInsensitiveDict


def search_condidature(search: str, token: str) -> Any:
    """Search condidature with filter handled."""
    query = ""

    if search:
        query = (
            "SELECT First_Name__c,Last_Name__c,Year__c,Year_Of_Experience__c FROM Candidature__c "
            f"WHERE First_Name__c = '{search}' "
            f"OR "
            f"Last_Name__c = '{search}'"
        )

    base_url = "https://soljit35-dev-ed.my.salesforce.com/"
    URL = f"{base_url}/services/data/v42.0/query/?q={query}"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    resp = requests.get(url=URL, headers=headers)

    return resp.json()
