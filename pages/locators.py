from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn - lg")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_REPEAT_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > button[name=registration_submit]")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_MESSAGE_EQUAL_REAL_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    REAL_PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BASKET_AMOUNT_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > p[class="price_color"]')
    PRODUCT_SUCCESS_ADDED_MESSAGE = (By.CSS_SELECTOR, ".alertinner")



