import logging

from tests.ui.pages.log_in import LogInPage

LOGGER = logging.getLogger(__name__)


class TestUILogIn:
    def test_can_log_in(self, log_in_page: LogInPage, user_registered: dict) -> None:
        log_in_page.open_page()
        log_in_page.enter_email(user_registered["email"])
        log_in_page.enter_password(user_registered["password"])
        log_in_page.click_log_in()
        log_in_page.verify_logged_in()

    def test_log_in_non_existent_user(self, log_in_page: LogInPage, user_default: dict) -> None:
        log_in_page.open_page()
        log_in_page.enter_email(user_default["email"])
        log_in_page.enter_password(user_default["password"])
        log_in_page.click_log_in()
        log_in_page.verify_log_in_failed()

    def test_button_sign_up_is_working(self, log_in_page: LogInPage) -> None:
        log_in_page.open_page()
        log_in_page.click_sign_up()
        log_in_page.verify_sign_up_button_works()
