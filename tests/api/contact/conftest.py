import logging

import pytest

from tests.api.contact.test_cases_contact import (
    CONTACTS,
    CONTACTS_INVALID,
)
from tests.util.test_case_parse import get_test_case_id_payload_id
from util.admin.admin_api import AdminAPI

LOGGER = logging.getLogger(__name__)


@pytest.fixture
def contact_default() -> dict:
    return CONTACTS[0][0]

@pytest.fixture
def contact_list_default() -> dict:
    contact_list = []
    contact_list.append(CONTACTS[0][0])
    contact_list.append(CONTACTS[1][0])
    contact_list.append(CONTACTS[2][0])
    return contact_list

@pytest.fixture(params = CONTACTS, ids = get_test_case_id_payload_id)
def contact_raw_data(request) -> dict:
    return request.param[0]

@pytest.fixture(params = CONTACTS_INVALID, ids = get_test_case_id_payload_id)
def contact_raw_data_invalid(request) -> dict:
    return request.param[0]

@pytest.fixture
def contact_created(admin: AdminAPI, token: str, contact_default: dict):
    contact_default_created = admin.create_contact(token, contact_default)
    LOGGER.info("Created default contact")
    yield contact_default_created
    admin.delete_contact(token, contact_default_created["_id"])
    LOGGER.info("Deleted default contact")

@pytest.fixture
def contact_list_created(admin: AdminAPI, token: str, contact_list_default: list):
    contact_list_default_created = []
    for contact in contact_list_default:
        contact_list_default_created.append(admin.create_contact(token, contact))
    LOGGER.info("Created default contact list")
    yield contact_list_default_created
    admin.delete_contact_list(token)
    LOGGER.info("Deleted default contact list")
