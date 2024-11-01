import logging

import pytest
import requests

from util.admin.bearer_auth import BearerAuth

LOGGER = logging.getLogger(__name__)


class TestAPIUser:
    endpoint = "https://thinking-tester-contact-list.herokuapp.com/users/"
    myself = "me"
    login = "login"
    logout = "logout"

    def check_user_json_schema(self, user: dict) -> None:
        assert "_id" in user
        assert "firstName" in user
        assert "lastName" in user
        assert "email" in user
        assert "__v" in user

    def check_user_equals(self, user: dict, another: dict) -> None:
        assert user["firstName"] == another["firstName"]
        assert user["lastName"] == another["lastName"]
        assert user["email"] == another["email"]


    def test_create_user_valid(self, admin, user_raw_data) -> None:
        response = requests.post(TestAPIUser.endpoint, json = user_raw_data)

        assert response.status_code == 201
        assert "application/json" in response.headers["Content-Type"]

        data = response.json()
        assert "user" in data
        self.check_user_json_schema(data["user"])
        self.check_user_equals(user_raw_data, data["user"])
        assert "token" in data

        # Cleanup
        admin.delete_user(data["token"])


    def test_create_user_invalid(self, user_raw_data_invalid):
        response = requests.post(TestAPIUser.endpoint, json = user_raw_data_invalid)

        assert response.status_code == 400

    def test_get_user_myself(self, user_registered: dict, token: str):
        response = requests.get(TestAPIUser.endpoint + TestAPIUser.myself, auth = BearerAuth(token))

        assert response.status_code == 200
        assert "application/json" in response.headers["Content-Type"]

        data = response.json()
        self.check_user_json_schema(data)
        self.check_user_equals(user_registered, data)

    def test_get_user_myself_without_auth(self, user_registered: dict):
        response = requests.get(TestAPIUser.endpoint + TestAPIUser.myself)

        assert response.status_code == 401

    # def test_update_user(self):
    #     pass

    # def test_delete_user(self):
    #     return
