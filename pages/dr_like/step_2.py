from .locators import *
from ..base_page import BasePage
from ..base_locators import Common_Locators
import time
from datetime import date
from dateutil.relativedelta import relativedelta
import random

email=[f'user{str(random.randint(90000, 99999))}@gmail.com']

class Step_2(BasePage):
    def should_be_step_2(self):
        assert self.is_element_present(*DrLikeLocators.surname0), "Не выполнен переход на второй шаг"

    def input_full_anketa(self):
        self.wait_element(*DrLikeLocators.step_2)

        # ____________________________________________________________________________________
        # Страхователь
        self.selenium_input('тестов', *DrLikeLocators.surname0)
        self.selenium_input('тест', *DrLikeLocators.firstname0)
        self.selenium_input('тестович', *DrLikeLocators.lastname0)
        self.js_input('03081994', *DrLikeLocators.birthday0)
        time.sleep(0.6)
        self.wait_element(*DrLikeLocators.phone0)
        self.selenium_click(*DrLikeLocators.phone0)
        self.selenium_input('9990403660', *DrLikeLocators.phone0)
        self.selenium_input('awjon94@gmail.com', *DrLikeLocators.email)
        self.js_input('6420001900', *DrLikeLocators.pass0)
        self.js_input('04092019', *DrLikeLocators.date_start0)
        self.selenium_click(*Common_Locators.body)
        self.js_input('650002', *DrLikeLocators.division0)
        self.selenium_input('Кем-то выдан', *DrLikeLocators.pass_who_give0)

        # Адрес регистрации страхователя
        # ____________________________________________________________________________________

        self.scroll_to_element(*DrLikeLocators.inp_address0)
        self.input_city('Мос', *DrLikeLocators.inp_address0)
        self.selenium_input('Арсеньева', *DrLikeLocators.street0)
        self.js_input('692502', *DrLikeLocators.index0)
        self.selenium_input('33', *DrLikeLocators.house0)
        self.selenium_input('1', *DrLikeLocators.korpus0)
        self.selenium_input('2', *DrLikeLocators.building0)
        self.selenium_input('60', *DrLikeLocators.flat0)
        self.selenium_input('Уссурийск', *DrLikeLocators.birth_place0)

        # Адрес фактического места жительства страхователя

        self.scroll_to_element(*DrLikeLocators.inp_address02)
        self.input_city('Мос', *DrLikeLocators.inp_address02)
        self.selenium_input('Арсеньева', *DrLikeLocators.street02)
        self.js_input('692502', *DrLikeLocators.index02)
        self.selenium_input('33', *DrLikeLocators.house02)
        self.selenium_input('1', *DrLikeLocators.korpus02)
        self.selenium_input('2', *DrLikeLocators.building02)
        self.selenium_input('60', *DrLikeLocators.flat02)

        # Застрахованный

        self.scroll_to_element(*DrLikeLocators.surname1)
        self.selenium_input('тестов', *DrLikeLocators.surname1)
        self.selenium_input('тест', *DrLikeLocators.firstname1)
        self.selenium_input('тестович', *DrLikeLocators.lastname1)
        # self.js_input('03081994', *DrLikeLocators.birthday1)
        time.sleep(0.6)
        self.wait_element(*DrLikeLocators.phone1)
        self.selenium_click(*DrLikeLocators.phone1)
        self.selenium_input('9990403660', *DrLikeLocators.phone1)
        self.selenium_input('awjon94@gmail.com', *DrLikeLocators.email1)
        self.js_input('6420001900', *DrLikeLocators.pass1)
        self.js_input('04092019', *DrLikeLocators.date_start1)
        self.selenium_click(*Common_Locators.body)
        self.js_input('650002', *DrLikeLocators.division1)
        self.selenium_input('Кем-то выдан', *DrLikeLocators.pass_who_give1)

        # Адрес регистрации застрахованного

        self.scroll_to_element(*DrLikeLocators.inp_address1)
        self.input_city('Мос', *DrLikeLocators.inp_address1)
        self.selenium_input('Арсеньева', *DrLikeLocators.street1)
        self.js_input('692502', *DrLikeLocators.index1)
        self.selenium_input('33', *DrLikeLocators.house1)
        self.selenium_input('1', *DrLikeLocators.korpus1)
        self.selenium_input('2', *DrLikeLocators.building1)
        self.selenium_input('60', *DrLikeLocators.flat1)
        self.selenium_input('Уссурийск', *DrLikeLocators.birth_place1)

        # Адрес фактического места жительства застрахованного

        self.scroll_to_element(*DrLikeLocators.inp_address12)
        self.input_city('Мос', *DrLikeLocators.inp_address12)
        self.selenium_input('Арсеньева', *DrLikeLocators.street12)
        self.js_input('692502', *DrLikeLocators.index12)
        self.selenium_input('33', *DrLikeLocators.house12)
        self.selenium_input('1', *DrLikeLocators.korpus12)
        self.selenium_input('2', *DrLikeLocators.building12)
        self.selenium_input('60', *DrLikeLocators.flat12)

        self.scroll_to_element(*DrLikeLocators.go_to_step_3)
        self.selenium_click(*DrLikeLocators.go_to_step_3)
# # _________________________________________________________________________________________________________
    def anketa_min_data(self):

        self.wait_element(*DrLikeLocators.step_2)
        # ____________________________________________________________________________________
        # Страхователь
        self.selenium_input('Тест', *DrLikeLocators.surname0)
        self.selenium_input('Тест', *DrLikeLocators.firstname0)
        self.js_input('03081994', *DrLikeLocators.birthday0)
        time.sleep(0.6)
        self.wait_element(*DrLikeLocators.phone0)
        self.selenium_click(*DrLikeLocators.phone0)
        self.selenium_input('9990403660', *DrLikeLocators.phone0)
        self.selenium_input('awjon94@gmail.com', *DrLikeLocators.email)
        self.js_input('6420001900', *DrLikeLocators.pass0)
        self.js_input('04092019', *DrLikeLocators.date_start0)
        self.selenium_click(*Common_Locators.body)
        self.js_input('650002', *DrLikeLocators.division0)
        self.selenium_input('Тест', *DrLikeLocators.pass_who_give0)

        # Адрес регистрации страхователя
        # ____________________________________________________________________________________

        self.scroll_to_element(*DrLikeLocators.inp_address0)
        self.input_city('Мос', *DrLikeLocators.inp_address0)
        self.selenium_input('Тест', *DrLikeLocators.street0)
        self.selenium_input('33', *DrLikeLocators.house0)
        self.selenium_input('Уссурийск', *DrLikeLocators.birth_place0)

        # Адрес фактического места жительства страхователя
        self.selenium_click(*DrLikeLocators.checkbox1)

        # Застрахованный

        self.scroll_to_element(*DrLikeLocators.surname1)
        self.selenium_input('Тест', *DrLikeLocators.surname1)
        self.selenium_input('Тест', *DrLikeLocators.firstname1)
        # self.js_input('03081994', *DrLikeLocators.birthday1)
        time.sleep(0.6)
        self.wait_element(*DrLikeLocators.phone1)
        self.selenium_click(*DrLikeLocators.phone1)
        self.selenium_input('9990403660', *DrLikeLocators.phone1)
        self.selenium_input('awjon94@gmail.com', *DrLikeLocators.email1)
        self.js_input('6420001900', *DrLikeLocators.pass1)
        self.js_input('04092019', *DrLikeLocators.date_start1)
        self.selenium_click(*Common_Locators.body)
        self.js_input('650002', *DrLikeLocators.division1)
        self.selenium_input('Тест', *DrLikeLocators.pass_who_give1)

        # Адрес регистрации застрахованного

        self.scroll_to_element(*DrLikeLocators.inp_address1)
        self.input_city('Мос', *DrLikeLocators.inp_address1)
        self.selenium_input('Тест', *DrLikeLocators.street1)
        self.selenium_input('33', *DrLikeLocators.house1)
        self.selenium_input('Уссурийск', *DrLikeLocators.birth_place1)

        # Адрес фактического места жительства застрахованного
        self.selenium_click(*DrLikeLocators.checkbox2)

        self.scroll_to_element(*DrLikeLocators.go_to_step_3)
        self.selenium_click(*DrLikeLocators.go_to_step_3)

    def anketa_fio_whogiveandstreet(self, fio, whogiveandstreet):
        self.wait_element(*DrLikeLocators.step_2)

        # ____________________________________________________________________________________
        # Страхователь
        self.selenium_input(fio, *DrLikeLocators.surname0)
        self.selenium_input(fio, *DrLikeLocators.firstname0)
        self.selenium_input(fio, *DrLikeLocators.lastname0)
        self.js_input('03081994', *DrLikeLocators.birthday0)
        time.sleep(0.6)
        self.wait_element(*DrLikeLocators.phone0)
        self.selenium_click(*DrLikeLocators.phone0)
        self.selenium_input('9990403660', *DrLikeLocators.phone0)
        self.selenium_input('awjon94@gmail.com', *DrLikeLocators.email)
        self.js_input('6420001900', *DrLikeLocators.pass0)
        self.js_input('04092019', *DrLikeLocators.date_start0)
        self.selenium_click(*Common_Locators.body)
        self.js_input('650002', *DrLikeLocators.division0)
        self.selenium_input(whogiveandstreet, *DrLikeLocators.pass_who_give0)

        # Адрес регистрации страхователя
        # ____________________________________________________________________________________

        self.scroll_to_element(*DrLikeLocators.inp_address0)
        self.input_city('Мос', *DrLikeLocators.inp_address0)
        self.selenium_input(whogiveandstreet, *DrLikeLocators.street0)
        self.selenium_input('33', *DrLikeLocators.house0)
        self.selenium_input('Уссурийск', *DrLikeLocators.birth_place0)

        # Адрес фактического места жительства страхователя

        self.scroll_to_element(*DrLikeLocators.inp_address02)
        self.input_city('Мос', *DrLikeLocators.inp_address02)
        self.selenium_input(whogiveandstreet, *DrLikeLocators.street02)
        self.selenium_input('33', *DrLikeLocators.house02)

        # Застрахованный

        self.scroll_to_element(*DrLikeLocators.surname1)
        self.selenium_input(fio, *DrLikeLocators.surname1)
        self.selenium_input(fio, *DrLikeLocators.firstname1)
        self.selenium_input(fio, *DrLikeLocators.lastname1)
        # self.js_input('03081994', *DrLikeLocators.birthday1)
        time.sleep(0.6)
        self.wait_element(*DrLikeLocators.phone1)
        self.selenium_click(*DrLikeLocators.phone1)
        self.selenium_input('9990403660', *DrLikeLocators.phone1)
        self.selenium_input('awjon94@gmail.com', *DrLikeLocators.email1)
        self.js_input('6420001900', *DrLikeLocators.pass1)
        self.js_input('04092019', *DrLikeLocators.date_start1)
        self.selenium_click(*Common_Locators.body)
        self.js_input('650002', *DrLikeLocators.division1)
        self.selenium_input(whogiveandstreet, *DrLikeLocators.pass_who_give1)

        # Адрес регистрации застрахованного

        self.scroll_to_element(*DrLikeLocators.inp_address1)
        self.input_city('Мос', *DrLikeLocators.inp_address1)
        self.selenium_input(whogiveandstreet, *DrLikeLocators.street1)
        self.selenium_input('33', *DrLikeLocators.house1)
        self.selenium_input('Уссурийск', *DrLikeLocators.birth_place1)

        # Адрес фактического места жительства застрахованного

        self.scroll_to_element(*DrLikeLocators.inp_address12)
        self.input_city('Мос', *DrLikeLocators.inp_address12)
        self.selenium_input(whogiveandstreet, *DrLikeLocators.street12)
        self.selenium_input('33', *DrLikeLocators.house12)

        self.scroll_to_element(*DrLikeLocators.go_to_step_3)
        self.selenium_click(*DrLikeLocators.go_to_step_3)
#
    def anketa_null_fields_errors(self):
        self.wait_element(*DrLikeLocators.surname0)
        self.js_click(*DrLikeLocators.go_to_step_3)
        self.wait_element(*DrLikeLocators.surname0_error)
        # _________________________________________________________________________
        # Страхователь
        self.check_errors(*DrLikeLocators.surname0_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.firstname0_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.birthday0_error, 'Обязательное поле')
        # self.check_errors(*DrLikeLocators.phone0_error, 'Ошибка заполнения') #общая ошибка связанная с количеством персон больше одной
        self.check_errors(*DrLikeLocators.email_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.pass0_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.date_start0_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.division0_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.pass_who_give0_error, 'Обязательное поле')

        self.check_errors(*DrLikeLocators.inp_address0_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.street0_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.house0_error, 'Обязательное поле')

        self.check_errors(*DrLikeLocators.inp_address02_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.street02_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.house02_error, 'Обязательное поле')
        # _________________________________________________________________________
        # Застрахованный
        self.check_errors(*DrLikeLocators.surname1_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.firstname1_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.phone1_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.email1_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.pass1_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.date_start1_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.division1_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.pass_who_give0_error, 'Обязательное поле')

        self.check_errors(*DrLikeLocators.inp_address1_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.street1_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.house1_error, 'Обязательное поле')

        self.check_errors(*DrLikeLocators.inp_address12_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.street12_error, 'Обязательное поле')
        self.check_errors(*DrLikeLocators.house12_error, 'Обязательное поле')

    def anketa_validation_errors(self):
        self.wait_element(*DrLikeLocators.step_2)

        # ____________________________________________________________________________________
        # Страхователь
        self.selenium_input('testfio', *DrLikeLocators.surname0)
        self.selenium_input('testfio', *DrLikeLocators.firstname0)
        self.selenium_input('testfio', *DrLikeLocators.lastname0)
        self.js_input('030819', *DrLikeLocators.birthday0)
        time.sleep(0.6)
        self.wait_element(*DrLikeLocators.phone0)
        self.selenium_click(*DrLikeLocators.phone0)
        self.selenium_input('99904036', *DrLikeLocators.phone0)
        self.selenium_input('awjon94@', *DrLikeLocators.email)
        self.js_input('6420001', *DrLikeLocators.pass0)
        self.js_input('040920', *DrLikeLocators.date_start0)
        self.selenium_click(*Common_Locators.body)
        self.js_input('6500', *DrLikeLocators.division0)
        self.selenium_input('test', *DrLikeLocators.pass_who_give0)

        # Адрес регистрации страхователя
        # ____________________________________________________________________________________

        self.scroll_to_element(*DrLikeLocators.inp_address0)
        self.input_city('Мос', *DrLikeLocators.inp_address0)
        self.selenium_input('test', *DrLikeLocators.street0)
        self.js_input('6925', *DrLikeLocators.index0)
        self.selenium_input('testfio', *DrLikeLocators.house0)
        self.selenium_input('testfio', *DrLikeLocators.korpus0)
        self.selenium_input('testfio', *DrLikeLocators.building0)
        self.selenium_input('testfio', *DrLikeLocators.flat0)
        self.selenium_input('testfio', *DrLikeLocators.birth_place0)

        # Адрес фактического места жительства страхователя

        self.scroll_to_element(*DrLikeLocators.inp_address02)
        self.input_city('Мос', *DrLikeLocators.inp_address02)
        self.selenium_input('test', *DrLikeLocators.street02)
        self.js_input('6925', *DrLikeLocators.index02)
        self.selenium_input('testfio', *DrLikeLocators.house02)
        self.selenium_input('testfio', *DrLikeLocators.korpus02)
        self.selenium_input('testfio', *DrLikeLocators.building02)
        self.selenium_input('testfio', *DrLikeLocators.flat02)

        # Застрахованный

        self.scroll_to_element(*DrLikeLocators.surname1)
        self.selenium_input('testfio', *DrLikeLocators.surname1)
        self.selenium_input('testfio', *DrLikeLocators.firstname1)
        self.selenium_input('testfio', *DrLikeLocators.lastname1)
        # self.js_input('03081994', *DrLikeLocators.birthday1)
        time.sleep(0.6)
        self.wait_element(*DrLikeLocators.phone1)
        self.selenium_click(*DrLikeLocators.phone1)
        self.selenium_input('99904036', *DrLikeLocators.phone1)
        self.selenium_input('awjon94@', *DrLikeLocators.email1)
        self.js_input('6420001', *DrLikeLocators.pass1)
        self.js_input('040920', *DrLikeLocators.date_start1)
        self.selenium_click(*Common_Locators.body)
        self.js_input('6500', *DrLikeLocators.division1)
        self.selenium_input('test', *DrLikeLocators.pass_who_give1)

        # Адрес регистрации застрахованного

        self.scroll_to_element(*DrLikeLocators.inp_address1)
        self.input_city('Мос', *DrLikeLocators.inp_address1)
        self.selenium_input('test', *DrLikeLocators.street1)
        self.js_input('6925', *DrLikeLocators.index1)
        self.selenium_input('testfio', *DrLikeLocators.house1)
        self.selenium_input('testfio', *DrLikeLocators.korpus1)
        self.selenium_input('testfio', *DrLikeLocators.building1)
        self.selenium_input('testfio', *DrLikeLocators.flat1)
        self.selenium_input('testfio', *DrLikeLocators.birth_place1)

        # Адрес фактического места жительства застрахованного

        self.scroll_to_element(*DrLikeLocators.inp_address12)
        self.input_city('Мос', *DrLikeLocators.inp_address12)
        self.selenium_input('test', *DrLikeLocators.street12)
        self.js_input('6925', *DrLikeLocators.index12)
        self.selenium_input('testfio', *DrLikeLocators.house12)
        self.selenium_input('testfio', *DrLikeLocators.korpus12)
        self.selenium_input('testfio', *DrLikeLocators.building12)
        self.selenium_input('testfio', *DrLikeLocators.flat12)

        self.scroll_to_element(*DrLikeLocators.go_to_step_3)
        self.selenium_click(*DrLikeLocators.go_to_step_3)
#
        self.wait_element(*DrLikeLocators.surname0_error)
# #   Проверка ошибок
        self.check_errors(*DrLikeLocators.surname0_error, 'Допустимы кирилические символы')
        self.check_errors(*DrLikeLocators.firstname0_error, 'Допустимы кирилические символы')
        self.check_errors(*DrLikeLocators.lastname0_error, 'Допустимы кирилические символы')
        # self.check_errors(*DrLikeLocators.birthday0_error, 'Неверный формат даты') #поле обнуляется при неполном вводе
        self.check_errors(*DrLikeLocators.phone0_error, 'Ошибка заполнения')
        self.check_errors(*DrLikeLocators.email_error, 'Неверный формат почты')
        self.check_errors(*DrLikeLocators.pass0_error, 'Ошибка заполнения')
        self.check_errors(*DrLikeLocators.division0_error, 'Ошибка заполнения')
        self.check_errors(*DrLikeLocators.pass_who_give0_error, 'Допустимы кирилические символы')
        self.check_errors(*DrLikeLocators.street0_error, 'Допустимы кирилические символы')
        self.check_errors(*DrLikeLocators.index0_error, 'Ошибка заполнения')

        self.check_errors(*DrLikeLocators.street02_error, 'Допустимы кирилические символы')
        self.check_errors(*DrLikeLocators.index02_error, 'Ошибка заполнения')

        self.check_errors(*DrLikeLocators.surname1_error, 'Допустимы кирилические символы')
        self.check_errors(*DrLikeLocators.firstname1_error, 'Допустимы кирилические символы')
        self.check_errors(*DrLikeLocators.lastname1_error, 'Допустимы кирилические символы')
        self.check_errors(*DrLikeLocators.phone1_error, 'Ошибка заполнения')
        self.check_errors(*DrLikeLocators.email1_error, 'Неверный формат почты')
        self.check_errors(*DrLikeLocators.pass1_error, 'Ошибка заполнения')
        self.check_errors(*DrLikeLocators.division1_error, 'Ошибка заполнения')
        self.check_errors(*DrLikeLocators.pass_who_give1_error, 'Допустимы кирилические символы')
        self.check_errors(*DrLikeLocators.street1_error, 'Допустимы кирилические символы')
        self.check_errors(*DrLikeLocators.index1_error, 'Ошибка заполнения')

        self.check_errors(*DrLikeLocators.street12_error, 'Допустимы кирилические символы')
        self.check_errors(*DrLikeLocators.index12_error, 'Ошибка заполнения')

    def fio_validation_negative(self, testfio, textfields):
        self.wait_element(*DrLikeLocators.step_2)

        # ____________________________________________________________________________________
        # Страхователь
        self.selenium_input(testfio, *DrLikeLocators.surname0)
        self.selenium_input(testfio, *DrLikeLocators.firstname0)
        self.selenium_input(testfio, *DrLikeLocators.lastname0)
        # Адрес регистрации страхователя
        # ____________________________________________________________________________________

        self.scroll_to_element(*DrLikeLocators.inp_address0)
        self.selenium_input(textfields, *DrLikeLocators.house0)
        self.selenium_input(textfields, *DrLikeLocators.korpus0)
        self.selenium_input(textfields, *DrLikeLocators.building0)
        self.selenium_input(textfields, *DrLikeLocators.flat0)
        self.selenium_input(textfields, *DrLikeLocators.birth_place0)

        # Адрес фактического места жительства страхователя
        self.scroll_to_element(*DrLikeLocators.inp_address02)
        self.selenium_input(textfields, *DrLikeLocators.house02)
        self.selenium_input(textfields, *DrLikeLocators.korpus02)
        self.selenium_input(textfields, *DrLikeLocators.building02)
        self.selenium_input(textfields, *DrLikeLocators.flat02)

        # Застрахованный

        self.scroll_to_element(*DrLikeLocators.surname1)
        self.selenium_input(testfio, *DrLikeLocators.surname1)
        self.selenium_input(testfio, *DrLikeLocators.firstname1)
        self.selenium_input(testfio, *DrLikeLocators.lastname1)

        # Адрес регистрации застрахованного
        self.scroll_to_element(*DrLikeLocators.inp_address1)
        self.selenium_input(textfields, *DrLikeLocators.house1)
        self.selenium_input(textfields, *DrLikeLocators.korpus1)
        self.selenium_input(textfields, *DrLikeLocators.building1)
        self.selenium_input(textfields, *DrLikeLocators.flat1)
        self.selenium_input(textfields, *DrLikeLocators.birth_place1)

        # Адрес фактического места жительства застрахованного

        self.scroll_to_element(*DrLikeLocators.inp_address12)
        self.selenium_input(textfields, *DrLikeLocators.house12)
        self.selenium_input(textfields, *DrLikeLocators.korpus12)
        self.selenium_input(textfields, *DrLikeLocators.building12)
        self.selenium_input(textfields, *DrLikeLocators.flat12)

        self.scroll_to_element(*DrLikeLocators.go_to_step_3)
        self.selenium_click(*DrLikeLocators.go_to_step_3)
        #
        self.wait_element(*DrLikeLocators.surname0_error)
        # #   Проверка ошибок
        self.check_errors(*DrLikeLocators.surname0_error, 'Допустимы кирилические символы')
        self.check_errors(*DrLikeLocators.firstname0_error, 'Допустимы кирилические символы')
        self.check_errors(*DrLikeLocators.lastname0_error, 'Допустимы кирилические символы')

        self.check_errors(*DrLikeLocators.surname1_error, 'Допустимы кирилические символы')
        self.check_errors(*DrLikeLocators.firstname1_error, 'Допустимы кирилические символы')
        self.check_errors(*DrLikeLocators.lastname1_error, 'Допустимы кирилические символы')



    def pass_date_start_negative(self, birth_day, days):
        self.js_input((date.today() - relativedelta
        (years=birth_day+1)).strftime('%d%m%Y'), *DrLikeLocators.birthday0)

        self.js_input((date.today() + relativedelta
        (years=-1, days=days)).strftime('%d%m%Y'), *DrLikeLocators.date_start0)

        self.js_click(*DrLikeLocators.go_to_step_3)
        self.should_be(*DrLikeLocators.date_start0_error)
        if birth_day == 14:
            self.check_errors(*DrLikeLocators.date_start0_error,
                'Дата выдачи паспорта некорректна: '
                'паспорт не может быть выдан ранее 14-ти лет с даты рождения')
        elif birth_day <= 0 or (birth_day == 20 and  days== 370):
            self.check_errors(*DrLikeLocators.date_start0_error,
                'Дата больше текущей')

        else:
            self.check_errors(*DrLikeLocators.date_start0_error,
                              'Дата выдачи паспорта некорректна: '
                              'срок действия указанного паспорта истек')



    def pass_date_start_positive(self, birth_day, days):
        self.wait_element(*DrLikeLocators.step_2)
        # ____________________________________________________________________________________
        # Страхователь
        self.selenium_input('Тест', *DrLikeLocators.surname0)
        self.selenium_input('Тест', *DrLikeLocators.firstname0)
        self.js_input((date.today() - relativedelta(years=birth_day+1)).strftime('%d%m%Y'), *DrLikeLocators.birthday0)
        time.sleep(0.6)
        self.wait_element(*DrLikeLocators.phone0)
        self.selenium_click(*DrLikeLocators.phone0)
        self.selenium_input('9990403660', *DrLikeLocators.phone0)
        self.selenium_input('awjon94@gmail.com', *DrLikeLocators.email)
        self.js_input('6420001900', *DrLikeLocators.pass0)
        self.js_input((date.today() + relativedelta(years=-1, days=days)).strftime('%d%m%Y'),
                      *DrLikeLocators.date_start0)
        self.selenium_click(*Common_Locators.body)
        self.js_input('650002', *DrLikeLocators.division0)
        self.selenium_input('Тест', *DrLikeLocators.pass_who_give0)

        # Адрес регистрации страхователя
        # ____________________________________________________________________________________

        self.scroll_to_element(*DrLikeLocators.inp_address0)
        self.input_city('Мос', *DrLikeLocators.inp_address0)
        self.selenium_input('Тест', *DrLikeLocators.street0)
        self.selenium_input('33', *DrLikeLocators.house0)
        self.selenium_input('Уссурийск', *DrLikeLocators.birth_place0)

        # Адрес фактического места жительства страхователя
        self.selenium_click(*DrLikeLocators.checkbox1)

        # Застрахованный

        self.scroll_to_element(*DrLikeLocators.surname1)
        self.selenium_input('Тест', *DrLikeLocators.surname1)
        self.selenium_input('Тест', *DrLikeLocators.firstname1)
        # self.js_input('03081994', *DrLikeLocators.birthday1)
        time.sleep(0.6)
        self.wait_element(*DrLikeLocators.phone1)
        self.selenium_click(*DrLikeLocators.phone1)
        self.selenium_input('9990403660', *DrLikeLocators.phone1)
        self.selenium_input('awjon94@gmail.com', *DrLikeLocators.email1)
        self.js_input('6420001900', *DrLikeLocators.pass1)
        self.js_input('04092019', *DrLikeLocators.date_start1)
        self.selenium_click(*Common_Locators.body)
        self.js_input('650002', *DrLikeLocators.division1)
        self.selenium_input('Тест', *DrLikeLocators.pass_who_give1)

        # Адрес регистрации застрахованного

        self.scroll_to_element(*DrLikeLocators.inp_address1)
        self.input_city('Мос', *DrLikeLocators.inp_address1)
        self.selenium_input('Тест', *DrLikeLocators.street1)
        self.selenium_input('33', *DrLikeLocators.house1)
        self.selenium_input('Уссурийск', *DrLikeLocators.birth_place1)

        # Адрес фактического места жительства застрахованного
        self.selenium_click(*DrLikeLocators.checkbox2)

        self.scroll_to_element(*DrLikeLocators.go_to_step_3)
        self.selenium_click(*DrLikeLocators.go_to_step_3)
# #     ____________________________________________________________________________________________________________
#
#     def age_check(self, age, sex):
#         self.wait_element(*NoAfraidChangeLocators.step_2)
#         # Заполнение первого блока личных данных
#         # ____________________________________________________________________________________
#         self.selenium_input('тестов', *NoAfraidChangeLocators.surname)
#         self.selenium_input('тест', *NoAfraidChangeLocators.firstname)
#         self.selenium_input('тестович', *NoAfraidChangeLocators.lastname)
#         self.element_to_be_clickable(*NoAfraidChangeLocators.sex)
#         self.selenium_click(*NoAfraidChangeLocators.sex)
#         self.wait_element(*NoAfraidChangeLocators.sex_list)
#         self.select_sex(sex)
#         self.js_input(self.age(age), *NoAfraidChangeLocators.birthday)
#         time.sleep(0.6)
#         self.wait_element(*NoAfraidChangeLocators.phone)
#         self.selenium_click(*NoAfraidChangeLocators.phone)
#         self.selenium_input('9990403660', *NoAfraidChangeLocators.phone)
#         self.selenium_input('awjon94@gmail.com', *NoAfraidChangeLocators.email)
#         self.js_input('6420001900', *NoAfraidChangeLocators.passport)
#         self.js_input('04092019', *NoAfraidChangeLocators.date_start)
#         self.selenium_click(*NoAfraidChangeLocators.body)
#         self.js_input('650002', *NoAfraidChangeLocators.division)
#         self.selenium_input('Кем-то выдан', *NoAfraidChangeLocators.pass_who_give)
#
#         # Заполнение блока адреса регистрации
#         # ____________________________________________________________________________________
#         self.scroll_to_element(*NoAfraidChangeLocators.person1)
#         self.selenium_click(*NoAfraidChangeLocators.inp_address)
#         self.selenium_input('Мос', *NoAfraidChangeLocators.city)
#         self.selenium_click(*NoAfraidChangeLocators.select_city)
#         self.selenium_input('Арсеньева', *NoAfraidChangeLocators.street)
#         self.selenium_input('33', *NoAfraidChangeLocators.home)
#         self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
#         self.selenium_click(*NoAfraidChangeLocators.go_to_step_3)
#         if age<18 or (age>64 and sex=='male') or (age>59 and sex=='famale'):
#             self.wait_element(*NoAfraidChangeLocators.birthday_error)
#             assert self.driver.find_element(
#                 *NoAfraidChangeLocators.birthday_error).text == 'Нарушены условия страхования', 'некорректный текст ошибки'
#         else:
#             return True
#
#
#


