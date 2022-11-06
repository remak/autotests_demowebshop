from .locators import RegisterPageLocators
from .base_page import BasePage
from settings import BASE_URL
from test_data.user import TestUser


class RegisterPage(BasePage):
    URL_PATH = "/register"

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RegisterPageLocators()
        self.url = f"{BASE_URL}{self.URL_PATH}"

    def fill_first_name(self, value):
        self.driver.find_element(*self.locators.FIRST_NAME_FIELD).send_keys(value)

    def fill_last_name(self, value):
        self.driver.find_element(*self.locators.LAST_NAME_FIELD).send_keys(value)

    def fill_email(self, value):
        self.driver.find_element(*self.locators.EMAIL_FIELD).send_keys(value)

    def fill_password(self, value):
        self.driver.find_element(*self.locators.PASSWORD_FIELD).send_keys(value)

    def fill_password_confirm(self, value):
        self.driver.find_element(*self.locators.PASSWORD_CONFIRM_FIELD).send_keys(value)

    def click_to_register_button(self):
        self.driver.find_element(*self.locators.REGISTER_BUTTON).click()

    def verify_validation_errors(self):
        """
        проверка наличия ошибки регистрации в связи с уже зарегистрированным email
        """
        assert self.locators.VALIDATION_ERROR_EMAIL_EXISTS_TEXT in self.driver.find_element(
            *self.locators.VALIDATION_ERRORS).text

    def fill_register_form(self, user: TestUser):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.fill_password(user.password)
        self.fill_password_confirm(user.password)
        self.click_to_register_button()
