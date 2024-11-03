from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

from tests.ui.pages.base_page import BasePage


class SignUpPage(BasePage):
    def __init__(self, driver: WebDriver):
        url = "https://thinking-tester-contact-list.herokuapp.com/addUser"
        super().__init__(driver, url)

    def enter_first_name(self, first_name: str):
        self.driver.find_element(By.ID, "firstName").send_keys(first_name)

    def enter_last_name(self, last_name: str):
        self.driver.find_element(By.ID, "lastName").send_keys(last_name)

    def enter_email(self, email: str):
        self.driver.find_element(By.ID, "email").send_keys(email)

    def enter_password(self, password: str):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_sign_up(self):
        self.driver.find_element(By.ID, "submit").click()

    def verify_signed_up(self):
        self.verify_browser_url_changed("https://thinking-tester-contact-list.herokuapp.com/contactList")

    def verify_sign_up_failed(self):
        try:
            error_element = self.driver.find_element(By.ID, "error")
            self.verify_element_is_displayed(error_element)
        except NoSuchElementException as exception:
            raise AssertionError("Error message not found") from exception

    def click_cancel(self):
        self.driver.find_element(By.ID, "cancel").click()

    def verify_cancel_button_works(self):
        self.verify_browser_url_changed("https://thinking-tester-contact-list.herokuapp.com/login")
