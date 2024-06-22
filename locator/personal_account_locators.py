from selenium.webdriver.common.by import By


class PersonaAccountLocators:

    EXIT_BUTTON = By.XPATH, '//*[text()="Выход"]'
    ORDER_HISTORY_BUTTON = By.XPATH, "//*[text()='История заказов']"
    ORDER_HISTORY_PAGE = By.XPATH, '//*[contains(@class,"OrderHistory_orderHistory")]'
    PERSONAL_ACCOUNT_EXIT_BUTTON = By.XPATH, "//*[text()='Выход']"
    MAIN_PAGE_COUNTER = By.XPATH, '//h2[contains(@class,"title_shadow")]'
