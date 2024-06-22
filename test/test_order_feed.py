from conftest import driver
from pages.main_page import MainPage
from pages.enter_page import EnterPage
from pages.forgot_pass_page import ForgotPassPage
from pages.personal_account_page import PersonalAccount
from data import UserData
from pages.rec_pass_page import RecPassPage
from pages.order_feed_page import OrderFeedPage
import allure


class TestOrderFeed:

    def test_click_order_opened_details_window_success(self, driver):
        user = MainPage(driver)
        user.wait_for_main_page_located()
        user.click_order_feed_button()
        user = OrderFeedPage(driver)
        user.click_first_order_in_order_feed()
        user.wait_for_details_window_in_order_feed_opened()
        assert user.check_for_details_window_in_order_feed_is_displayed()

    def test_user_order_from_history_order_displayed_in_order_feed_success(self, driver):
        pass

    def test_all_time_counter_increase_after_new_order_created_success(self, driver):
        user = MainPage(driver)
        user.wait_for_main_page_located()
        user.click_personal_account_button()
        user = EnterPage(driver)
        user.input_email_text()
        user.input_password_text()
        user.click_enter_button()
        user = MainPage(driver)
        user.wait_for_personal_account_button_located()
        user.click_order_feed_button()
        user = OrderFeedPage(driver)
        old_counter = user.get_all_time_counter()
        user = MainPage(driver)
        user.click_constructor_button()
        user.add_n200_bun_to_basket()
        user.click_make_order_button()
        user.click_close_button_ingredients()
        user.click_order_feed_button()
        user = OrderFeedPage(driver)
        user.wait_for_order_in_order_feed_located()
        new_counter = user.get_all_time_counter()
        assert new_counter > old_counter

    def test_today_counter_increase_after_new_order_created_success(self, driver):
        user = MainPage(driver)
        user.wait_for_main_page_located()
        user.click_personal_account_button()
        user = EnterPage(driver)
        user.input_email_text()
        user.input_password_text()
        user.click_enter_button()
        user = MainPage(driver)
        user.wait_for_personal_account_button_located()
        user.click_order_feed_button()
        user = OrderFeedPage(driver)
        old_counter = user.get_today_counter()
        user = MainPage(driver)
        user.click_constructor_button()
        user.add_n200_bun_to_basket()
        user.click_make_order_button()
        user.click_close_button_ingredients()
        user.click_order_feed_button()
        user = OrderFeedPage(driver)
        user.wait_for_order_in_order_feed_located()
        new_counter = user.get_today_counter()
        assert new_counter > old_counter

    def test_in_work_counter_is_displayed_after_new_order_created_success(self, driver):
        user = MainPage(driver)
        user.wait_for_main_page_located()
        user.click_personal_account_button()
        user = EnterPage(driver)
        user.input_email_text()
        user.input_password_text()
        user.click_enter_button()
        user = MainPage(driver)
        user.wait_for_personal_account_button_located()



