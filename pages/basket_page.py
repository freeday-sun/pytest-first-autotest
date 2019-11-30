from pytest_first_autotest.pages.base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def empty_basket_doesnt_have_a_proceed_to_checkout_button(self):
        """Method for checking that there are no products in an empty basket

        :return bool:
        """
        assert not self.is_element_present(*BasketPageLocators.PROCEED_TO_CHECKOUT_BUTTON), \
            "Empty basket have proceed_to_checkout_button"

    def empty_basket_have_text(self):
        """Method for checking that there is text in an empty basket

        :return bool:
        """
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Empty basket has no missing text"
