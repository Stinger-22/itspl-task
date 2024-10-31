import logging

import requests

from util.admin.bearer_auth import BearerAuth

LOGGER = logging.getLogger(__name__)


class AdminAPI:
    url = "https://thinking-tester-contact-list.herokuapp.com/"

    def create_user(self, user: dict) -> str:
        response = requests.post(AdminAPI.url + "users", json = user)
        return response.json()["token"]

    def login(self, email: str, password: str) -> str:
        login_data = {
            "email": email,
            "password": password,
        }
        response = requests.post(AdminAPI.url + "users/login", json = login_data)
        return response.json()["token"]

    def delete_user(self, token: str):
        requests.delete(AdminAPI.url + "users/me", auth = BearerAuth(token))
