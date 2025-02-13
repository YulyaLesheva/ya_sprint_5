import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.constants import WEB_SITE_ADDRESS
from data.website_data import Buttons, Pages


@pytest.mark.usefixtures('login')
class TestPersonalAccount:

    def test_go_to_personal_account_page(self, driver):

        driver.find_element(By.XPATH, Buttons.PERSONAL_ACCOUNT.value).click()

        assert WebDriverWait(driver, timeout=3).until(expected_conditions.
                                                      url_to_be(WEB_SITE_ADDRESS + Pages.PROFILE.value))

        driver.quit()

    @pytest.mark.parametrize('button', [Buttons.CONSTRUCTOR.value, Buttons.LOGO.value])
    def test_go_out_personal_account_page(self, driver, button):

        driver.find_element(By.XPATH, Buttons.PERSONAL_ACCOUNT.value).click()

        driver.find_element(By.XPATH, button).click()

        assert WebDriverWait(driver, timeout=3).until(expected_conditions.
                                                      url_to_be(WEB_SITE_ADDRESS))

        driver.quit()
