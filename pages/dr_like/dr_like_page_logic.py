from .locators import *
from ..base_page import BasePage
import time


class Step_1(BasePage):

    def step1(self, region, franchise):
        self.js_input('03081994', *DrLikeLocators.birthday_step1)
        self.driver.execute_script(f"document.getElementById('at_work{region}').click()")
        self.driver.execute_script(f"document.getElementById('franchise{franchise}').click()")
        self.selenium_click(*DrLikeLocators.sep1_calc)
        if self.cnt(*DrLikeLocators.tarifs)==0:
            assert False, 'Отсутствуют программы страхования'
        else:
            self.wait_element(*DrLikeLocators.box_program)
            self.selenium_click(*DrLikeLocators.program1)
            self.scroll_to_element(*DrLikeLocators.go_to_step_2)

    def go_to_next_step(self):
        self.selenium_click(*DrLikeLocators.go_to_step_2)


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
        self.selenium_click(*DrLikeLocators.body)
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
        self.selenium_click(*DrLikeLocators.body)
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

        self.scroll_to_element(*DrLikeLocators.go_to_step3)
        self.selenium_click(*DrLikeLocators.go_to_step3)


# # _________________________________________________________________________________________________________
#     def anketa_required_fields(self):
#         self.wait_element(*NoAfraidChangeLocators.step_2)
#         # Заполнение первого блока личных данных
#         # ____________________________________________________________________________________
#         self.selenium_input('тестов', *NoAfraidChangeLocators.surname)
#         self.selenium_input('тест', *NoAfraidChangeLocators.firstname)
#         self.selenium_input('тестович', *NoAfraidChangeLocators.lastname)
#         self.js_input('03081994', *NoAfraidChangeLocators.birthday)
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
#
#     def anketa_null_fields_errors(self):
#         self.wait_element(*NoAfraidChangeLocators.step_2)
#         self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
#         self.selenium_click(*NoAfraidChangeLocators.go_to_step_3)
#         self.wait_element(*NoAfraidChangeLocators.surname_error)
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.surname_error).text=='Обязательное поле', "не указана ошибка обязательности фамилии или текст ошибки не тот"
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.firstname_error).text == 'Обязательное поле', "не указана ошибка обязательности имени или текст ошибки не тот"
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.lastname_error).text == 'Обязательное поле', "не указана ошибка обязательности отчества или текст ошибки не тот"
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.birthday_error).text == 'Обязательное поле', "не указана ошибка обязательности др или текст ошибки не тот"
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.phone_error).text == 'Ошибка заполнения', "не указана ошибка некорректного номера"
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.email_error).text == 'Обязательное поле', "не указана ошибка обязательности email или текст ошибки не тот"
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.passport_error).text == 'Обязательное поле', "не указана ошибка обязательности № паспорта или текст ошибки не тот"
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.date_start_error).text == 'Обязательное поле', "не указана ошибка обязательности даты выдачи или текст ошибки не тот"
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.division_error).text == 'Обязательное поле', "не указана ошибка обязательности подразделения или текст ошибки не тот"
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.pass_who_give_error).text == 'Обязательное поле', "не указана ошибка обязательности кем выдан или текст ошибки не тот"
#
#         # Заполнение первого блока личных данных
#         # ____________________________________________________________________________________
#         self.selenium_input('тестов', *NoAfraidChangeLocators.surname)
#         self.selenium_input('тест', *NoAfraidChangeLocators.firstname)
#         self.selenium_input('тестович', *NoAfraidChangeLocators.lastname)
#         self.js_input('03081994', *NoAfraidChangeLocators.birthday)
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
# # _______________________________________________________________________________________
#     def anketa_validation_errors(self):
#         self.wait_element(*NoAfraidChangeLocators.step_2)
#
#         # Заполнение первого блока личных данных
#         # ____________________________________________________________________________________
#         self.selenium_input('test', *NoAfraidChangeLocators.surname)
#         self.selenium_input('test', *NoAfraidChangeLocators.firstname)
#         self.selenium_input('test', *NoAfraidChangeLocators.lastname)
#         self.js_input(self.age(18), *NoAfraidChangeLocators.birthday)
#         self.scroll_to_element(*NoAfraidChangeLocators.phone)
#         self.wait_element(*NoAfraidChangeLocators.phone)
#         self.selenium_click(*NoAfraidChangeLocators.phone)
#         self.selenium_input('99904036', *NoAfraidChangeLocators.phone)
#         self.selenium_input('awjon94@gmail', *NoAfraidChangeLocators.email)
#         self.js_input('6420001', *NoAfraidChangeLocators.passport)
#         self.js_input('040920', *NoAfraidChangeLocators.date_start)
#         self.selenium_click(*NoAfraidChangeLocators.body)
#         self.js_input('6500', *NoAfraidChangeLocators.division)
#         self.selenium_input('gddfgd', *NoAfraidChangeLocators.pass_who_give)
#
#
#         # Заполнение блока адреса регистрации
#         # ____________________________________________________________________________________
#         self.scroll_to_element(*NoAfraidChangeLocators.person1)
#         self.selenium_click(*NoAfraidChangeLocators.inp_address)
#         self.selenium_input('Мос', *NoAfraidChangeLocators.city)
#         self.selenium_click(*NoAfraidChangeLocators.select_city)
#         self.selenium_input('вывфdsf', *NoAfraidChangeLocators.street)
#         self.js_input('6925', *NoAfraidChangeLocators.index)
#         self.selenium_input('ывфfd', *NoAfraidChangeLocators.home)
#         self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
#         self.selenium_click(*NoAfraidChangeLocators.go_to_step_3)
#         self.wait_element(*NoAfraidChangeLocators.surname_error)
#         time.sleep(10)
# #   Проверка ошибок
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.surname_error).text=='Допустимы кирилические символы', 'Фамилия, Фактический результат:'+self.driver.find_element(
#             *NoAfraidChangeLocators.surname_error).text
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.firstname_error).text=='Допустимы кирилические символы', 'Имя, Фактический результат:'+self.driver.find_element(
#             *NoAfraidChangeLocators.firstname_error).text
# # тут на данный момент ошибка
#         # assert self.driver.find_element(
#         #     *NoAfraidChangeLocators.lastname_error).text=='Допустимы кирилические символы', 'Отчество, Фактический результат:'+self.driver.find_element(
#         #     *NoAfraidChangeLocators.lastname_error).text
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.phone_error).text == 'Ошибка заполнения', 'Телефон, Фактический результат:' + self.driver.find_element(
#             *NoAfraidChangeLocators.phone_error).text
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.email_error).text == 'Ошибка заполнения', 'Email, Фактический результат:' + self.driver.find_element(
#             *NoAfraidChangeLocators.email_error).text
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.passport_error).text == 'Ошибка заполнения', 'Паспорт, Фактический результат:' + self.driver.find_element(
#             *NoAfraidChangeLocators.passport_error).text
# # тут на данный момент ошибка
#         # assert self.driver.find_element(
#         #     *NoAfraidChangeLocators.pass_who_give_error).text == 'Допустимы кирилические символы', 'Кем выдан, Фактический результат:' + self.driver.find_element(
#         #     *NoAfraidChangeLocators.pass_who_give_error).text
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.division_error).text == 'Ошибка заполнения', 'Код подразделения, Фактический результат:' + self.driver.find_element(
#             *NoAfraidChangeLocators.division_error).text
# # тут на данный момент ошибка
#         # assert self.driver.find_element(
#         #     *NoAfraidChangeLocators.street_error).text=='Допустимы кирилические символы', 'Улица, Фактический результат:'+self.driver.find_element(
#         #     *NoAfraidChangeLocators.street_error).text
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.index_error).text == 'Ошибка заполнения', 'Индекс, Фактический результат:' + self.driver.find_element(
#             *NoAfraidChangeLocators.index_error).text
# # тут на данный момент ошибка
#         # assert self.driver.find_element(
#         #     *NoAfraidChangeLocators.home_error).text != 'Ошибка заполнения', 'Дом, Фактический результат:' + self.driver.find_element(
#         #     *NoAfraidChangeLocators.home_error).text
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
class Step_3(BasePage):
    def should_be_step_3(self):
        assert self.is_element_present(*DrLikeLocators.step3), "Не выполнен переход на третий шаг"
        self.wait_element(*DrLikeLocators.step3)
        self.scroll_to_element(*DrLikeLocators.get_code)
        self.wait_element(*DrLikeLocators.email_confirm)
        time.sleep(3)

    def get_input_code(self):
        self.selenium_click(*DrLikeLocators.get_code)
        self.wait_element(*DrLikeLocators.code)
        self.selenium_input(self.driver.find_element(*DrLikeLocators.code).text, *DrLikeLocators.codeConfirm)
        self.selenium_click(*DrLikeLocators.codeConfirmNext)
        time.sleep(1)
    def accept_checkbox(self):
        self.scroll_to_element(*DrLikeLocators.checkboxes)
        x = len(self.driver.find_elements(*DrLikeLocators.checkboxes))
        # Активируем
        for i in range(1, x+1):
            self.driver.execute_script(f"document.getElementById('check{i}').click()")
        self.selenium_click(*DrLikeLocators.step_to_pay)
#
#
class Pay_step(BasePage):
    def sbp(self):
        self.wait_element(*DrLikeLocators.card_pay)
        self.selenium_click(*DrLikeLocators.card_pay)

    def go_to_pay(self):

        self.wait_element(*DrLikeLocators.pan)
        assert self.is_element_present(*DrLikeLocators.pan), "Не выполнен переход на эквайринг'"
        self.js_input('9000000000000000001', *DrLikeLocators.pan)
        time.sleep(0.2)
        self.driver.find_element(*DrLikeLocators.month).send_keys('12')
        self.driver.find_element(*DrLikeLocators.year).send_keys('21')
        self.js_input('123', *DrLikeLocators.cvc)
        self.js_click(*DrLikeLocators.pay_button)

        self.wait_element(*DrLikeLocators.payment_info)
        success = self.driver.find_element(*DrLikeLocators.payment_info_message).text
        assert 'Операция выполнена успешно' == success, success

