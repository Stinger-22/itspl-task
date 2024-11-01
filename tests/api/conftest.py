import logging

import pytest

from tests.api.test_cases import USER, USER_UPDATED, USERS_INVALID
from util.admin.admin_api import AdminAPI

LOGGER = logging.getLogger(__name__)


def user_invalid_test_case_id(user_invalid):
    return user_invalid[1]

@pytest.fixture(autouse = True, scope = "session")
def admin():
    LOGGER.info("Creating AdminAPI")
    return AdminAPI()

@pytest.fixture
def user_raw_data() -> dict:
    return USER

@pytest.fixture(params = USERS_INVALID, ids = user_invalid_test_case_id)
def user_raw_data_invalid(request) -> dict:
    return request.param[0]

@pytest.fixture
def user_registered(admin: AdminAPI):
    token = admin.create_user(USER)
    yield USER
    admin.delete_user(token)

@pytest.fixture
def token(admin: AdminAPI, user_registered: dict) -> str:
    return admin.log_in(user_registered["email"], user_registered["password"])

# TODO write extensive cleanup fixture for module
