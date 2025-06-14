from .pages .main_page import MainPage
from .pages .login_page import LoginPage
from .pages .basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:
    # Тест проверяет, что гость может перейти на страницу логина с главной страницы
    def test_guest_can_go_to_login_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    # Тест проверяет, что на главной странице присутствует ссылка на логин
    def test_guest_should_see_login_link(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    # Тест проверяет, что корзина пуста при открытии с главной страницы и отображается сообщение об этом
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty()
        basket_page.should_be_empty_message_present()

    # Метод для перехода на страницу логина (используется в MainPage)
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()






