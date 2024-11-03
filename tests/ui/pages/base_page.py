from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, url: str) -> None:
        self.driver = driver
        if url is None:
            self.url = "https://thinking-tester-contact-list.herokuapp.com/"
        else:
            self.url = url

    def open_page(self) -> None:
        self.driver.get(self.url)

    def verify_element_is_displayed(self, element: WebElement) -> None:
        try:
            wait = WebDriverWait(element, 5)
            wait.until(
                lambda element: element.is_displayed()
            )
        except TimeoutException as exception:
            error_msg = f"Element {element} is not displayed"
            raise AssertionError(error_msg) from exception

    def verify_browser_url_changed(self, new_url: str) -> None:
        try:
            wait = WebDriverWait(self.driver, 5)
            wait.until(
                lambda driver: driver.current_url == new_url
            )
        except TimeoutException as exception:
            raise AssertionError("url has not changed") from exception
