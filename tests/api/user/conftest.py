import pytest

from tests.api.test_cases_user import (
    USERS_REGISTRATION,
    USERS_REGISTRATION_INVALID,
    USERS_UPDATED,
    USERS_UPDATED_INVALID,
)


def user_payload_id(entry):
    return entry[1]

def user_payload_expected_id(entry):
    return entry[2]

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
