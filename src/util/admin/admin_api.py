import logging

import requests

from util.admin.bearer_auth import BearerAuth

LOGGER = logging.getLogger(__name__)


class AdminAPI:
    """Wrapper for safe use of Contact List Application API.

    Attributes:
        url (str):       Contact List Application base url.

    """

    url = "https://thinking-tester-contact-list.herokuapp.com/"


    def create_user(self, user: dict) -> requests.Response:
        LOGGER.info("Creating user: %s", user)
        response = requests.post(AdminAPI.url + "users", json = user)
        if response.status_code == 201:
            return response.json()["token"]
        exception_msg = f"Couldn't create user:\n{response.text}"
        raise Exception(exception_msg)

    def log_in(self, email: str, password: str) -> str:
        LOGGER.info("Logging in user with credentials: %s, %s", email, password)
        login_data = {
            "email": email,
            "password": password,
        }
        response = requests.post(AdminAPI.url + "users/login", json = login_data)
        if response.status_code == 200:
            return response.json()["token"]
        exception_msg = f"Couldn't log in with the given credential: (email: {email}, password: {password})\n{response.text}"
        raise Exception(exception_msg)

    def get_user(self, token: str) -> requests.Response:
        LOGGER.info("Getting user with token: %s", token)
        return requests.get(AdminAPI.url + "users/me", auth = BearerAuth(token))

    def delete_user(self, token: str) -> requests.Response:
        LOGGER.info("Deleting user with token: %s", token)
        if token is not None:
            return requests.delete(AdminAPI.url + "users/me", auth = BearerAuth(token))
        exception_msg = "Received token is None"
        raise TypeError(exception_msg)
