from selenium.webdriver.common.by import By


class EnterPageLocators:
    # СТРАНИЦА ВХОДА
    # ссылка "Восстановить пароль" на странице входа
    FORGOT_PASSWORD = By.XPATH, "//a[text()='Восстановить пароль']"
    # поле ввода логина на странице входа
    INPUT_EMAIL = (By.XPATH, ".//input[@name = 'name']")
    # поле ввода пароля на странице входа
    INPUT_PASSWORD = (By.XPATH, ".//input[@name = 'Пароль']")
    # кнопка "Войти" на странице входа
    ENTER_BUTTON = (By.XPATH, "//button[text() = 'Войти']")
