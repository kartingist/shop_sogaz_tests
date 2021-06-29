from .locators import *
from .base_page import BasePage
import time


class Step_1(BasePage):

    def step1(self):
        self.selenium_click(*OncologyStep1.program1)

    def go_to_next_step(self):
        self.selenium_click(*OncologyStep1.go_to_step_2)


class Step_2(BasePage):
    def should_be_step_2(self):
        assert self.is_element_present(*NoAfraidChangeLocators.surname), "Не выполнен переход на второй шаг"

    def input_full_anketa(self):
        # self.wait_element(*NoAfraidChangeLocators.step_2)
        # Заполнение первого блока личных данных
        # ____________________________________________________________________________________
        self.selenium_input('тестов', *Anketa.surname)
        self.selenium_input('тест', *Anketa.firstname)
        self.selenium_input('тестович', *Anketa.lastname)
        self.js_input('03081994', *Anketa.birthday)
        time.sleep(0.6)
        self.wait_element(*Anketa.phone)
        self.selenium_click(*Anketa.phone)
        self.selenium_input('9990403660', *Anketa.phone)
        self.selenium_input('awjon94@gmail.com', *Anketa.email)
        self.js_input('6420001900', *Anketa.passport)
        self.js_input('04092019', *Anketa.date_start)
        self.selenium_click(*NoAfraidChangeLocators.body)
        self.js_input('650002', *Anketa.division)
        self.selenium_input('Кем-то выдан', *Anketa.pass_who_give)

        # ____________________________________________________________________________________
        # self.scroll_to_element(*Anketa.person1)
        self.selenium_click(*Anketa.inp_address)
        self.selenium_input('Мос', *Anketa.city)
        self.selenium_click(*Anketa.select_city)
        self.selenium_input('Арсеньева', *Anketa.street)
        self.js_input('692502', *Anketa.index)
        self.selenium_input('33', *Anketa.home)
        self.selenium_input('1', *Anketa.korpus)
        self.selenium_input('2', *Anketa.building)
        self.selenium_input('60', *Anketa.flat)
        self.selenium_input('Уссурийск', *Anketa.birth_place)

# Застрахованное лицо
        self.scroll_to_element(*OncologyStep2.surname)
        self.selenium_input('тестов', *OncologyStep2.surname)
        self.selenium_input('тест', *OncologyStep2.firstname)
        self.selenium_input('тестович', *OncologyStep2.lastname)
        self.js_input('03081994', *OncologyStep2.birthday)
        self.selenium_click(*OncologyStep2.birthday)
        self.selenium_input('ENTER', *OncologyStep2.birthday)
        self.selenium_click(*OncologyStep2.body)
        self.selenium_click(*OncologyStep2.phone)
        self.wait_element(*OncologyStep2.phone)
        self.selenium_input('9990403660', *OncologyStep2.phone)
        self.js_input('6420001900', *OncologyStep2.passport)
        self.js_input('04092019', *OncologyStep2.date_start)
        self.selenium_click(*NoAfraidChangeLocators.body)
        self.js_input('650002', *OncologyStep2.division)
        self.selenium_input('Кем-то выдан', *OncologyStep2.pass_who_give)

        # Застрахованное лицо > Адрес места жительства (регистрации)
        # ____________________________________________________________________________________
        self.scroll_to_element(*OncologyStep2.inp_address)
        self.selenium_click(*OncologyStep2.inp_address)
        self.selenium_input('Мос', *OncologyStep2.city)
        self.selenium_click(*OncologyStep2.select_city)
        self.selenium_input('Арсеньева', *OncologyStep2.street)
        self.js_input('692502', *OncologyStep2.index)
        self.selenium_input('33', *OncologyStep2.home)
        self.selenium_input('1', *OncologyStep2.korpus)
        self.selenium_input('2', *OncologyStep2.building)
        self.selenium_input('60', *OncologyStep2.flat)

        self.scroll_to_element(*OncologyStep2.go_to_step_3)
        self.selenium_click(*OncologyStep2.go_to_step_3)

class Step_3(BasePage):
    def should_be_step_3(self):
        assert self.is_element_present(*NoAfraidChangeLocators.step3), "Не выполнен переход на третий шаг"
        self.wait_element(*NoAfraidChangeLocators.step3)
        self.scroll_to_element(*NoAfraidChangeLocators.get_code)
        self.wait_element(*NoAfraidChangeLocators.email_confirm)
        time.sleep(3)

    def get_input_code(self):
        self.selenium_click(*NoAfraidChangeLocators.get_code)
        self.wait_element(*NoAfraidChangeLocators.code)
        self.selenium_input(self.driver.find_element(*NoAfraidChangeLocators.code).text, *NoAfraidChangeLocators.codeConfirm)
        self.selenium_click(*NoAfraidChangeLocators.codeConfirmNext)
        time.sleep(1)
    def accept_checkbox(self):
        self.scroll_to_element(*NoAfraidChangeLocators.checkboxes)
        x = len(self.driver.find_elements(*NoAfraidChangeLocators.checkboxes))
        # Активируем
        for i in range(1, x+1):
            self.driver.execute_script(f"document.getElementById('check{i}').click()")
        self.selenium_click(*NoAfraidChangeLocators.step_to_pay)


class Pay_step(BasePage):

    def go_to_pay(self):

        self.wait_element(*NoAfraidChangeLocators.pan)
        assert self.is_element_present(*NoAfraidChangeLocators.pan), "Не выполнен переход на эквайринг'"
        self.js_input('9000000000000000001', *NoAfraidChangeLocators.pan)
        time.sleep(0.2)
        self.driver.find_element(*NoAfraidChangeLocators.month).send_keys('12')
        self.driver.find_element(*NoAfraidChangeLocators.year).send_keys('21')
        self.js_input('123', *NoAfraidChangeLocators.cvc)
        self.js_click(*NoAfraidChangeLocators.pay_button)

        self.wait_element(*NoAfraidChangeLocators.payment_info)
        success = self.driver.find_element(*NoAfraidChangeLocators.payment_info_message).text
        assert 'Операция выполнена успешно' == success, success


