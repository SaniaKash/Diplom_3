import allure
from pages.base_page import BasePage
from locator.main_page_locators import MainPageLocators
from locator.order_feed_locators import OrderFeedLocators
from data import UserData



class OrderFeedPage(BasePage):
    @allure.step('Открываем браузер Chrome')
    @allure.story('')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def wait_for_order_in_order_feed_located(self):
        return self.clickable_of_element_located(OrderFeedLocators.FIRST_ORDER)

    def click_first_order_in_order_feed(self):
        return self.click_element(OrderFeedLocators.FIRST_ORDER)

    def wait_for_details_window_in_order_feed_opened(self):
        return self.presence_of_element_detected(OrderFeedLocators.DETAILS_WINDOW)

    def check_for_details_window_in_order_feed_is_displayed(self):
        return self.check_element_displayed(OrderFeedLocators.DETAILS_WINDOW)

    def get_all_time_counter(self):
        return self.get_text(OrderFeedLocators.ALL_TIME_COUNTER)

    def get_today_counter(self):
        return self.get_text(OrderFeedLocators.TODAY_COUNTER)

    def wait_for_in_work_counter_visible(self):
        return self.presence_of_element_detected(OrderFeedLocators.ORDER_IN_WORK)

    def get_in_work_counter(self):
        count = self.get_text(OrderFeedLocators.ORDER_IN_WORK)[1::]
        return count

    def get_text_from_last_user_order(self):
        return self.get_text(OrderFeedLocators.LAST_ORDER_USER_TEXT)

