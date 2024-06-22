import allure

from pages.base_page import BasePage
from locator.forgot_pass_locators import ForgotPassPageLocators
from conftest import driver
from data import UserData


class ForgotPassPage(BasePage):

    @allure.step('Открываем браузер Chrome')
    @allure.story('')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def wait_for_recover_butt_located(self):
        return self.visibility_of_element_located(ForgotPassPageLocators.RECOVER_BUTT)
    def check_rec_pass_page_url(self):
        return self.current_url()

    def input_email(self):
        return self.input_text(ForgotPassPageLocators.INPUT_EMAIL, UserData.EMAIL)

    def click_recover_butt(self):
        return self.click_element(ForgotPassPageLocators.RECOVER_BUTT)
