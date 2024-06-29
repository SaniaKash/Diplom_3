from selenium.webdriver.common.by import By


class PersonaAccountLocators:
    # кнопка выхода
    EXIT_BUTTON = By.XPATH, '//*[text()="Выход"]'
    # кнопка "История заказов"
    ORDER_HISTORY_BUTTON = By.XPATH, "//*[text()='История заказов']"
    # окно "История заказов"
    ORDER_HISTORY_PAGE = By.XPATH, '//*[contains(@class,"OrderHistory_orderHistory")]'
    # кнопка "Выйти" в "Личном кабинете"
    PERSONAL_ACCOUNT_EXIT_BUTTON = By.XPATH, "//*[text()='Выход']"
    # счетчик
    MAIN_PAGE_COUNTER = By.XPATH, '//h2[contains(@class,"title_shadow")]'
    # номер последнего заказа
    LAST_ORDER_NUMMER = By.XPATH, '//li[last()]//p[contains(text(), "#")]'
