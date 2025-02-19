import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.constants import WEB_SITE_ADDRESS
from data.website_data import Pages, Forms, Buttons, Errors
from generators import email_generator, text_generator
from data.test_data import TestData


@pytest.mark.usefixture('driver')
class TestSignUp:

    def test_signing_up(self, driver):

        driver.get(WEB_SITE_ADDRESS + Pages.REGISTER.value)

        name = driver.find_element(By.XPATH, value=Forms.NAME.value)
        random_name = text_generator(limitation=5)
        name.send_keys(random_name)

        email = driver.find_element(By.XPATH, value=Forms.EMAIL.value)
        random_email = email_generator()
        email.send_keys(random_email)

        password = driver.find_element(By.XPATH, value=Forms.PASSWORD.value)
        password.send_keys(TestData.PASSWORD.value)

        driver.find_element(By.XPATH, value=Buttons.SIGN_UP.value).click()

        expected_page = WEB_SITE_ADDRESS + Pages.LOGIN.value
        assert WebDriverWait(driver, timeout=3).until(expected_conditions.url_to_be(expected_page))

    @pytest.mark.parametrize('invalid_passwords', [1, 3, 5])
    def test_incorrect_password_input(self, invalid_passwords, driver):

        sign_in_page = WEB_SITE_ADDRESS + Pages.REGISTER.value
        driver.get(sign_in_page)

        password = driver.find_element(By.XPATH, value=Forms.PASSWORD.value)
        random_password = text_generator(limitation=invalid_passwords)
        password.send_keys(random_password)

        driver.find_element(By.XPATH, value=Buttons.SIGN_UP.value).click()

        assert driver.find_elements(By.XPATH, Errors.INCORRECT_PASSWORD.value) and driver.current_url == sign_in_page
