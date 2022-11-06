from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from test_data.user import TestUser


class LoginPage(BasePage):
    URL_PATH = "/login"

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators
        # self.url = f"{BASE_URL}{self.URL_PATH}"
        self.url = self.url + self.URL_PATH

    def fill_email(self, value):
        self.driver.find_element(*self.locators.EMAIL_FIELD).send_keys(value)

    def fill_password(self, value):
        self.driver.find_element(*self.locators.PASSWORD_FIELD).send_keys(value)

    def click_login(self):
        self.driver.find_element(*self.locators.LOGIN_BUTTON).click()

    def login(self, user: TestUser):
        """
        Заполнение формы авторизации данными пользователя и отправка формы
        :param user: TestUser
        """
        self.fill_email(user.email)
        self.fill_password(user.password)
        self.click_login()
