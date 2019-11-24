from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_MESSAGE_EQUAL_REAL_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    REAL_PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BASKET_AMOUNT_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > p[class="price_color"]')
