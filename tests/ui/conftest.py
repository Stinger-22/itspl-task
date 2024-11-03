import logging

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from tests.ui.pages.log_in import LogInPage
from tests.ui.pages.sign_up import SignUpPage

LOGGER = logging.getLogger(__name__)


@pytest.fixture(params = ["Chrome", "Firefox"])
def driver(request):
    _driver = None
    if request.param == "Chrome":
        _driver = webdriver.Chrome()
    elif request.param == "Firefox":
        _driver = webdriver.Firefox()
    _driver.implicitly_wait(5)
    yield _driver
    _driver.quit()

@pytest.fixture
def log_in_page(driver: WebDriver):
    return LogInPage(driver)

@pytest.fixture
def sign_up_page(driver: WebDriver):
    return SignUpPage(driver)
