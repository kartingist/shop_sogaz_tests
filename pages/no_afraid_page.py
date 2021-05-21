from .locators import NoAfraidChangeLocators
from .base_page import BasePage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import json
from link import link



class Step_1(BasePage):

    def select_program(self):
        self.driver.find_element(*NoAfraidChangeLocators.program).click()
    def go_to_next_step(self):
        self.driver.find_element(*NoAfraidChangeLocators.go_to_step_2).click()



class Step_2(BasePage):
    def should_be_step_2(self):
        assert self.is_element_present(*NoAfraidChangeLocators.surname), "form is not presented"

    def input_first_block_FIO(self):
        # Заполнение первого блока личных данных
        # ____________________________________________________________________________________
        self.driver.find_element(*NoAfraidChangeLocators.surname).send_keys('тестов')
        self.driver.find_element(*NoAfraidChangeLocators.firstname).send_keys('тест')
        self.driver.find_element(*NoAfraidChangeLocators.lastname).send_keys('тестович')
        self.driver.find_element(*NoAfraidChangeLocators.birthday).send_keys('03081994')
        self.driver.find_element(*NoAfraidChangeLocators.phone).click()
        self.driver.find_element(*NoAfraidChangeLocators.phone).send_keys('9990403660')
        self.driver.find_element(*NoAfraidChangeLocators.email).send_keys('awjon94@gmail.com')
        self.driver.find_element(*NoAfraidChangeLocators.passport).send_keys('6420001900')
        self.driver.find_element(*NoAfraidChangeLocators.date_start).send_keys('04092019')
        self.driver.find_element(*NoAfraidChangeLocators.body).click()
        self.driver.find_element(*NoAfraidChangeLocators.division).send_keys('650002')
        self.driver.find_element(*NoAfraidChangeLocators.pass_who_give).send_keys('Кем-то выдан')

        # Заполнение блока адреса регистрации
        # ____________________________________________________________________________________
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*NoAfraidChangeLocators.person1))
        self.scroll_to_element(*NoAfraidChangeLocators.person1)
        self.driver.find_element(*NoAfraidChangeLocators.inp_address).click()
        self.driver.find_element(*NoAfraidChangeLocators.city).send_keys('Мос')
        self.driver.find_element(*NoAfraidChangeLocators.select_city).click()
        self.driver.find_element(*NoAfraidChangeLocators.street).send_keys('Арсеньева')
        self.driver.find_element(*NoAfraidChangeLocators.index).send_keys('692502')
        self.driver.find_element(*NoAfraidChangeLocators.home).send_keys('33')
        self.driver.find_element(*NoAfraidChangeLocators.korpus).send_keys('1')
        self.driver.find_element(*NoAfraidChangeLocators.building).send_keys('2')
        self.driver.find_element(*NoAfraidChangeLocators.flat).send_keys('60')
        self.driver.find_element(*NoAfraidChangeLocators.birth_place).send_keys('Уссурийск')
        self.driver.find_element(*NoAfraidChangeLocators.personal_code).send_keys('12345678')
        self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
        self.driver.find_element(*NoAfraidChangeLocators.go_to_step_3).click()

class Step_3(BasePage):
    def should_be_step_3(self):
        assert self.is_element_present(*NoAfraidChangeLocators.item_iner_step_3), "form is not presented"
        self.wait_element(*NoAfraidChangeLocators.item_iner_step_3)
        time.sleep(0.5)
        self.scroll_to_element(*NoAfraidChangeLocators.get_code)
        self.wait_element(*NoAfraidChangeLocators.email_confirm)
        time.sleep(0.2)

    def get_input_code(self):

        self.driver.find_element(*NoAfraidChangeLocators.get_code).click()
        self.wait_element(*NoAfraidChangeLocators.code)
        self.driver.find_element(*NoAfraidChangeLocators.codeConfirm).send_keys(self.driver.find_element(*NoAfraidChangeLocators.code).text)
        self.driver.find_element(*NoAfraidChangeLocators.codeConfirmNext).click()
        time.sleep(1)
    def accept_checkbox(self):
        self.scroll_to_element(*NoAfraidChangeLocators.checkboxes)
        x = len(self.driver.find_elements(*NoAfraidChangeLocators.checkboxes))
        # Активируем
        for i in range(1, x+1):
            self.driver.execute_script(f"document.getElementById('check{i}').click()")
        self.driver.find_element(*NoAfraidChangeLocators.step_to_pay).click()

if link != "http://shop.sogaz.loc/" and link != 'http://sogazrelease.support.zetest.site/':
    class Pay_step(BasePage):
        def go_to_pay(self):
            self.wait_element(*NoAfraidChangeLocators.pan)
            # self.driver.find_element(*NoAfraidChangeLocators.pan).send_keys('9000000000000000001')
            time.sleep(0.2)
            self.driver.execute_script("arguments[0].value = '9000000000000000001';", self.driver.find_element(*NoAfraidChangeLocators.pan))
            # self.driver.execute_script("arguments[0].value = '12';", self.driver.find_element(*NoAfraidChangeLocators.month))
            self.driver.find_element(*NoAfraidChangeLocators.month).send_keys('12')
            # self.driver.execute_script("arguments[0].value = '24';", self.driver.find_element(*NoAfraidChangeLocators.year))
            self.driver.find_element(*NoAfraidChangeLocators.year).send_keys('21')
            self.driver.execute_script("arguments[0].value = '123';", self.driver.find_element(*NoAfraidChangeLocators.cvc))
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(*NoAfraidChangeLocators.pay_button))

            self.wait_element(*NoAfraidChangeLocators.payment_info)
            success = self.driver.find_element(*NoAfraidChangeLocators.payment_info_message).text
            assert 'Операция выполнена успешно' == success, success.text


