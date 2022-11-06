from pages.login_page import LoginPage
from test_data.user import Active_User


class TestLogin:
    def test_login_ok(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(Active_User)
        login_page.verify_accout_link(Active_User)
