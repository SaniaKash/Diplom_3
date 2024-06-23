from conftest import driver, popup
from pages.main_page import MainPage
from pages.enter_page import EnterPage
from pages.personal_account_page import PersonalAccount
from data import UserData
import allure


class TestPersonalAccount:

    @allure.title('Проверка перехода по клику на «Личный кабинет».')
    def test_open_personal_account_through_personal_acc_butt_success(self, driver, popup):
        user = MainPage(driver)
        user.click_personal_account_button()
        user = PersonalAccount(driver)
        user.wait_for_exit_button_located()
        assert user.check_personal_account_url() == UserData.PERSONAL_ACCOUNT_URL

    @allure.title('Проверка перехода в раздел «История заказов».')
    def test_open_page_order_history_from_personal_account(self, driver, popup):
        user = MainPage(driver)
        user.click_personal_account_button()
        user = PersonalAccount(driver)
        user.click_order_history_button()
        assert user.check_order_history_page_is_active()

    @allure.title('Проверка выхода из аккаунта.')
    def test_click_exit_button_personal_account_open_login_page_success(self, driver, popup):
        user = MainPage(driver)
        user.click_personal_account_button()
        user = PersonalAccount(driver)
        user.click_personal_account_exit_button()
        user = EnterPage(driver)
        user.wait_for_enter_button_located()
        assert user.current_url() == UserData.LOGIN_URL
