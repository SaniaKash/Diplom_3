import allure
from pages.base_page import BasePage
from locator.personal_account_locators import PersonaAccountLocators
from data import UserData


class PersonalAccount(BasePage):

    @allure.step('Открываем браузер Chrome')
    @allure.story('')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def wait_for_exit_button_located(self):
        self.visibility_of_element_located(PersonaAccountLocators.EXIT_BUTTON)

    def check_personal_account_url(self):
        return self.current_url()

    def click_order_history_button(self):
        return self.click_element(PersonaAccountLocators.ORDER_HISTORY_BUTTON)

    def wait_for_order_page_history_located(self):
        return self.visibility_of_element_located(PersonaAccountLocators.ORDER_HISTORY_PAGE)

    def check_order_history_page_is_active(self):
        return self.presence_of_element_detected(PersonaAccountLocators.ORDER_HISTORY_PAGE)

    def click_personal_account_exit_button(self):
        return self.click_element(PersonaAccountLocators.PERSONAL_ACCOUNT_EXIT_BUTTON)
