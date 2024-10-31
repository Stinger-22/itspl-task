import logging

import pytest
import requests

LOGGER = logging.getLogger(__name__)

class TestAPIUser:
    endpoint = "https://thinking-tester-contact-list.herokuapp.com/users/"
    user = "me"
    login = "login"
    logout = "logout"


    @pytest.fixture(autouse = True)
    def token(self, request: pytest.FixtureRequest):
        if "no_token_required" in request.keywords:
            return None
        token = ""
        return token


    @pytest.mark.no_token_required
    def test_create_user(self, user_data):
        response = requests.post(TestAPIUser.endpoint, json=user_data)

        assert response.status_code == 201
        assert "application/json" in response.headers["Content-Type"]

        data = response.json()
        assert "user" in data
        assert "_id" in data["user"]
        assert "firstName" in data["user"]
        assert "lastName" in data["user"]
        assert "email" in data["user"]
        assert "__v" in data["user"]
        assert "token" in data

        assert user_data["firstName"] == data["user"]["firstName"]
        assert user_data["lastName"] == data["user"]["lastName"]
        assert user_data["email"] == data["user"]["email"]


    # def test_read_user(self):
    #     return

    # def test_update_user(self):
    #     return

    # def test_delete_user(self):
    #     return
