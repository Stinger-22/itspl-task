import logging

from tests.ui.pages.sign_up import SignUpPage
from src.util.admin.admin_api import AdminAPI

LOGGER = logging.getLogger(__name__)


class TestUISignUp:
    def enter_sign_up_data(self, sign_up_page: SignUpPage, user: dict):
        sign_up_page.enter_first_name(user["firstName"])
        sign_up_page.enter_last_name(user["lastName"])
        sign_up_page.enter_email(user["email"])
        sign_up_page.enter_password(user["password"])

    def test_can_sign_up(self, admin: AdminAPI, sign_up_page: SignUpPage, user_default: dict) -> None:
        sign_up_page.open_page()
        self.enter_sign_up_data(sign_up_page, user_default)
        sign_up_page.click_sign_up()
        sign_up_page.verify_signed_up()

        # Cleanup
        token = admin.log_in(user_default["email"], user_default["password"])
        admin.delete_user(token)

    def test_sign_up_used_mail(self, sign_up_page: SignUpPage, user_registered: dict) -> None:
        sign_up_page.open_page()
        self.enter_sign_up_data(sign_up_page, user_registered)
        sign_up_page.click_sign_up()
        sign_up_page.verify_sign_up_failed()

    def test_button_sign_up_is_working(self, sign_up_page: SignUpPage) -> None:
        sign_up_page.open_page()
        sign_up_page.click_cancel()
        sign_up_page.verify_cancel_button_works()
