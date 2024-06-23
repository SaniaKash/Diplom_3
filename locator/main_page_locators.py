from selenium.webdriver.common.by import By


class MainPageLocators:

    # ГЛАВНАЯ СТРАНИЦА САЙТА
    # все картинке на главной странице сайта
    MAIN_PAGE_IMG = By.XPATH, "//img"
    # кнопка "войти в аккаунт" на главной странице
    PRIMARY_ENTER_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']"
    # кнопка "Личный кабинет" на главной странице
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//*[text()='Личный Кабинет']"
    # кнопка "Оформить заказ"
    MAKE_ORDER_BUTTON = By.XPATH, "//*[text()='Оформить заказ']"
    # кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = By.XPATH, '//*[text()="Конструктор"]'
    # кнопка "Лента заказов"
    ORDER_FEED_BUTTON = By.XPATH, '//*[text()="Лента Заказов"]'
    # ингредиент "Соус спайси"
    INGREDIENT_SOUSE_SPICY = By.XPATH, "//img[@alt = 'Соус Spicy-X']"
    # окно ингредиента "Соуса спайси"
    INGREDIENT_SOUSE_SPICY_DETAILS = By.XPATH, "//*[@class ='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"
    # кнопка закрыть окно ингредиента
    INGREDIENT_CLOSE_BUTTON = By.XPATH, "//section[1]//*[@type ='button']"
    # кнопка закрыть окно
    INGREDIENTS_WINDOW_CLOSED = By.XPATH, "//*[@class ='Modal_modal__P3_V5']"
    # счетчик "Соус спайси"
    INGREDIENT_SOUSE_SPICY_COUNTER = By.XPATH, "//*[@class ='counter_counter__num__3nue1'and text()='1']"
    # корзина конструктора
    BURGER_CONSTRUCTOR_BASKET = By.XPATH, '//*[text()="Перетяните булочку сюда (низ)"]'
    # окно "Заказ оформлен"
    DONE_ORDER_PAGE = By.XPATH, '//*[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]'
    # булка "Н200"
    N200_BUN = By.XPATH, '//*[text()="Краторная булка N-200i"]'
    # картинка заказа
    ORDER_IMG = By.XPATH, '//div[@class="Modal_modal__P3_V5"]'
    # номер заказа
    ORDER_NUMMER = By.XPATH, '//*[contains(@class,"title_shadow")]'




