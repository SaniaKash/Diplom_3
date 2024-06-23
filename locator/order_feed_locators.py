from selenium.webdriver.common.by import By


class OrderFeedLocators:
    FIRST_ORDER = By.XPATH, '//li[1]/a/h2'
    DETAILS_WINDOW = By.XPATH, "//*[@class ='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"
    ALL_TIME_COUNTER = By.XPATH, '//*[@class="undefined mb-15"]/*[contains(@class,"Order")]'
    TODAY_COUNTER = By.XPATH, '//div[3]/p[contains(@class,"OrderFeed_number")]'
    ORDER_IN_WORK = By.XPATH, "//ul[2]/*[@class='text text_type_digits-default mb-2']"
    LAST_ORDER_USER_TEXT = By.XPATH, '//li[1]//p[contains(text(), "#")]'
