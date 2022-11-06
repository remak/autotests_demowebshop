from pages.base_page import BasePage
from pages.locators import CategoryPageLocators
from settings import BASE_URL
from selenium.webdriver.support.ui import Select


class CategoryPage(BasePage):

    def __init__(self, driver, category_name: str):
        super().__init__(driver)
        self.category_name = category_name
        self.locators = CategoryPageLocators
        self.url = f"{BASE_URL}/{self.category_name}"

    def get_all_products_on_page(self):
        return self.driver.find_elements(*self.locators.PRODUCT_ITEM)

    def get_product_by_name(self, name):
        products_on_page = self.get_all_products_on_page()
        for product in products_on_page:
            if self.get_product_name(product) == name:
                return product
        return False

    def open_product_page(self, product_name):
        self.get_product_by_name(product_name).click()

    def get_product_price(self, product):
        """
        Получаем цену продукта (актуальную)
        :param product: webelement
        :return: price: str
        """
        return product.find_element(*self.locators.PRODUCT_ITEM_PRICE).text

    def get_product_name(self, product):
        """
        Получаем название продукта
        :param product: webelement
        :return: name: str
        """
        return product.find_element(*self.locators.PRODUCT_ITEM_TITLE).text

    def select_order_type(self, order_value):
        """
        Select order type for products on category page
        :param order_value: value (int) from ?orderby=<>
        """
        select = Select(self.driver.find_element(*self.locators.CATEGORY_ORDERBY_SELECT))
        value = f"{self.url}?orderby={order_value}"
        select.select_by_value(value)
