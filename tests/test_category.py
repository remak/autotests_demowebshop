import pytest

from pages.category_page import CategoryPage
from pages.login_page import LoginPage


class TestCategoryHeaderLinks:
    CATEGORY = "desktops"

    @pytest.fixture
    def category_page(self, driver):
        category_page = CategoryPage(driver, self.CATEGORY)
        category_page.open()
        self.driver = driver
        yield category_page

    def test_link_to_login(self, category_page):
        category_page.click_to_login_link()
        login_page = LoginPage(self.driver)
        login_page.check_url()


class TestCategoryProducts:
    CATEGORY = {"name": "desktops", "count": 6}
    PRODUCT = {
        "name": "Build your own cheap computer",
        "rating": 46,
        "price": "800.00"
    }

    @pytest.fixture
    def category_page(self, driver):
        category_page = CategoryPage(driver, self.CATEGORY["name"])
        category_page.open()
        self.driver = driver
        return category_page

    def test_count_products_on_page(self, category_page):
        products = category_page.get_all_products_on_page()
        assert len(products) == self.CATEGORY["count"]

    def test_item_price(self, category_page):
        products = category_page.get_all_products_on_page()
        item = products[0]
        item_price = category_page.get_product_price(item)
        assert item_price == self.PRODUCT["price"]
