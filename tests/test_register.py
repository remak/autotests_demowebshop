from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from test_data.user import FakeUser


class TestRegisterPage:
    def test_link_to_login(self, driver):
        register_page = RegisterPage(driver)
        register_page.open()
        register_page.click_to_login_link()
        login_page = LoginPage(driver)
        login_page.check_url()

    def test_fill_first_name_field(self, driver):
        register_page = RegisterPage(driver)
        register_page.open()
        register_page.fill_register_form(FakeUser)
        register_page.verify_accout_link(FakeUser)
