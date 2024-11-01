import contextlib
import logging

import pytest

from tests.api.test_cases_user import USERS_REGISTRATION, USERS_REGISTRATION_INVALID, USERS_UPDATED, USERS_UPDATED_INVALID
from util.admin.admin_api import AdminAPI, AdminAPIException

LOGGER = logging.getLogger(__name__)


@pytest.fixture(autouse = True, scope = "session")
def admin():
    LOGGER.info("Creating AdminAPI")
    return AdminAPI()

@pytest.fixture(autouse = True)
def cleanup(admin: AdminAPI):
    LOGGER.info("Performing cleanup in case valid user from test cases exists")
    with contextlib.suppress(AdminAPIException):
        for user in USERS_REGISTRATION:
            token = admin.log_in(user[0]["email"], user[0]["password"])
            admin.delete_user(token)


def user_payload_id(entry):
    return entry[1]

def user_payload_expected_id(entry):
    return entry[2]


@pytest.fixture
def user_default() -> dict:
    return USERS_REGISTRATION[0][0]

@pytest.fixture(params = USERS_REGISTRATION, ids = user_payload_id)
def user_raw_data(request) -> dict:
    return request.param[0]

@pytest.fixture(params = USERS_REGISTRATION_INVALID, ids = user_payload_id)
def user_raw_data_invalid(request) -> dict:
    return request.param[0]

@pytest.fixture(params = USERS_UPDATED, ids = user_payload_expected_id)
def user_updated_raw_data(request) -> dict:
    return (request.param[0], request.param[1])

@pytest.fixture(params = USERS_UPDATED_INVALID, ids = user_payload_id)
def user_updated_raw_data_invalid(request) -> dict:
    return request.param[0]

@pytest.fixture
def user_registered(admin: AdminAPI, user_default):
    token = admin.create_user(user_default)
    yield user_default
    admin.delete_user(token)

@pytest.fixture
def token(admin: AdminAPI, user_registered: dict) -> str:
    return admin.log_in(user_registered["email"], user_registered["password"])
