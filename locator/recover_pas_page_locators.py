from selenium.webdriver.common.by import By


class RecPassPageLocator:

    SAVE_BUTTON = By.XPATH, "//button[text()='Сохранить']"
    # поле ввода пароля на странице входа
    RECOVER_PASSWORD_FIELD = By.XPATH, ".//input[@name = 'Введите новый пароль']"
    INPUT_ICON = By.XPATH, '//*[@class="input__icon input__icon-action"]/*'
    PASSWORD_FIELD_FOCUSED = By.XPATH, '//input[@type="text"]/following-sibling::div'
