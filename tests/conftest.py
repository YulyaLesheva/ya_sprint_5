from typing import Any, Generator

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

from data.constants import WEB_SITE_ADDRESS
from data.website_data import Pages, Forms, Buttons
from data.test_data import TestData


@pytest.fixture
def driver() -> Generator[WebDriver, Any, None]:
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def login(driver) -> WebDriver:
    driver.get(WEB_SITE_ADDRESS + Pages.LOGIN.value)
    driver.find_element(By.XPATH, Forms.EMAIL.value).send_keys(TestData.EMAIL.value)
    driver.find_element(By.XPATH, Forms.PASSWORD.value).send_keys(TestData.PASSWORD.value)
    driver.find_element(By.XPATH, Buttons.LOGIN.value).click()
    return driver




