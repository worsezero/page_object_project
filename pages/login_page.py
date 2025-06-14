from .product_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Login URL is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email: str, password: str):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        pass1_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        pass2_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        email_input.send_keys(email)
        pass1_input.send_keys(password)
        pass2_input.send_keys(password)
        register_btn.click()



