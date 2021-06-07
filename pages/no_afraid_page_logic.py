from .locators import NoAfraidChangeLocators
from .base_page import BasePage
import time




class Step_1(BasePage):

    def select_program(self):
        self.selenium_click(*NoAfraidChangeLocators.program)
    def go_to_next_step(self):
        self.selenium_click(*NoAfraidChangeLocators.go_to_step_2)

class Step_2(BasePage):
    def should_be_step_2(self):
        assert self.is_element_present(*NoAfraidChangeLocators.step_2), "Не выполнен переход на второй шаг"

    def input_full_anketa(self):
        self.wait_element(*NoAfraidChangeLocators.step_2)
        # Заполнение первого блока личных данных
        # ____________________________________________________________________________________
        self.selenium_input('тестов', *NoAfraidChangeLocators.surname)
        self.selenium_input('тест', *NoAfraidChangeLocators.firstname)
        self.selenium_input('тестович', *NoAfraidChangeLocators.lastname)
        self.js_input('03081994', *NoAfraidChangeLocators.birthday)
        time.sleep(0.6)
        self.wait_element(*NoAfraidChangeLocators.phone)
        self.selenium_click(*NoAfraidChangeLocators.phone)
        self.selenium_input('9990403660', *NoAfraidChangeLocators.phone)
        self.selenium_input('awjon94@gmail.com', *NoAfraidChangeLocators.email)
        self.js_input('6420001900', *NoAfraidChangeLocators.passport)
        self.js_input('04092019', *NoAfraidChangeLocators.date_start)
        self.selenium_click(*NoAfraidChangeLocators.body)
        self.js_input('650002', *NoAfraidChangeLocators.division)
        self.selenium_input('Кем-то выдан', *NoAfraidChangeLocators.pass_who_give)

        # Заполнение блока адреса регистрации
        # ____________________________________________________________________________________
        self.scroll_to_element(*NoAfraidChangeLocators.person1)
        self.selenium_click(*NoAfraidChangeLocators.inp_address)
        self.selenium_input('Мос', *NoAfraidChangeLocators.city)
        self.selenium_click(*NoAfraidChangeLocators.select_city)
        self.selenium_input('Арсеньева', *NoAfraidChangeLocators.street)
        self.js_input('692502', *NoAfraidChangeLocators.index)
        self.selenium_input('33', *NoAfraidChangeLocators.home)
        self.selenium_input('1', *NoAfraidChangeLocators.korpus)
        self.selenium_input('2', *NoAfraidChangeLocators.building)
        self.selenium_input('60', *NoAfraidChangeLocators.flat)
        self.selenium_input('Уссурийск', *NoAfraidChangeLocators.birth_place)
        self.js_input('12345678', *NoAfraidChangeLocators.personal_code)
        self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
        self.selenium_click(*NoAfraidChangeLocators.go_to_step_3)
# _________________________________________________________________________________________________________
    def anketa_required_fields(self, fio):
        self.wait_element(*NoAfraidChangeLocators.step_2)
        # Заполнение первого блока личных данных
        # ____________________________________________________________________________________
        self.selenium_input(fio, *NoAfraidChangeLocators.surname)
        self.selenium_input(fio, *NoAfraidChangeLocators.firstname)
        self.selenium_input(fio, *NoAfraidChangeLocators.lastname)
        self.js_input('03081994', *NoAfraidChangeLocators.birthday)
        time.sleep(0.6)
        self.wait_element(*NoAfraidChangeLocators.phone)
        self.selenium_click(*NoAfraidChangeLocators.phone)
        self.selenium_input('9990403660', *NoAfraidChangeLocators.phone)
        self.selenium_input('awjon94@gmail.com', *NoAfraidChangeLocators.email)
        self.js_input('6420001900', *NoAfraidChangeLocators.passport)
        self.js_input('04092019', *NoAfraidChangeLocators.date_start)
        self.selenium_click(*NoAfraidChangeLocators.body)
        self.js_input('650002', *NoAfraidChangeLocators.division)
        self.selenium_input('Кем-то выдан', *NoAfraidChangeLocators.pass_who_give)

        # Заполнение блока адреса регистрации
        # ____________________________________________________________________________________
        self.scroll_to_element(*NoAfraidChangeLocators.person1)
        self.selenium_click(*NoAfraidChangeLocators.inp_address)
        self.selenium_input('Мос', *NoAfraidChangeLocators.city)
        self.selenium_click(*NoAfraidChangeLocators.select_city)
        self.selenium_input('Арсеньева', *NoAfraidChangeLocators.street)
        self.selenium_input('33', *NoAfraidChangeLocators.home)
        self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
        self.selenium_click(*NoAfraidChangeLocators.go_to_step_3)

    def anketa_null_fields_errors(self):
        self.wait_element(*NoAfraidChangeLocators.step_2)
        self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
        self.selenium_click(*NoAfraidChangeLocators.go_to_step_3)
        self.wait_element(*NoAfraidChangeLocators.surname_error)
        assert self.driver.find_element(
            *NoAfraidChangeLocators.surname_error).text=='Обязательное поле', "не указана ошибка обязательности фамилии или текст ошибки не тот"
        assert self.driver.find_element(
            *NoAfraidChangeLocators.firstname_error).text == 'Обязательное поле', "не указана ошибка обязательности имени или текст ошибки не тот"
        assert self.driver.find_element(
            *NoAfraidChangeLocators.lastname_error).text == 'Обязательное поле', "не указана ошибка обязательности отчества или текст ошибки не тот"
        assert self.driver.find_element(
            *NoAfraidChangeLocators.birthday_error).text == 'Обязательное поле', "не указана ошибка обязательности др или текст ошибки не тот"
        assert self.driver.find_element(
            *NoAfraidChangeLocators.phone_error).text == 'Обязательное поле', 'Фактический результат:' + self.driver.find_element(
            *NoAfraidChangeLocators.phone_error).text
        assert self.driver.find_element(
            *NoAfraidChangeLocators.email_error).text == 'Обязательное поле', "не указана ошибка обязательности email или текст ошибки не тот"
        assert self.driver.find_element(
            *NoAfraidChangeLocators.passport_error).text == 'Обязательное поле', "не указана ошибка обязательности № паспорта или текст ошибки не тот"
        assert self.driver.find_element(
            *NoAfraidChangeLocators.date_start_error).text == 'Обязательное поле', "не указана ошибка обязательности даты выдачи или текст ошибки не тот"
        assert self.driver.find_element(
            *NoAfraidChangeLocators.division_error).text == 'Обязательное поле', "не указана ошибка обязательности подразделения или текст ошибки не тот"
        assert self.driver.find_element(
            *NoAfraidChangeLocators.pass_who_give_error).text == 'Обязательное поле', "не указана ошибка обязательности кем выдан или текст ошибки не тот"

        # Заполнение первого блока личных данных
        # ____________________________________________________________________________________
        self.selenium_input('тестов', *NoAfraidChangeLocators.surname)
        self.selenium_input('тест', *NoAfraidChangeLocators.firstname)
        self.selenium_input('тестович', *NoAfraidChangeLocators.lastname)
        self.js_input('03081994', *NoAfraidChangeLocators.birthday)
        time.sleep(0.6)
        self.wait_element(*NoAfraidChangeLocators.phone)
        self.selenium_click(*NoAfraidChangeLocators.phone)
        self.selenium_input('9990403660', *NoAfraidChangeLocators.phone)
        self.selenium_input('awjon94@gmail.com', *NoAfraidChangeLocators.email)
        self.js_input('6420001900', *NoAfraidChangeLocators.passport)
        self.js_input('04092019', *NoAfraidChangeLocators.date_start)
        self.selenium_click(*NoAfraidChangeLocators.body)
        self.js_input('650002', *NoAfraidChangeLocators.division)
        self.selenium_input('Кем-то выдан', *NoAfraidChangeLocators.pass_who_give)

        # Заполнение блока адреса регистрации
        # ____________________________________________________________________________________
        self.scroll_to_element(*NoAfraidChangeLocators.person1)
        self.selenium_click(*NoAfraidChangeLocators.inp_address)
        self.selenium_input('Мос', *NoAfraidChangeLocators.city)
        self.selenium_click(*NoAfraidChangeLocators.select_city)
        self.selenium_input('Арсеньева', *NoAfraidChangeLocators.street)
        self.selenium_input('33', *NoAfraidChangeLocators.home)
        self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
        self.selenium_click(*NoAfraidChangeLocators.go_to_step_3)
# _______________________________________________________________________________________
    def anketa_validation_errors(self, test):
        self.wait_element(*NoAfraidChangeLocators.step_2)

        # Заполнение первого блока личных данных
        # ____________________________________________________________________________________
        self.selenium_input(test, *NoAfraidChangeLocators.surname)
        self.selenium_input('test', *NoAfraidChangeLocators.firstname)
        self.selenium_input('test', *NoAfraidChangeLocators.lastname)
        self.js_input('030819', *NoAfraidChangeLocators.birthday)
        self.scroll_to_element(*NoAfraidChangeLocators.phone)
        self.wait_element(*NoAfraidChangeLocators.phone)
        self.selenium_click(*NoAfraidChangeLocators.phone)
        self.selenium_input('99904036', *NoAfraidChangeLocators.phone)
        self.selenium_input('awjon94@gmail', *NoAfraidChangeLocators.email)
        self.js_input('6420001', *NoAfraidChangeLocators.passport)
        self.js_input('040920', *NoAfraidChangeLocators.date_start)
        self.selenium_click(*NoAfraidChangeLocators.body)
        self.js_input('6500', *NoAfraidChangeLocators.division)
        self.selenium_input(test, *NoAfraidChangeLocators.pass_who_give)


        # Заполнение блока адреса регистрации
        # ____________________________________________________________________________________
        self.scroll_to_element(*NoAfraidChangeLocators.person1)
        self.selenium_click(*NoAfraidChangeLocators.inp_address)
        self.selenium_input('Мос', *NoAfraidChangeLocators.city)
        self.selenium_click(*NoAfraidChangeLocators.select_city)
        self.selenium_input('test', *NoAfraidChangeLocators.street)
        self.js_input('6925', *NoAfraidChangeLocators.index)
        self.selenium_input('test', *NoAfraidChangeLocators.home)
        self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
        self.selenium_click(*NoAfraidChangeLocators.go_to_step_3)
        self.wait_element(*NoAfraidChangeLocators.birthday_error)
#   Проверка ошибок
        self.check_errors(*NoAfraidChangeLocators.surname_error, 'Допустимы кирилические символы')
        # assert self.driver.find_element(
        #     ).text=='Допустимы кирилические символы', 'Фамилия, Фактический результат:'+self.driver.find_element(
        #     *NoAfraidChangeLocators.surname_error).text
        # assert self.driver.find_element(
        #     *NoAfraidChangeLocators.firstname_error).text=='Допустимы кирилические символы', 'Имя, Фактический результат:'+self.driver.find_element(
        #     *NoAfraidChangeLocators.firstname_error).text
        self.check_errors(*NoAfraidChangeLocators.firstname_error, 'Допустимы кирилические символы')
# тут на данный момент ошибка
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.lastname_error).text=='Допустимы кирилические символы', 'Отчество, Фактический результат:'+self.driver.find_element(
#             *NoAfraidChangeLocators.lastname_error).text
        self.check_errors(*NoAfraidChangeLocators.lastname_error, 'Допустимы кирилические символы')
        # assert self.driver.find_element(
        #     *NoAfraidChangeLocators.phone_error).text == 'Ошибка заполнения', 'Телефон, Фактический результат:' + self.driver.find_element(
        #     *NoAfraidChangeLocators.phone_error).text
        self.check_errors(*NoAfraidChangeLocators.phone_error, 'Ошибка заполнения')
        # assert self.driver.find_element(
        #     *NoAfraidChangeLocators.email_error).text == 'Неверный формат почты', 'Email, Фактический результат:' + self.driver.find_element(
        #     *NoAfraidChangeLocators.email_error).text
        self.check_errors(*NoAfraidChangeLocators.email_error, 'Неверный формат почты')
        # assert self.driver.find_element(
        #     *NoAfraidChangeLocators.passport_error).text == 'Ошибка заполнения', 'Паспорт, Фактический результат:' + self.driver.find_element(
        #     *NoAfraidChangeLocators.passport_error).text
        self.check_errors(*NoAfraidChangeLocators.passport_error, 'Ошибка заполнения')
# тут на данный момент ошибка
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.pass_who_give_error).text == 'Допустимы кирилические символы', 'Кем выдан, Фактический результат:' + self.driver.find_element(
#             *NoAfraidChangeLocators.pass_who_give_error).text
        self.check_errors(*NoAfraidChangeLocators.pass_who_give_error, 'Допустимы кирилические символы')
        # assert self.driver.find_element(
        #     *NoAfraidChangeLocators.division_error).text == 'Ошибка заполнения', 'Код подразделения, Фактический результат:' + self.driver.find_element(
        #     *NoAfraidChangeLocators.division_error).text
        self.check_errors(*NoAfraidChangeLocators.division_error, 'Ошибка заполнения')
# тут на данный момент ошибка
#         assert self.driver.find_element(
#             *NoAfraidChangeLocators.street_error).text=='Допустимы кирилические символы', 'Улица, Фактический результат:'+self.driver.find_element(
#             *NoAfraidChangeLocators.street_error).text
        self.check_errors(*NoAfraidChangeLocators.street_error, 'Допустимы кирилические символы')
        # assert self.driver.find_element(
        #     *NoAfraidChangeLocators.index_error).text == 'Ошибка заполнения', 'Индекс, Фактический результат:' + self.driver.find_element(
        #     *NoAfraidChangeLocators.index_error).text
        self.check_errors(*NoAfraidChangeLocators.index_error, 'Ошибка заполнения')

#     ____________________________________________________________________________________________________________

    def age_check(self, age, sex):
        self.wait_element(*NoAfraidChangeLocators.step_2)
        # Заполнение первого блока личных данных
        # ____________________________________________________________________________________
        self.selenium_input('тестов', *NoAfraidChangeLocators.surname)
        self.selenium_input('тест', *NoAfraidChangeLocators.firstname)
        self.selenium_input('тестович', *NoAfraidChangeLocators.lastname)
        self.element_to_be_clickable(*NoAfraidChangeLocators.sex)
        self.selenium_click(*NoAfraidChangeLocators.sex)
        self.wait_element(*NoAfraidChangeLocators.sex_list)
        self.select_sex(sex)
        self.js_input(self.age(age), *NoAfraidChangeLocators.birthday)
        time.sleep(0.6)
        self.wait_element(*NoAfraidChangeLocators.phone)
        self.selenium_click(*NoAfraidChangeLocators.phone)
        self.selenium_input('9990403660', *NoAfraidChangeLocators.phone)
        self.selenium_input('awjon94@gmail.com', *NoAfraidChangeLocators.email)
        self.js_input('6420001900', *NoAfraidChangeLocators.passport)
        self.js_input('04092019', *NoAfraidChangeLocators.date_start)
        self.selenium_click(*NoAfraidChangeLocators.body)
        self.js_input('650002', *NoAfraidChangeLocators.division)
        self.selenium_input('Кем-то выдан', *NoAfraidChangeLocators.pass_who_give)

        # Заполнение блока адреса регистрации
        # ____________________________________________________________________________________
        self.scroll_to_element(*NoAfraidChangeLocators.person1)
        self.selenium_click(*NoAfraidChangeLocators.inp_address)
        self.selenium_input('Мос', *NoAfraidChangeLocators.city)
        self.selenium_click(*NoAfraidChangeLocators.select_city)
        self.selenium_input('Арсеньева', *NoAfraidChangeLocators.street)
        self.selenium_input('33', *NoAfraidChangeLocators.home)
        self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
        self.selenium_click(*NoAfraidChangeLocators.go_to_step_3)
        if (18 <= age <= 64 and sex == 'male') or (18 <= age <= 59 and sex == 'famale'):
            return True
        else:
            self.wait_element(*NoAfraidChangeLocators.birthday_error)
            assert self.driver.find_element(
                *NoAfraidChangeLocators.birthday_error).text == 'Нарушены условия страхования', 'Фактический результат:'+self.driver.find_element(*NoAfraidChangeLocators.birthday_error).text

    def personal_code_check(self, code):
        self.wait_element(*NoAfraidChangeLocators.step_2)
        # Заполнение первого блока личных данных
        # ____________________________________________________________________________________
        self.selenium_input('тестов', *NoAfraidChangeLocators.surname)
        self.selenium_input('тест', *NoAfraidChangeLocators.firstname)
        self.selenium_input('тестович', *NoAfraidChangeLocators.lastname)
        self.js_input(self.age(18), *NoAfraidChangeLocators.birthday)
        time.sleep(0.6)
        self.wait_element(*NoAfraidChangeLocators.phone)
        self.selenium_click(*NoAfraidChangeLocators.phone)
        self.selenium_input('9990403660', *NoAfraidChangeLocators.phone)
        self.selenium_input('awjon94@gmail.com', *NoAfraidChangeLocators.email)
        self.js_input('6420001900', *NoAfraidChangeLocators.passport)
        self.js_input('04092019', *NoAfraidChangeLocators.date_start)
        self.selenium_click(*NoAfraidChangeLocators.body)
        self.js_input('650002', *NoAfraidChangeLocators.division)
        self.selenium_input('Кем-то выдан', *NoAfraidChangeLocators.pass_who_give)

        # Заполнение блока адреса регистрации
        # ____________________________________________________________________________________
        self.scroll_to_element(*NoAfraidChangeLocators.person1)
        self.selenium_click(*NoAfraidChangeLocators.inp_address)
        self.selenium_input('Мос', *NoAfraidChangeLocators.city)
        self.selenium_click(*NoAfraidChangeLocators.select_city)
        self.selenium_input('Арсеньева', *NoAfraidChangeLocators.street)
        self.selenium_input('33', *NoAfraidChangeLocators.home)
        self.scroll_to_element(*NoAfraidChangeLocators.personal_code)
        self.js_input(code, *NoAfraidChangeLocators.personal_code)
        self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
        self.selenium_click(*NoAfraidChangeLocators.go_to_step_3)
        if 0<len(code)<4:
            self.wait_element(*NoAfraidChangeLocators.personal_code_error)
            assert self.driver.find_element(*NoAfraidChangeLocators.personal_code_error).text == 'Числовое значение от 4 до 8 символов включительно', 'некорректный текст ошибки:'+self.driver.find_element(*NoAfraidChangeLocators.personal_code_error).text
        elif len(code)>8:
            assert len(self.driver.find_element(*NoAfraidChangeLocators.personal_code).get_attribute('value'))==8, 'удалось ввести 9ти значный код'
            return True
        else:
            return True

class Step_3(BasePage):
    def should_be_step_3(self):
        time.sleep(1)
        self.wait_element(*NoAfraidChangeLocators.step3)
        assert self.is_element_present(*NoAfraidChangeLocators.step3), "Не выполнен переход на третий шаг"

    def get_input_code(self):
        self.scroll_to_element(*NoAfraidChangeLocators.get_code)
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

