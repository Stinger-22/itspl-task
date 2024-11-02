import logging

import pytest
import requests

from util.admin.admin_api import AdminAPI, AdminAPIException, BearerAuth

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
        for key in contact:
            assert contact[key] == another[key]


    def test_create_contact(self, admin: AdminAPI, token: str, contact_raw_data: dict) -> None:
        LOGGER.debug("Creating contact: %s", contact_raw_data)
        response = requests.post(TestAPIContact.endpoint, auth = BearerAuth(token), json = contact_raw_data)
        LOGGER.debug("Received response text: %s", response.text)
        assert response.status_code == 201
        assert "application/json" in response.headers["Content-Type"]
        LOGGER.info("Response status code and headers are correct")

        data = response.json()
        owner = admin.get_user(token)
        assert owner["_id"] == data["owner"]
        LOGGER.info("Owner of contact is correct")
        self.check_contact_equals(contact_raw_data, data)
        LOGGER.info("Created contact response JSON is correct")

        created_contact = admin.get_contact(token, data["_id"])
        self.check_contact_equals(contact_raw_data, created_contact)
        LOGGER.info("Successfully received the same contact")

        # Cleanup
        admin.delete_contact(token, data["_id"])

    def test_create_contact_invalid(self, admin: AdminAPI, token: str, contact_raw_data_invalid: dict) -> None:
        LOGGER.debug("Creating invalid contact: %s", contact_raw_data_invalid)
        response = requests.post(TestAPIContact.endpoint, auth = BearerAuth(token), json = contact_raw_data_invalid)
        LOGGER.debug("Received response text: %s", response.text)
        try:
            assert response.status_code == 400
            LOGGER.info("Invalid contact was not created")
        except AssertionError as error:
            # Cleanup
            admin.delete_contact(token, response.json()["_id"])
            exception_msg = "Invalid contact was created"
            raise AssertionError(exception_msg) from error

    def test_get_contact(self, token: str, contact_created: dict):
        LOGGER.debug("Getting contact: %s", contact_created)
        response = requests.get(TestAPIContact.endpoint + contact_created["_id"], auth = BearerAuth(token))
        LOGGER.debug("Received response text: %s", response.text)
        assert response.status_code == 200
        assert "application/json" in response.headers["Content-Type"]
        LOGGER.info("Response status code and headers are correct")

        received_contact = response.json()
        self.check_contact_equals(contact_created, received_contact)
        LOGGER.info("Successfully received contact")

    def test_get_contact_without_auth(self, contact_created: dict):
        LOGGER.debug("Getting contact: %s", contact_created)
        response = requests.get(TestAPIContact.endpoint + contact_created["_id"])
        LOGGER.debug("Received response text: %s", response.text)
        assert response.status_code == 401
        LOGGER.info("Can't get contact without authorization as it is intended")

    @pytest.mark.xfail(reason = "Not implemented")
    def test_get_contact_list(self):
        pass

    @pytest.mark.xfail(reason = "Not implemented")
    def test_get_contact_list_without_auth(self):
        pass

    @pytest.mark.xfail(reason = "Not implemented")
    def test_update_contact(self):
        pass

    @pytest.mark.xfail(reason = "Not implemented")
    def test_update_contact_invalid(self):
        pass

    @pytest.mark.xfail(reason = "Not implemented")
    def test_patch_contact(self):
        pass

    @pytest.mark.xfail(reason = "Not implemented")
    def test_patch_contact_invalid(self):
        pass

    def test_delete_contact(self, admin: AdminAPI, token: str, contact_default: dict):
        # Setup
        contact = admin.create_contact(token, contact_default)

        LOGGER.debug("Deleting contact: %s", contact)
        response = requests.delete(TestAPIContact.endpoint + contact["_id"], auth = BearerAuth(token))
        LOGGER.debug("Received response text: %s", response.text)
        assert response.status_code == 200
        LOGGER.info("Response status code is correct")

        with pytest.raises(AdminAPIException):
            admin.get_contact(token, contact["_id"])
        LOGGER.info("Can't get contact that was deleted")

    def test_delete_contact_without_auth(self, contact_created: dict):
        LOGGER.debug("Deleting contact: %s", contact_created)
        response = requests.delete(TestAPIContact.endpoint + contact_created["_id"])
        LOGGER.debug("Received response text: %s", response.text)
        assert response.status_code == 401
        LOGGER.info("Can't delete contact without authorization as it is intended")

    @pytest.mark.xfail(reason = "Not implemented")
    def test_delete_contact_list(self):
        pass
