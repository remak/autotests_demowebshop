import pytest

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestHeaderLinks:

    @pytest.fixture
    def main_page(self, driver):
        main_page = MainPage(driver)
        self.driver = driver
        main_page.open()
        yield main_page

    def test_link_to_login(self, main_page):
        main_page.click_to_login_link()
        login_page = LoginPage(self.driver)
        login_page.check_url()

    def test_link_to_cart(self, main_page):
        main_page.click_to_cart_link()
        login_page = CartPage(self.driver)
        login_page.check_url()
