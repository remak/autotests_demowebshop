from selenium.webdriver.common.by import By


class HeaderLocators:
    REGISTER_LINK = (By.CSS_SELECTOR, ".ico-register")
    LOGIN_LINK = (By.CSS_SELECTOR, ".ico-login")
    CART_LINK = (By.CSS_SELECTOR, "a[class='ico-cart'] span[class='cart-label']")
    WISHLIST_LINK = (By.CSS_SELECTOR, "a[class='ico-wishlist'] span[class='cart-label']")
    ACCOUNT_LINK = (By.CSS_SELECTOR, "div[class='header-links'] a[class='account']")


class FooterLocators:
    SITEMAP_LINK = (By.CSS_SELECTOR, "a[href='/sitemap']")


class MainPageLocators(HeaderLocators, FooterLocators):
    pass


class CartPageLocators(HeaderLocators, FooterLocators):
    COUNT_ITEMS = (By.CSS_SELECTOR, ".qty-input")


class ProductPageLocators(HeaderLocators, FooterLocators):
    ADD_TO_CART_BUTTON = (By.XPATH, "//input[@value='Add to cart']")


class CategoryPageLocators(HeaderLocators, FooterLocators):
    CATEGORY_TITLE = (By.CSS_SELECTOR, "div[class='page-title'] h1")
    CATEGORY_ORDERBY_SELECT = (By.CSS_SELECTOR, "#products-orderby")
    PRODUCT_ITEM = (By.CSS_SELECTOR, ".product-item")
    PRODUCT_ITEM_TITLE = (By.CSS_SELECTOR, ".product-title > a")
    PRODUCT_ITEM_PRICE = (By.CSS_SELECTOR, ".price.actual-price")


class LoginPageLocators(HeaderLocators, FooterLocators):
    EMAIL_FIELD = (By.CSS_SELECTOR, "#Email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#Password")
    REMEMBER_ME_CHECKBOX = (By.CSS_SELECTOR, "#RememberMe")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='Log in']")


class RegisterPageLocators:
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#FirstName")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "#LastName")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#Email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#Password") 
    PASSWORD_CONFIRM_FIELD = (By.CSS_SELECTOR, "#ConfirmPassword")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register-button")
    VALIDATION_ERRORS = (By.CSS_SELECTOR, "div.message-error > div.validation-summary-errors > ul > li")
    VALIDATION_ERROR_EMAIL_EXISTS_TEXT = "The specified email already exists"
