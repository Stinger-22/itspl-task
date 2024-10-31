import logging

from selenium.webdriver.remote.webdriver import WebDriver

LOGGER = logging.getLogger(__name__)


def test_app_loads(browser_chrome: WebDriver):
    browser_chrome.get("https://thinking-tester-contact-list.herokuapp.com/")
    LOGGER.info("Hello info")

    assert browser_chrome.title == "Contact List App"
