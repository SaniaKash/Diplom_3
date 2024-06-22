from conftest import driver
from pages.main_page import MainPage
from pages.enter_page import EnterPage
from pages.forgot_pass_page import ForgotPassPage
from data import UserData
from pages.rec_pass_page import RecPassPage
import allure



class TestRecoverPassword:

    def test_click_rec_pass_link_open_rec_pass_page_success(self, driver):
        user = MainPage(driver)
        user.wait_for_main_page_located()
        user.click_enter_account_button()
        user = EnterPage(driver)
        user.click_link_recover_password()
        user = ForgotPassPage(driver)
        user.wait_for_recover_butt_located()
        assert user.current_url() == UserData.FORGOT_URL

    def test_click_recover_butt_input_email_success(self, driver):
        user = MainPage(driver)
        user.wait_for_main_page_located()
        user.click_enter_account_button()
        user = EnterPage(driver)
        user.click_link_recover_password()
        user = ForgotPassPage(driver)
        user.input_email()
        user.click_recover_butt()
        user = RecPassPage(driver)
        user.wait_for_password_field_located()
        assert user.current_url() == UserData.RECOVER_URL

    def test_click_butt_show_or_hide_active_password_field_success(self, driver):
        user = MainPage(driver)
        user.wait_for_main_page_located()
        user.click_enter_account_button()
        user = EnterPage(driver)
        user.click_link_recover_password()
        user = ForgotPassPage(driver)
        user.input_email()
        user.click_recover_butt()
        user = RecPassPage(driver)
        user.wait_for_password_field_located()
        user.input_recover_password()
        user.wait_for_hide_butt_is_clickable()
        user.click_hide_button()
        assert user.check_rec_pass_field_active_success()






