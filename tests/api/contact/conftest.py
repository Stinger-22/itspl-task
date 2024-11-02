import pytest

from tests.api.contact.test_cases_contact import (
    CONTACTS,
)
from tests.util.test_case_parse import get_test_case_id_payload_id


@pytest.fixture
def contact_default() -> dict:
    return CONTACTS[0][0]

@pytest.fixture(params = CONTACTS, ids = get_test_case_id_payload_id)
def contact_raw_data(request) -> dict:
    return request.param[0]

