import logging

import pytest
import requests

from util.admin.admin_api import AdminAPI, BearerAuth

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
        LOGGER.info("Contact JSON schema is correct")

    def check_contact_equals(self, contact: dict, another: dict) -> None:
        for i in range (1, len(TestAPIContact.schema) - 2):
            field = TestAPIContact.schema[i]
            assert contact[field] == another[field]


    def test_create_contact(self, admin: AdminAPI, token: str, contact_raw_data: dict) -> None:
        response = requests.post(TestAPIContact.endpoint, auth = BearerAuth(token), json = contact_raw_data)
        assert response.status_code == 201
        assert "application/json" in response.headers["Content-Type"]
        LOGGER.info("Response status code and headers are correct")

        data = response.json()
        owner = admin.get_user(token)
        assert owner["_id"] == data["owner"]
        LOGGER.info("Owner of contact is correct")
        self.check_contact_json_schema(data)
        self.check_contact_equals(contact_raw_data, data)
        LOGGER.info("Created contact response JSON is correct")

        created_contact = admin.get_contact(token, data["_id"])
        self.check_contact_json_schema(created_contact)
        self.check_contact_equals(contact_raw_data, created_contact)
        LOGGER.info("Successfully received the same contact")

        # Cleanup
        admin.delete_contact(token, data["_id"])

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
