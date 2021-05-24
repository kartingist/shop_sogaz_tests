from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
#    browser.set_window_size(375, 1080)
    yield driver
    print("\nquit browser..")

    driver.quit()


