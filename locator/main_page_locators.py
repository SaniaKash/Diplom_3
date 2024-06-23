from selenium.webdriver.common.by import By


class MainPageLocators:

    # ГЛАВНАЯ СТРАНИЦА САЙТА
    # все картинке на главной странице сайта
    MAIN_PAGE_IMG = By.XPATH, "//img"
    # кнопка "войти в аккаунт" на главной странице
    PRIMARY_ENTER_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']"
    # кнопка "Личный кабинет" на главной странице
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//*[text()='Личный Кабинет']"
    MAKE_ORDER_BUTTON = By.XPATH, "//*[text()='Оформить заказ']"
    CONSTRUCTOR_BUTTON = By.XPATH, '//*[text()="Конструктор"]'
    ORDER_FEED_BUTTON = By.XPATH, '//*[text()="Лента Заказов"]'
    INGREDIENT_SOUSE_SPICY = By.XPATH, "//img[@alt = 'Соус Spicy-X']"
    INGREDIENT_SOUSE_SPICY_DETAILS = By.XPATH, "//*[@class ='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"
    INGREDIENT_CLOSE_BUTTON = By.XPATH, "//section[1]//*[@type ='button']"
    INGREDIENTS_WINDOW_CLOSED = By.XPATH, "//*[@class ='Modal_modal__P3_V5']"
    INGREDIENT_SOUSE_SPICY_COUNTER = By.XPATH, "//*[@class ='counter_counter__num__3nue1'and text()='1']"
    BURGER_CONSTRUCTOR_BASKET = By.XPATH, '//*[text()="Перетяните булочку сюда (низ)"]'
    DONE_ORDER_PAGE = By.XPATH, '//*[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]'
    N200_BUN = By.XPATH, '//*[text()="Краторная булка N-200i"]'
    ORDER_IMG = By.XPATH, '//div[@class="Modal_modal__P3_V5"]'
    ORDER_NUMMER = By.XPATH, '//*[contains(@class,"title_shadow")]'




