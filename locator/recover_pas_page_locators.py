from selenium.webdriver.common.by import By


class RecPassPageLocator:
    # кнопка "Сохранить"
    SAVE_BUTTON = By.XPATH, "//button[text()='Сохранить']"
    # поле ввода пароля на странице входа
    RECOVER_PASSWORD_FIELD = By.XPATH, ".//input[@name = 'Введите новый пароль']"
    # кнопка скрыть
    INPUT_ICON = By.XPATH, '//*[@class="input__icon input__icon-action"]/*'
    # активное поля пароля
    PASSWORD_FIELD_FOCUSED = By.XPATH, '//input[@type="text"]/following-sibling::div'
