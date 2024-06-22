from conftest import driver
from pages.main_page import MainPage
from pages.enter_page import EnterPage
from pages.forgot_pass_page import ForgotPassPage
from pages.personal_account_page import PersonalAccount
from data import UserData
from pages.rec_pass_page import RecPassPage
import allure


class TestBasicFunctionality:
    def test_click_constructor_from_login_page_success(self, driver):
        user = MainPage(driver)
        user.wait_for_main_page_located()
        user.click_enter_account_button()
        user = EnterPage(driver)
        user.wait_for_enter_button_located()
        user = MainPage(driver)
        user.click_constructor_button()
        user.wait_for_main_page_located()
        assert user.current_url() == UserData.MAIN_PAGE_BURGER_URL

    def test_click_order_feed_field_open_order_feed_page_success(self, driver):
        user = MainPage(driver)
        user.wait_for_main_page_located()
        user.click_order_feed_button()
        user.wait_for_url_order_feed_to_be()
        assert user.current_url() == UserData.ORDER_FEED_URL

    def test_click_ingredient_opened_details_success(self, driver):
        user = MainPage(driver)
        user.wait_for_main_page_located()
        user.click_ingredient_souse_spicy()
        user.wait_for_details_ingredient_souse_spicy_visible()
        assert user.check_details_ingredients_is_displace()

    def test_click_close_button_ingredient_closed_details_window_success(self, driver):
        user = MainPage(driver)
        user.wait_for_main_page_located()
        user.click_ingredient_souse_spicy()
        user.wait_for_details_ingredient_souse_spicy_visible()
        user.click_close_button_ingredients()
        assert user.check_ingredients_details_window_closed()

    def test_add_ingredient_souse_spicy_in_basket_change_counter_success(self, driver):
        user = MainPage(driver)
        user.wait_for_souse_spicy_located()
        user.add_souse_spicy_to_basket()
        assert user.check_change_souse_spicy_counter()

    def test_click_place_order_logged_user_new_order_success(self, driver):
        user = MainPage(driver)
        user.wait_for_main_page_located()
        user.click_personal_account_button()
        user = EnterPage(driver)
        user.input_email_text()
        user.input_password_text()
        user.click_enter_button()
        user = MainPage(driver)
        user.wait_for_make_order_located()
        user.click_make_order_button()
        user.wait_for_order_page_located()
        assert user.check_done_order_page_is_displaced()
