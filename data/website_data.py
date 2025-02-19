from enum import Enum


class Pages(Enum):
    REGISTER = 'register'
    LOGIN = 'login'
    FORGOT_PASSWORD = 'forgot-password'
    PROFILE = 'account/profile'


class Forms(Enum):
    NAME = '//input[@name="name" and contains(@class, "input__textfield")]'
    PASSWORD = '//input[@type="password" and @name="Пароль"]'
    EMAIL = '//label[contains(text(), "Email")]/following-sibling::input'


class Buttons(Enum):
    SIGN_UP = '//form/button'
    ACCOUNT_ENTER = '//section[2]//button[contains(text(), "Войти в аккаунт")]'
    PERSONAL_ACCOUNT = '//nav//p[contains(text(), "Личный Кабинет")]'
    LOGIN_HYPERTEXT = '//a[@href="/login" and text()="Войти"]'
    LOGIN = '//button[contains(text(), "Войти")]'
    ORDER = '//button[text()="Оформить заказ"]'
    CONSTRUCTOR = '//p[contains(text(), "Конструктор")]'
    LOGO = '//div[contains(@class, "AppHeader_header__logo__")]'
    LOGOUT = '//button[contains(text(), "Выход")]'


class Errors(Enum):
    EXISTED_USER = '//p[contains(@class, "input__error")]'
    INCORRECT_PASSWORD = '//fieldset[3]//p[contains(text(), "Некорректный пароль")]'


class ConstructorTabs(Enum):
    BUNS = "//div[1]/span"
    SAUCES = '//div[2]/span'
    FILL = '//div[3]/span'

    SAUCES_TEXT = '//h2[contains(text(), "Соусы")]'
    BUNS_TEXT = '//h2[contains(text(), "Булки")]'
    FILL_TEXT = '//h2[contains(text(), "Начинки")]'





