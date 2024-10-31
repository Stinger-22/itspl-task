import logging

import pytest

from util.admin.admin_api import AdminAPI

LOGGER = logging.getLogger(__name__)

USER = {
    "firstName": "John",
    "lastName": "Green",
    "email": "john.green@mail.com",
    "password": "1234567",
}


@pytest.fixture
def admin():
    return AdminAPI()


@pytest.fixture
def user_data(admin: AdminAPI):
    yield USER
    token = admin.login(USER["email"], USER["password"])
    admin.delete_user(token)


@pytest.fixture
def user_registered(admin: AdminAPI):
    token = admin.create_user(USER)
    yield USER
    admin.delete_user(token)
