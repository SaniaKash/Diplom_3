from seletools.actions import drag_and_drop
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # Ожидание отображения элемента
    def visibility_of_element_located(self, locator):  # Ожидание отображения элемента
        return WebDriverWait(self.driver, 100).until(expected_conditions.visibility_of_element_located(locator))

    def move_to(self, locator):
        element = self.visibility_of_element_located(locator)
        action = ActionChains(self.driver)
        return action.move_to_element(element).click().perform()

    # Ожидание кликабельности элемента
    def clickable_of_element_located(self, locator):
        return WebDriverWait(self.driver, 100).until(expected_conditions.element_to_be_clickable(locator))

    # Клик элемента
    def click_element(self, locator):  # Клик на элемент
        element = self.clickable_of_element_located(locator)
        return element.click()

    # Проверка отображения элемента
    def check_element_displayed(self, locator):
        return self.presence_of_element_detected(locator).is_displayed()

    # Отправить значение в поля
    def input_text(self, locator, text):
        element = self.visibility_of_element_located(locator)
        element.clear()
        return element.send_keys(text)

    def current_url(self):
        return self.driver.current_url

    def visibility_of_url_located(self, url):
        return WebDriverWait(self.driver, 100).until(expected_conditions.url_to_be(url))

    def presence_of_element_detected(self, locator):
        return WebDriverWait(self.driver, 100).until(expected_conditions.presence_of_element_located(locator))

    def seletools_drag_and_drop_element(self, locator1, locator2):
        source = self.visibility_of_element_located(locator1)
        target = self.presence_of_element_detected(locator2)
        return drag_and_drop(self.driver, source, target)

    def get_text(self, locator):
        return self.presence_of_element_detected(locator).text

    # Скролл страницы до элемента
    def execute_script(self, locator):
        element = self.visibility_of_element_located(locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)




