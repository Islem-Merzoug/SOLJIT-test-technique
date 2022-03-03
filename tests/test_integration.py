"""integration tests file."""

import json

from fastapi.testclient import TestClient

from services.main import app
from services.utils import search_condidature

client = TestClient(app)


class TestEntrypointServices:
    def test_connect(self):
        """Test connect to salesforce."""
        response = client.post(
            "/connect",
            data=json.dumps(
                {
                    "username": "soljit_algeria2@soljit.com",
                    "password": "entretient_1235zoLmTaUDLiouUaOAN6WhOQPi",
                    "grant_type": "password",
                    "client_id": "3MVG9I9urWjeUW051PumYX1mbS5HkS3kpZsbCE"
                    "zYWjgivRyDno1MjvM08EfVf2be52s0vrthHamsgMpQCrm5Z",
                    "client_secret": "EC97DAFBF9F6F2399DE5E7BADA2E9BBE"
                    "F6B3B6E832DC435668AA452940AD9501",
                }
            ),
        )

        assert response.status_code == 200
        json_response = response.json()
        assert all(
            element in json_response
            for element in ["access_token", "instance_url", "id", "token_type", "signature"]
        )

    def test_get_one_candidature(self):
        """Test get one candidature."""
        token = "00D4L000000gmbH!AQsAQPPIIjH_fUVMez58h1hD9L_lvCXy5zvA2Iw.8e70TYS0ioVZl01rzvCPbCDU_ewh24x84SvZ9SaasRzY9nl2u_B5L9fV"
        base_url = "https://soljit35-dev-ed.my.salesforce.com/"

        response = client.get(
            "/candidature",
            data=json.dumps({"id": "a004L000002gCJK", "base_url": base_url, "token": token}),
        )

        assert response.status_code == 200

        assert len(response.json()["records"]) == 1
        assert response.json()["records"][0]["First_Name__c"] == "mohamed"

    def test_get_all_candidature(self):
        """Test get all candidatures."""
        token = "00D4L000000gmbH!AQsAQPPIIjH_fUVMez58h1hD9L_lvCXy5zvA2Iw.8e70TYS0ioVZl01rzvCPbCDU_ewh24x84SvZ9SaasRzY9nl2u_B5L9fV"
        base_url = "https://soljit35-dev-ed.my.salesforce.com/"

        response = client.post(
            "/candidature",
            data=json.dumps({"base_url": base_url, "token": token}),
        )
        assert response.status_code == 200
        assert len(response.json()["records"]) > 1

    def test_insert_candidature(self):
        """Test insert candidature."""
        token = "00D4L000000gmbH!AQsAQPPIIjH_fUVMez58h1hD9L_lvCXy5zvA2Iw.8e70TYS0ioVZl01rzvCPbCDU_ewh24x84SvZ9SaasRzY9nl2u_B5L9fV"
        base_url = "https://soljit35-dev-ed.my.salesforce.com/"
        field = "Candidature__c"
        body = {
            "First_Name__c": "Islem",
            "Last_Name__c": "Merzoug",
            "Year_Of_Experience__c": 2,
        }

        response = client.post(
            "/create_candidatures",
            data=json.dumps({"field": field, "base_url": base_url, "token": token, "body": body}),
        )

        assert response.status_code == 200
        assert response.json()["success"] is True

    def test_update_candidature(self):
        """Test update candidature."""
        token = "00D4L000000gmbH!AQsAQPPIIjH_fUVMez58h1hD9L_lvCXy5zvA2Iw.8e70TYS0ioVZl01rzvCPbCDU_ewh24x84SvZ9SaasRzY9nl2u_B5L9fV"
        base_url = "https://soljit35-dev-ed.my.salesforce.com/"
        field = "Candidature__c"
        id = "a004L000002gCJK"
        body = {"Last_Name__c": "Merzouuuuug"}

        response = client.patch(
            "/update_candidatures",
            data=json.dumps(
                {"field": field, "id": id, "base_url": base_url, "token": token, "body": body}
            ),
        )

        assert response.status_code == 204
        assert response.json()["detail"] == f"Record {id} has been updated successfully!"

    def test_search_condidature_function(self):
        """Test search condidature function from utils."""
        token = "00D4L000000gmbH!AQsAQPPIIjH_fUVMez58h1hD9L_lvCXy5zvA2Iw.8e70TYS0ioVZl01rzvCPbCDU_ewh24x84SvZ9SaasRzY9nl2u_B5L9fV"
        name = "Charaf"
        resp = search_condidature(name, token)
        assert resp["done"] is True

    def test_search_condidature(self):
        """Test search condidature."""
        token = "00D4L000000gmbH!AQsAQPPIIjH_fUVMez58h1hD9L_lvCXy5zvA2Iw.8e70TYS0ioVZl01rzvCPbCDU_ewh24x84SvZ9SaasRzY9nl2u_B5L9fV"
        response = client.post(
            "/search_candidatures",
            data=json.dumps({"search": "Charaf", "token": token}),
        )
        assert response.status_code == 200
        assert len(response.json()["records"]) > 1
