from selenium.common.exceptions import NoSuchElementException
from .locators import NoAfraidChangeLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage():
    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def close_popaps(self):  # Закрываем попапы
        # self.wait_element(*NoAfraidChangeLocators.popap1)
        # self.driver.find_element(*NoAfraidChangeLocators.popap1).click()
        self.driver.find_element(*NoAfraidChangeLocators.popap2).click()
        self.driver.find_element(*NoAfraidChangeLocators.popap3).click()


    def scroll_to_element(self, how, what): # Нужна доработка, ожидание не работает
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((how, what))))
        time.sleep(0.25)

    def wait_element(self, how, what):
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((how, what)))

    def js_input(self, value, how, what):
        self.driver.execute_script(f"arguments[0].value = '{value}';",self.driver.find_element(how, what))

    def js_click(self, how, what):
        self.driver.execute_script("arguments[0].click();",self.driver.find_element(how, what))

    def element_to_be_clickable(self, how, what):
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((how, what)))




