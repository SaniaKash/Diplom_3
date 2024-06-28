import allure

from pages.base_page import BasePage
from locator.forgot_pass_locators import ForgotPassPageLocators
from conftest import driver
from data import UserData


class ForgotPassPage(BasePage):

    @allure.step('Открываем браузер Chrome')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Ожидаем видимости кнопки "Восстановить пароль".')
    def wait_for_recover_butt_located(self):
        return self.visibility_of_element_located(ForgotPassPageLocators.RECOVER_BUTT)

    @allure.step('Проверяем URL страницы "Забыли пароль".')
    def check_rec_pass_page_url(self):
        return self.current_url()

    @allure.step('Вводим эмейл.')
    def input_email(self):
        return self.input_text(ForgotPassPageLocators.INPUT_EMAIL_FORGOT_PASS, UserData.EMAIL)

    @allure.step('Нажимаем кнопку "Восстановить пароль".')
    def click_recover_butt(self):
        return self.click_element(ForgotPassPageLocators.RECOVER_BUTT)
