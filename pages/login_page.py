from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверка на корректный url адрес
        assert 'login' in self.browser.current_url, "'login' not in current url: {}".format(self.browser.current_url)

    def should_be_login_form(self):
        # Проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not exists"

    def should_be_register_form(self):
        # Проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not exists"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        email_input.send_keys(str(email))
        pass_input1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT)
        pass_input1.send_keys(str(password))
        pass_input2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT_INPUT)
        pass_input2.send_keys(str(password))
        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        register_button.click()
