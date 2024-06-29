import allure
from conftest import driver, popup
from pages.main_page import MainPage
from pages.enter_page import EnterPage
from data import UserData


class TestBasicFunctionality:

    @allure.title('Проверка перехода по клику на «Конструктор».')
    def test_open_constructor_page_from_login_page_success(self, driver):
        user = MainPage(driver)
        user.click_enter_account_button()
        user = EnterPage(driver)
        user.wait_for_enter_button_located()
        user = MainPage(driver)
        user.click_constructor_button()
        user.wait_for_main_page_located()
        assert user.current_url() == UserData.MAIN_PAGE_BURGER_URL

    @allure.title('Проверка перехода по клику на «Лента заказов».')
    def test_click_order_feed_field_open_order_feed_page_success(self, driver):
        user = MainPage(driver)
        user.click_order_feed_button()
        user.wait_for_url_order_feed_to_be()
        assert user.current_url() == UserData.ORDER_FEED_URL

    @allure.title('Проверка открытия окна с деталями кликом на ингредиент.')
    def test_click_ingredient_opened_details_success(self, driver):
        user = MainPage(driver)
        user.click_ingredient_souse_spicy()
        user.wait_for_details_ingredient_souse_spicy_visible()
        assert user.check_details_ingredients_is_displace()

    @allure.title('Проверка закрытия всплывающего окна кликом по крестику.')
    def test_click_close_button_ingredient_closed_details_window_success(self, driver):
        user = MainPage(driver)
        user.click_ingredient_souse_spicy()
        user.wait_for_details_ingredient_souse_spicy_visible()
        user.click_close_button_ingredients()
        user.wait_for_ingredients_details_window_closed()
        assert user.check_ingredients_details_window_closed()

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается.')
    def test_add_ingredient_souse_spicy_in_basket_change_counter_success(self, driver):
        user = MainPage(driver)
        user.add_souse_spicy_to_basket()
        assert user.check_change_souse_spicy_counter() == '1'

    @allure.title('Проверка оформления заказа зарегистрированным пользователем.')
    def test_click_place_order_logged_user_new_order_success(self, driver, popup):
        user = MainPage(driver)
        user.wait_for_make_order_located()
        user.click_make_order_button()
        user.wait_for_order_page_located()
        assert user.check_done_order_page_is_displaced()
