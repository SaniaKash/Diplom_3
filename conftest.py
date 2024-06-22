import pytest
from selenium import webdriver
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


