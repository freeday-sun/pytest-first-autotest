from pytest_first_autotest.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from .login_page import LoginPage


class MainPage(BasePage):
    pass
#   функциональность перенесена в base_page.py, т.к. перейти на страницу логина можно с любой страницы
#    def go_to_login_page(self):
#        link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
#        link.click()
#        для использования явной инициализации страниц
#        return LoginPage(browser=self.browser, url=self.browser.current_url)

#    def should_be_login_link(self):
#        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"

