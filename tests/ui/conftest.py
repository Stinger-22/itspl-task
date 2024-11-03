import logging

import pytest
from selenium import webdriver

from tests.ui.pages.log_in import LogInPage
from tests.ui.pages.sign_up import SignUpPage

LOGGER = logging.getLogger(__name__)


@pytest.fixture
def browser_chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def log_in_page(browser_chrome):
    return LogInPage(browser_chrome)

@pytest.fixture
def sign_up_page(browser_chrome):
    return SignUpPage(browser_chrome)
