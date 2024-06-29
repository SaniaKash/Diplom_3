import allure
from pages.base_page import BasePage
from locator.enter_page_locators import EnterPageLocators
from data import UserData


class EnterPage(BasePage):

    @allure.step('Открываем браузер Chrome')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Кликаем гиперссылку "Восстановить пароль".')
    def click_link_recover_password(self):
        return self.click_element(EnterPageLocators.FORGOT_PASSWORD)

    @allure.step('Вводим имейл.')
    def input_email_text(self):
        return self.input_text(EnterPageLocators.INPUT_EMAIL, UserData.EMAIL)

    @allure.step('Вводим пароль.')
    def input_password_text(self):
        return self.input_text(EnterPageLocators.INPUT_PASSWORD, UserData.RECOVER_PASSWORD)

    @allure.step('Нажимаем кнопку "Войти".')
    def click_enter_button(self):
        return self.click_element(EnterPageLocators.ENTER_BUTTON)

    @allure.step('Ожидаем видимости кнопки "Войти".')
    def wait_for_enter_button_located(self):
        return self.visibility_of_element_located(EnterPageLocators.ENTER_BUTTON)
