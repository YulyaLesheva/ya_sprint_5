import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.constants import WEB_SITE_ADDRESS
from data.website_data import Buttons, Pages


@pytest.mark.usefixtures('login')
class TestLogOut:

    def test_log_out(self, driver):

        driver.find_element(By.XPATH, Buttons.PERSONAL_ACCOUNT.value).click()

        WebDriverWait(driver, timeout=5).until(expected_conditions.
                                               presence_of_element_located((By.XPATH, Buttons.LOGOUT.value)))

        driver.find_element(By.XPATH, Buttons.LOGOUT.value).click()

        assert WebDriverWait(driver, timeout=3).until(expected_conditions.
                                                      url_to_be(WEB_SITE_ADDRESS + Pages.LOGIN.value))

        driver.quit()
