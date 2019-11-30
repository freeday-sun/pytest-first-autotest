import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from time import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """fixture to prepare data before the test

        :param selenium.webdriver.Remote browser: Selenium WebDriver instance
        """
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = str(time()) + "@fakemail.org"
        user_password = range(0, 15)
        login_page.register_new_user(email, user_password)  # используем метод для регистрации новых пользователей
        login_page.should_be_authorized_user() # используем метод BasePage - проверка, что юзер авторизовался

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """Method for checking user can add product to basket

        :param selenium.webdriver.Remote browser: Selenium WebDriver instance
        """
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        page.open()
        page.add_product_to_basket()  # выполняем метод страницы - добавлении продукта в корзину
        page.solve_quiz_and_get_code()  # выполняем метод страницы BasePage - решение мат. примера в алерте
        page.product_must_be_added_to_basket()  # выполняем метод страницы - проверка добавления продукта в корзину
        page.product_price_equal_basket_amount()  # проверка - баланс корзины должен быть равен цене продукта

    def test_user_cant_see_success_message(self, browser):
        """Method for checking user cant see success message

        :param selenium.webdriver.Remote browser: Selenium WebDriver instance
        """
        print(link)
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        page.open()
        page.should_not_be_success_message()  # проверка - при заходе на страницу товару не должно быть лишних сообщений


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Method for checking guest cant see success message after adding product to basket

    :param selenium.webdriver.Remote browser: Selenium WebDriver instance
    """
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.add_product_to_basket()  # выполняем метод страницы - добавлении продукта в корзину
    page.solve_quiz_and_get_code()  # выполняем метод страницы BasePage - решение мат. примера в алерте
    page.should_not_be_success_message()  # при добавлении товара в корзину не должно быть сообщения успещности


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Method for checking message disappeared after adding product to basket

    :param selenium.webdriver.Remote browser: Selenium WebDriver instance
    """
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_is_disappear()  # после добавления товара в корзину сообщение должно исчезнуть


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.empty_basket_doesnt_have_a_proceed_to_checkout_button()
    basket_page.empty_basket_have_text()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    print(link)
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_must_be_added_to_basket()
    page.product_price_equal_basket_amount()


def test_user_cant_see_success_message(browser):
    print(link)
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.should_not_be_success_message()
