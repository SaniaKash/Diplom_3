import allure
from pages.base_page import BasePage
from locator.recover_pas_page_locators import RecPassPageLocator
from data import UserData


class RecPassPage(BasePage):
    @allure.step('Открываем браузер Chrome')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Ожидаем появления поля "Пароль".')
    def wait_for_password_field_located(self):
        return self.visibility_of_element_located(RecPassPageLocator.RECOVER_PASSWORD_FIELD)

    @allure.step('Проверяем URL страницы "Восстановить пароль".')
    def check_recover_page_url(self):
        return self.current_url()

    @allure.step('Нажимаем кнопку "Восстановить Пароль".')
    def input_recover_password(self):
        return self.input_text(RecPassPageLocator.RECOVER_PASSWORD_FIELD, UserData.RECOVER_PASSWORD)

    @allure.step('Ожидаем кликабельности кнопки показать/скрыть.')
    def wait_for_hide_butt_is_clickable(self):
        return self.visibility_of_element_located(RecPassPageLocator.INPUT_ICON)

    @allure.step('Нажимаем кнопку показать/скрыть.')
    def click_hide_button(self):
        return self.click_element(RecPassPageLocator.INPUT_ICON)

    @allure.step('Проверяем отображение текста в поле "Восстановить пароль".')
    def check_rec_pass_field_active_success(self):
        return self.check_element_displayed(RecPassPageLocator.PASSWORD_FIELD_FOCUSED)

