from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # первый заказ
    FIRST_ORDER = By.XPATH, '//li[1]/a/h2'
    # окно деталей заказа
    DETAILS_WINDOW = By.XPATH, "//*[@class ='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"
    # счетчик "За все время"
    ALL_TIME_COUNTER = By.XPATH, '//*[@class="undefined mb-15"]/*[contains(@class,"Order")]'
    # счетчик "За сегодня"
    TODAY_COUNTER = By.XPATH, '//div[3]/p[contains(@class,"OrderFeed_number")]'
    # номер заказа "В работе"
    ORDER_IN_WORK = By.XPATH, "//ul[2]/*[@class='text text_type_digits-default mb-2']"
    # номер последнего заказа
    LAST_ORDER_USER_TEXT = By.XPATH, '//li[1]//p[contains(text(), "#")]'
