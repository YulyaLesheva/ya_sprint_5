import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.ie.webdriver import WebDriver

from data.constants import WEB_SITE_ADDRESS
from data.website_data import Pages, Buttons


class TestLogIn:

    @pytest.mark.parametrize('button', [Buttons.ACCOUNT_ENTER.value, Buttons.PERSONAL_ACCOUNT.value])
    def test_login_main_page(self, request, driver, button):

        driver.get(WEB_SITE_ADDRESS)
        driver.find_element(By.XPATH, button).click()

        request.getfixturevalue('login')

        self._check_login(driver)

    @pytest.mark.parametrize('page_url', [Pages.REGISTER.value, Pages.FORGOT_PASSWORD.value])
    def test_login(self, request, driver, page_url):

        driver.get(WEB_SITE_ADDRESS + page_url)
        driver.find_element(By.XPATH, Buttons.LOGIN_HYPERTEXT.value).click()

        request.getfixturevalue('login')

        self._check_login(driver)

    @staticmethod
    def _check_login(driver: WebDriver):

        assert WebDriverWait(driver, timeout=3).until(expected_conditions.
                                                      presence_of_element_located((By.XPATH, Buttons.ORDER.value)))
