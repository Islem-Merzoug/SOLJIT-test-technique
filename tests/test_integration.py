"""integration tests file."""

import json

from fastapi.testclient import TestClient

from services.main import app

client = TestClient(app)


class TestEntrypointServices:
    def test_read_main(self):
        """Test Read root function."""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json()[0] == {
            "avatar_url": "https://avatars.githubusercontent.com/u/1?v=4",
            "events_url": "https://api.github.com/users/mojombo/events{/privacy}",
            "followers_url": "https://api.github.com/users/mojombo/followers",
            "following_url": "https://api.github.com/users/mojombo/following{/other_user}",
            "gists_url": "https://api.github.com/users/mojombo/gists{/gist_id}",
            "gravatar_id": "",
            "html_url": "https://github.com/mojombo",
            "id": 1,
            "login": "mojombo",
            "node_id": "MDQ6VXNlcjE=",
            "organizations_url": "https://api.github.com/users/mojombo/orgs",
            "received_events_url": "https://api.github.com/users/mojombo/received_events",
            "repos_url": "https://api.github.com/users/mojombo/repos",
            "site_admin": False,
            "starred_url": "https://api.github.com/users/mojombo/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/mojombo/subscriptions",
            "type": "User",
            "url": "https://api.github.com/users/mojombo",
        }

    def test_connect(self):
        """Test Read root function."""
        response = client.post(
            "/connect",
            data=json.dumps(
                {
                    "username": "i.merzoug16@gmail.com",
                    "password": "*salesforce@account21#6M8WPBFmwpESPW106ZTDmxte",
                    "grant_type": "password",
                    "client_id": "3MVG9riCAn8HHkYVg9Z3a8MScGrJLMwS.gKym0h8eb"
                    "NPYYc1DJpQEvFEAkwxpFESAioDrdUl0H54Kc9mKSaZY",
                    "client_secret": "C731FD4B055E3D83BA681B859FF86F"
                    "2A123061C02554F7FB476276E945C6DA41",
                }
            ),
        )

        assert response.status_code == 200
        json_response = response.json()
        assert all(
            element in json_response
            for element in ["access_token", "instance_url", "id", "token_type", "signature"]
        )

    def test_get_accounts(self):
        """Test Read root function."""
        response = client.post(
            "/accounts",
            data=json.dumps(
                {
                    "query": "SELECT+Name,Type+FROM+Account",
                    "base_url": "https://testcompany-52a-dev-ed.my.salesforce.com",
                    "token": "00D8c000005IV6C!ARwAQBz6pq2bAdVUvEKETdCmVUmwXJWyS"
                    "qP5yHvB.IDt90rFyLGlXnxtzScZF.fN2dpUf0D83FOvzeyGubyjmvagMxJThfmo",
                }
            ),
        )

        assert response.status_code == 200
        # keys = []
        # for key in response.json()[0].keys():
        #     keys.append(key)
        # assert keys != ['message', 'errorCode']
        assert len(response.json()["records"]) == 14
