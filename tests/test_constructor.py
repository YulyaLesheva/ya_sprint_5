import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.constants import WEB_SITE_ADDRESS
from data.website_data import ConstructorTabs


@pytest.mark.usefixtures('driver')
class TestConstructor:

    def test_constructor_tabs(self, driver):
        driver.get(WEB_SITE_ADDRESS)

        burger_parts = {
            'Соусы': (ConstructorTabs.SAUCES.value, ConstructorTabs.SAUCES_TEXT.value),
            'Булки': (ConstructorTabs.BUNS.value, ConstructorTabs.BUNS_TEXT.value),
            'Начинка': (ConstructorTabs.FILL.value, ConstructorTabs.FILL_TEXT.value),
        }

        for name, (tab_xpath, text_xpath) in burger_parts.items():
            WebDriverWait(driver, timeout=10).until(expected_conditions.
                                                    element_to_be_clickable((By.XPATH, tab_xpath))).click()

            assert WebDriverWait(driver, timeout=5).until(expected_conditions.presence_of_element_located((By.XPATH, text_xpath)))

        driver.quit()
