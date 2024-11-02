import logging

import pytest
import requests

LOGGER = logging.getLogger(__name__)


class TestAPIContact:
    endpoint = "https://thinking-tester-contact-list.herokuapp.com/contacts/"

    schema = (
        "_id",
        "firstName",
        "lastName",
        "birthdate",
        "email",
        "phone",
        "street1",
        "street2",
        "city",
        "stateProvince",
        "postalCode",
        "country",
        "owner",
        "__v",
    )

    def check_contact_json_schema(self, contact: dict) -> None:
        for field in TestAPIContact.schema:
            assert field in contact

    def check_contact_equals(self, contact: dict, another: dict) -> None:
        for field in TestAPIContact.schema:
            assert contact[field] == another[field]


    @pytest.mark.xfail("Not implemented")
    def test_create_contact(self):
        pass

    @pytest.mark.xfail("Not implemented")
    def test_create_contact_invalid(self):
        pass

    @pytest.mark.xfail("Not implemented")
    def test_get_contact(self):
        pass

    @pytest.mark.xfail("Not implemented")
    def test_get_contact_without_auth(self):
        pass

    @pytest.mark.xfail("Not implemented")
    def test_get_contact_list(self):
        pass

    @pytest.mark.xfail("Not implemented")
    def test_get_contact_list_without_auth(self):
        pass

    @pytest.mark.xfail("Not implemented")
    def test_update_contact(self):
        pass

    @pytest.mark.xfail("Not implemented")
    def test_update_contact_invalid(self):
        pass

    @pytest.mark.xfail("Not implemented")
    def test_patch_contact(self):
        pass

    @pytest.mark.xfail("Not implemented")
    def test_patch_contact_invalid(self):
        pass

    @pytest.mark.xfail("Not implemented")
    def test_delete_contact(self):
        pass

    @pytest.mark.xfail("Not implemented")
    def test_delete_contactwithout_auth(self):
        pass

    @pytest.mark.xfail("Not implemented")
    def test_delete_contact_list(self):
        pass
