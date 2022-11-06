from pages.base_page import BasePage
from pages.locators import CartPageLocators
from settings import BASE_URL


class CartPage(BasePage):
    URL_PATH = "/cart"

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CartPageLocators
        self.url = f"{BASE_URL}{self.URL_PATH}"

    def get_count_item_value(self, element=None):
        if element:
            return element.find_element(*self.locators.COUNT_ITEMS).get_attribute("value")
        else:
            return self.driver.find_element(*self.locators.COUNT_ITEMS).get_attribute("value")

    def set_count_item_value(self,value):
        count_field = self.driver.find_element(*self.locators.COUNT_ITEMS)
        count_field.clear()
        count_field.send_keys(value)
