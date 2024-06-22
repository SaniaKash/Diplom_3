import allure
from pages.base_page import BasePage
from locator.main_page_locators import MainPageLocators
from data import UserData


class MainPage(BasePage):

    @allure.step('Открываем браузер Chrome')
    @allure.story('')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def wait_for_main_page_located(self):
        self.visibility_of_element_located(MainPageLocators.MAIN_PAGE_IMG)

    def click_enter_account_button(self):
        return self.click_element(MainPageLocators.PRIMARY_ENTER_BUTTON)

    def click_personal_account_button(self):
        return self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def wait_for_personal_account_button_located(self):
        return self.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_constructor_button(self):
        return self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed_button(self):
        return self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    def wait_for_url_order_feed_to_be(self):
        return self.visibility_of_url_located(UserData.ORDER_FEED_URL)

    def click_ingredient_souse_spicy(self):
        return self.click_element(MainPageLocators.INGREDIENT_SOUSE_SPICY)

    def wait_for_details_ingredient_souse_spicy_visible(self):
        return self.presence_of_element_detected(MainPageLocators.INGREDIENT_SOUSE_SPICY_DETAILS)

    def check_details_ingredients_is_displace(self):
        return self.presence_of_element_detected(MainPageLocators.INGREDIENT_SOUSE_SPICY_DETAILS).is_displayed()

    def click_close_button_ingredients(self):
        return self.click_element(MainPageLocators.INGREDIENT_CLOSE_BUTTON)

    def wait_for_ingredients_details_window_closed(self):
        return self.presence_of_element_detected(MainPageLocators.INGREDIENTS_WINDOW_CLOSED)

    def check_ingredients_details_window_closed(self):
        return self.check_element_displayed(MainPageLocators.INGREDIENTS_WINDOW_CLOSED)

    def wait_for_souse_spicy_located(self):
        return self.visibility_of_element_located(MainPageLocators.INGREDIENT_SOUSE_SPICY)

    def add_souse_spicy_to_basket(self):
        return self.seletools_drag_and_drop_element(MainPageLocators.INGREDIENT_SOUSE_SPICY,
                                                    MainPageLocators.BURGER_CONSTRUCTOR_BASKET)

    def check_change_souse_spicy_counter(self):
        return self.check_element_displayed(MainPageLocators.INGREDIENT_SOUSE_SPICY_COUNTER)

    def wait_for_make_order_located(self):
        return self.visibility_of_element_located(MainPageLocators.MAKE_ORDER_BUTTON)

    def click_make_order_button(self):
        return self.click_element(MainPageLocators.MAKE_ORDER_BUTTON)

    def wait_for_order_page_located(self):
        return self.visibility_of_element_located(MainPageLocators.DONE_ORDER_PAGE)

    def check_done_order_page_is_displaced(self):
        return self.presence_of_element_detected(MainPageLocators.DONE_ORDER_PAGE).is_displayed()

    def add_n200_bun_to_basket(self):
        return self.seletools_drag_and_drop_element(MainPageLocators.N200_BUN,
                                                    MainPageLocators.BURGER_CONSTRUCTOR_BASKET)

    def get_order_numer(self):
        return self.get_text()
