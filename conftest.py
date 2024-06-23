import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.enter_page import EnterPage
from data import UserData


def _get_driver(name):
    if name == 'chrome':
        return webdriver.Chrome()
    elif name == 'firefox':
        return webdriver.Firefox()
    else:
        raise TypeError


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = _get_driver(request.param)
    driver.get(UserData.MAIN_PAGE_BURGER_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def popup(driver):
    user = MainPage(driver)
    user.wait_for_main_page_located()
    user.click_personal_account_button()
    user = EnterPage(driver)
    user.input_email_text()
    user.input_password_text()
    user.click_enter_button()
    user = MainPage(driver)
    user.wait_for_personal_account_button_located()


