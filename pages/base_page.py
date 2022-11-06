from pages.locators import HeaderLocators, FooterLocators
from settings import BASE_URL
from test_data.user import TestUser


class BasePage:
    def __init__(self, driver):
        self.headers_locators = HeaderLocators
        self.footers_locators = FooterLocators
        self.driver = driver
        self.url = BASE_URL

    def open(self, url=None):
        if url:
            self.driver.get(url)
        else:
            self.driver.get(self.url)
        print(self.driver.name)

    def check_url(self, url=None):
        """
        Проверка соответствия текущего адреса адресу страницы
        :param url: str
        """
        if url:
            assert self.driver.current_url == url
        else:
            assert self.driver.current_url == self.url, f"ФР: {self.driver.current_url}\n" \
                                                        f"ОР: {self.url}"

    def click_to_login_link(self):
        login_link = self.driver.find_element(*self.headers_locators.LOGIN_LINK)
        login_link.click()

    def click_to_cart_link(self):
        login_link = self.driver.find_element(*self.headers_locators.CART_LINK)
        login_link.click()

    def verify_accout_link(self, user: TestUser):
        """
        Проверка наличия email пользователя в ссылке на профиль в хедере
        :param user: TestUser
        """
        assert user.email in self.driver.find_element(*self.headers_locators.ACCOUNT_LINK).text
