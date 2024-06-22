import allure
from pages.base_page import BasePage
from locator.recover_pas_page_locators import RecPassPageLocator
from data import UserData



class RecPassPage(BasePage):
    @allure.step('Открываем браузер Chrome')
    @allure.story('')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def wait_for_password_field_located(self):
        return self.visibility_of_element_located(RecPassPageLocator.RECOVER_PASSWORD_FIELD)

    def check_recover_page_url(self):
        return self.current_url()

    def input_recover_password(self):
        return self.input_text(RecPassPageLocator.RECOVER_PASSWORD_FIELD, UserData.RECOVER_PASSWORD)

    def wait_for_hide_butt_is_clickable(self):
        return self.visibility_of_element_located(RecPassPageLocator.INPUT_ICON)

    def click_hide_button(self):
        return self.click_element(RecPassPageLocator.INPUT_ICON)

    def check_rec_pass_field_active_success(self):
        return self.visibility_of_element_located(RecPassPageLocator.PASSWORD_FIELD_FOCUSED).is_displayed()

