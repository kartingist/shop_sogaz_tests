from selenium import webdriver
import pytest

def pytest_make_parametrize_id(val):
    return repr(val)

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()

    driver.set_window_size(1920, 1080)
#    browser.set_window_size(375, 1080)
    yield driver
    print("\nquit browser..")

    driver.quit()


