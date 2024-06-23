import allure
from pages.base_page import BasePage
from locator.main_page_locators import MainPageLocators
from data import UserData


class MainPage(BasePage):

    @allure.step('Открываем браузер Chrome')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Ожидаем появления картинки главной страницы.')
    def wait_for_main_page_located(self):
        return self.visibility_of_element_located(MainPageLocators.MAIN_PAGE_IMG)

    @allure.step('Нажимаем кнопку "Войти в аккаунт".')
    def click_enter_account_button(self):
        return self.click_element(MainPageLocators.PRIMARY_ENTER_BUTTON)

    @allure.step('Нажимаем кнопку "Личный кабинет".')
    def click_personal_account_button(self):
        return self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Ожидаем появления кнопки "Личный кабинет".')
    def wait_for_personal_account_button_located(self):
        return self.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Нажимаем кнопку "Конструктор".')
    def click_constructor_button(self):
        return self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Нажимаем кнопку "Лента заказов".')
    def click_order_feed_button(self):
        return self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Ожидаем появления URL страницы "Лента заказов".')
    def wait_for_url_order_feed_to_be(self):
        return self.visibility_of_url_located(UserData.ORDER_FEED_URL)

    @allure.step('Кликаем ингредиент "Соус спайси".')
    def click_ingredient_souse_spicy(self):
        return self.click_element(MainPageLocators.INGREDIENT_SOUSE_SPICY)

    @allure.step('Ожидаем появления окна с деталями "Соус спайси".')
    def wait_for_details_ingredient_souse_spicy_visible(self):
        return self.presence_of_element_detected(MainPageLocators.INGREDIENT_SOUSE_SPICY_DETAILS)

    @allure.step('Проверка отображения окна с деталями "Соус спайси".')
    def check_details_ingredients_is_displace(self):
        return self.presence_of_element_detected(MainPageLocators.INGREDIENT_SOUSE_SPICY_DETAILS).is_displayed()

    @allure.step('Нажимаем кнопку закрыть в окне ингредиентов.')
    def click_close_button_ingredients(self):
        return self.click_element(MainPageLocators.INGREDIENT_CLOSE_BUTTON)

    @allure.step('Ожидаем появления окна с деталями ингредиента.')
    def wait_for_ingredients_details_window_closed(self):
        return self.presence_of_element_detected(MainPageLocators.INGREDIENTS_WINDOW_CLOSED)

    @allure.step('Проверяем закрытие окна с деталями ингредиента.')
    def check_ingredients_details_window_closed(self):
        return self.check_element_displayed(MainPageLocators.INGREDIENTS_WINDOW_CLOSED)

    @allure.step('Ожидаем отображения картинки "Соус спайси".')
    def wait_for_souse_spicy_located(self):
        return self.visibility_of_element_located(MainPageLocators.INGREDIENT_SOUSE_SPICY)

    @allure.step('Добавляем "Соус спайси" в корзину.')
    def add_souse_spicy_to_basket(self):
        return self.seletools_drag_and_drop_element(MainPageLocators.INGREDIENT_SOUSE_SPICY,
                                                    MainPageLocators.BURGER_CONSTRUCTOR_BASKET)

    @allure.step('Проверяем изменение количество "Соус спайси".')
    def check_change_souse_spicy_counter(self):
        return self.get_text(MainPageLocators.INGREDIENT_SOUSE_SPICY_COUNTER)

    @allure.step('Ожидаем появления кнопки "Оформить заказ".')
    def wait_for_make_order_located(self):
        return self.visibility_of_element_located(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Нажимаем кнопку "Оформить заказ".')
    def click_make_order_button(self):
        return self.click_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Ожидание появления картинки в "Заказ оформлен".')
    def wait_for_order_img_loaded(self):
        return self.visibility_of_element_located(MainPageLocators.ORDER_IMG)

    @allure.step('Ожидаем появления окна "Заказ оформлен".')
    def wait_for_order_page_located(self):
        return self.visibility_of_element_located(MainPageLocators.DONE_ORDER_PAGE)

    @allure.step('Проверяем отображения окна "Заказ оформлен".')
    def check_done_order_page_is_displaced(self):
        return self.presence_of_element_detected(MainPageLocators.DONE_ORDER_PAGE).is_displayed()

    @allure.step('Добавляем бургер "Н200" в корзину.')
    def add_n200_bun_to_basket(self):
        return self.seletools_drag_and_drop_element(MainPageLocators.N200_BUN,
                                                    MainPageLocators.BURGER_CONSTRUCTOR_BASKET)

    @allure.step('Получаем номер заказа.')
    def get_order_numer(self):
        count = self.get_text(MainPageLocators.ORDER_NUMMER)
        return count
