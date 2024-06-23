from selenium.webdriver.common.by import By


class ForgotPassPageLocators:

    # поле ввода логина на странице входа
    INPUT_EMAIL = By.XPATH, ".//input[@name = 'name']"
    # кнопка "Восстановить пароль"
    RECOVER_BUTT = By.XPATH, "//button[text()='Восстановить']"
