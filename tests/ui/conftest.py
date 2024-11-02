import pytest
from selenium import webdriver


@pytest.fixture
def browser_chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
