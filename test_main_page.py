from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        """Method for checking that the guest can go to the login page

        :param selenium.webdriver.Remote browser: Selenium WebDriver instance
        :return None
        """
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)    # явная инициализация страницы через класс
        login_page.should_be_login_page()  # выполняем метод страницы - проверка на существование Login page
        login_page.should_be_login_form()  # выполняем метод страницы - проверка на существование формы для логина
        login_page.should_be_register_form()  # проверка на существование формы для регистрации
        login_page.should_be_login_url()  # выполняем метод страницы - проверка, что url имеет слово "login"

    def test_guest_should_see_login_link(self, browser):
        """Method for checking that the guest see login button

        :param selenium.webdriver.Remote browser: Selenium WebDriver instance
        :return None
        """
        page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        page.open() # открываем страницу
        page.should_be_login_link() # выполняем метод страницы - проверка на существовании кнопки Логин


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """Method for checking that the guest see login button

    :param selenium.webdriver.Remote browser: Selenium WebDriver instance
    :return None
    """
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()  # выполняем метод страницы - переход на страницу корзины
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.empty_basket_doesnt_have_a_proceed_to_checkout_button()  # проверка, что нет кнопки proceed_to_checkout
    basket_page.empty_basket_have_text()  # выполняем метод страницы - в пустой корзине есть текст о том, что она пуста


