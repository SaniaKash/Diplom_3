from selenium.webdriver.common.by import By


class ForgotPassPageLocators:

    # поле ввода логина на странице "Забыли пароль"
    INPUT_EMAIL_FORGOT_PASS = By.XPATH, ".//input[@name = 'name']"
    # кнопка "Восстановить пароль"
    RECOVER_BUTT = By.XPATH, "//button[text()='Восстановить']"
