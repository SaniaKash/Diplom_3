from conftest import driver, popup
from pages.main_page import MainPage
from pages.enter_page import EnterPage
from pages.forgot_pass_page import ForgotPassPage
from pages.personal_account_page import PersonalAccount
from data import UserData
from pages.rec_pass_page import RecPassPage
import allure


class TestPersonalAccount:

    def test_open_personal_account_through_personal_acc_butt_success(self, driver, popup):
        user = MainPage(driver)
        user.wait_for_personal_account_button_located()
        user.click_personal_account_button()
        user = PersonalAccount(driver)
        user.wait_for_exit_button_located()
        assert user.check_personal_account_url() == UserData.PERSONAL_ACCOUNT_URL

    def test_open_page_order_history_from_personal_account(self, driver, popup):
        user = MainPage(driver)
        user.wait_for_personal_account_button_located()
        user.click_personal_account_button()
        user = PersonalAccount(driver)
        user.click_order_history_button()
        assert user.check_order_history_page_is_active()

    def test_click_exit_button_personal_account_open_login_page_success(self, driver, popup):
        user = MainPage(driver)
        user.wait_for_personal_account_button_located()
        user.click_personal_account_button()
        user = PersonalAccount(driver)
        user.click_personal_account_exit_button()
        user = EnterPage(driver)
        user.wait_for_enter_button_located()
        assert user.current_url() == UserData.LOGIN_URL
