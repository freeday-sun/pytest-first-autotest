from pytest_first_autotest.pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to basket button is not exists"
        add_product_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_product_to_basket.click()

    def product_must_be_added_to_basket(self):
        product_name_in_message = \
            self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_EQUAL_REAL_PRODUCT_NAME)
        real_product_name = self.browser.find_element(*ProductPageLocators.REAL_PRODUCT_NAME)
        assert product_name_in_message.text == real_product_name.text, \
            'alert product name: "{}" real product name: "{}"'.format(product_name_in_message.text, real_product_name.text)

    def product_price_equal_basket_amount(self):
        basket_amount = self.browser.find_element(*ProductPageLocators.BASKET_AMOUNT_IN_MESSAGE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert basket_amount.text == product_price.text,\
            'alert basket amount: "{}" real product price: "{}"'.format(basket_amount.text, product_price.text)
