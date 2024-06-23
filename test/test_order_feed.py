from conftest import driver, popup
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
        user.click_order_feed_button()
        user = OrderFeedPage(driver)
        user.click_first_order_in_order_feed()
        user.wait_for_details_window_in_order_feed_opened()
        assert user.check_for_details_window_in_order_feed_is_displayed()

    def test_user_order_from_history_order_displayed_in_order_feed_success(self, driver, popup):
        user = MainPage(driver)
        user.add_n200_bun_to_basket()
        user.click_make_order_button()
        user.click_close_button_ingredients()
        user.click_personal_account_button()
        user = PersonalAccount(driver)
        user.click_order_history_button()
        user.scroll_to_last_order_history_page()
        history_page_nummer = user.get_text_last_order()
        user = MainPage(driver)
        user.click_order_feed_button()
        user = OrderFeedPage(driver)
        order_feed_last_order = user.get_text_from_last_user_order()
        assert history_page_nummer == order_feed_last_order


    def test_all_time_counter_increase_after_new_order_created_success(self, driver, popup):
        user = MainPage(driver)
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

    def test_today_counter_increase_after_new_order_created_success(self, driver, popup):
        user = MainPage(driver)
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
        new_counter = user.get_today_counter()
        assert new_counter > old_counter

    def test_in_work_counter_is_displayed_after_new_order_created_success(self, driver, popup):
        user = MainPage(driver)
        user.add_n200_bun_to_basket()
        user.click_make_order_button()
        user.wait_for_order_img_loaded()
        order_counter = user.get_order_numer()
        user.click_close_button_ingredients()
        user.click_order_feed_button()
        user = OrderFeedPage(driver)
        user.wait_for_in_work_counter_visible()
        in_work_counter = user.get_in_work_counter()
        assert order_counter == in_work_counter



