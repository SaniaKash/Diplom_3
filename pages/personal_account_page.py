import allure
from pages.base_page import BasePage
from locator.personal_account_locators import PersonaAccountLocators


class PersonalAccount(BasePage):

    @allure.step('Открываем браузер Chrome')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Ожидаем появления кнопки "Выйти".')
    def wait_for_exit_button_located(self):
        self.visibility_of_element_located(PersonaAccountLocators.EXIT_BUTTON)

    @allure.step('Проверяем URL страницы "Личный кабинет".')
    def check_personal_account_url(self):
        return self.current_url()

    @allure.step('Нажимаем кнопку "История заказоы".')
    def click_order_history_button(self):
        return self.click_element(PersonaAccountLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Ожидаем отображения окна "История заказов".')
    def wait_for_order_page_history_located(self):
        return self.visibility_of_element_located(PersonaAccountLocators.ORDER_HISTORY_PAGE)

    @allure.step('Проверяем отображения окна "История заказов".')
    def check_order_history_page_is_active(self):
        return self.presence_of_element_detected(PersonaAccountLocators.ORDER_HISTORY_PAGE)

    @allure.step('Нажимаем кнопку "Выход" в личном кабинете.')
    def click_personal_account_exit_button(self):
        return self.click_element(PersonaAccountLocators.PERSONAL_ACCOUNT_EXIT_BUTTON)

    @allure.step('Скролим до последнего заказа в истории заказов.')
    def scroll_to_last_order_history_page(self):
        return self.execute_script(PersonaAccountLocators.LAST_ORDER_NUMMER)

    @allure.step('Получаем номер последнего заказа.')
    def get_text_last_order(self):
        return self.get_text(PersonaAccountLocators.LAST_ORDER_NUMMER)
