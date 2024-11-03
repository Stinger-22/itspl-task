from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

from src.pages.base_page import BasePage


class LogInPage(BasePage):
    def __init__(self, driver: WebDriver):
        url = "https://thinking-tester-contact-list.herokuapp.com/login"
        super().__init__(driver, url)

    def enter_email(self, email: str):
        self.driver.find_element(By.ID, "email").send_keys(email)

    def enter_password(self, password: str):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_log_in(self):
        self.driver.find_element(By.ID, "submit").click()

    def verify_logged_in(self):
        self.verify_browser_url_changed("https://thinking-tester-contact-list.herokuapp.com/contactList")
        try:
            logout_button = self.driver.find_element(By.ID, "logout")
            self.verify_element_is_displayed(logout_button)
        except NoSuchElementException as exception:
            raise AssertionError("Log out button does not exist") from exception

    def verify_log_in_failed(self):
        try:
            error_element = self.driver.find_element(By.ID, "error")
            self.verify_element_is_displayed(error_element)
        except NoSuchElementException as exception:
            raise AssertionError("Error message not found") from exception

    def click_sign_up(self):
        self.driver.find_element(By.ID, "signup").click()

    def verify_sign_up_button_works(self):
        self.verify_browser_url_changed("https://thinking-tester-contact-list.herokuapp.com/addUser")
