import logging

from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.log_in import LogInPage

LOGGER = logging.getLogger(__name__)


class TestUILogIn:
    def test_can_log_in(self, log_in_page: LogInPage, user_registered: dict) -> None:
        log_in_page.open_page()
        log_in_page.enter_email(user_registered["email"])
        log_in_page.enter_password(user_registered["password"])
        log_in_page.click_log_in()
        log_in_page.verify_logged_in()

    def test_log_in_non_existent_user(self, log_in_page: LogInPage) -> None:
        log_in_page.open_page()
        log_in_page.enter_email("john.green@mail.com")
        log_in_page.enter_password("1234567890")
        log_in_page.click_log_in()
        log_in_page.verify_log_in_failed()

    def test_button_sign_up_is_working(self, log_in_page: LogInPage) -> None:
        log_in_page.open_page()
        log_in_page.click_sign_up()
        log_in_page.verify_sign_up_button_works()
