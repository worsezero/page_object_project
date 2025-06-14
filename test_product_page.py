from selenium.common.exceptions import NoAlertPresentException# в начале файла
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        login_link = " http://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(browser, login_link)
        login_page.open()

        # 2) Регистрируем нового пользователя
        email = f"{time.time()}@fakemail.org"
        password = "strongpass1613"
        login_page.register_new_user(email, password)

        # 3) Проверяем, что пользователь залогинен
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(self.browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()

        # Повторно создаём объект страницы, чтобы обновить состояние после действия
        page = ProductPage(self.browser, self.browser.current_url)
        page.should_be_success_message_with_product_name()
        page.should_be_basket_total_correct()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    # Проверяем успешное добавление и правильность суммы
    page.should_be_success_message_with_product_name()
    page.should_be_basket_total_correct()


@pytest.mark.xfail(reason="Success message is shown after adding product — known bug")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Success message doesn't disappear — known bug")
def test_message_disappears_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
    basket_page.should_be_empty_message_present()









