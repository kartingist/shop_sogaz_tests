from .locators import NoAfraidChangeLocators
from ..base_locators import Common_Locators
from ..base_page import BasePage
import time
import random
from datetime import date
from dateutil.relativedelta import relativedelta

email=[f'user{str(random.randint(90000, 99999))}@gmail.com']


class Step_1(BasePage):

    def select_program(self):
        self.selenium_click(*NoAfraidChangeLocators.program)
    def go_to_next_step(self):
        self.selenium_click(*NoAfraidChangeLocators.go_to_step_2)

class Step_2(BasePage):
    def should_be_step_2(self):
        assert self.should_be(*NoAfraidChangeLocators.step_2), "Не выполнен переход на второй шаг"

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
        self.selenium_input(email, *NoAfraidChangeLocators.email)
        self.js_input('6420001900', *NoAfraidChangeLocators.passport)
        self.js_input('04092019', *NoAfraidChangeLocators.date_start)
        self.selenium_click(*Common_Locators.body)
        self.js_input('650002', *NoAfraidChangeLocators.division)
        self.selenium_input('Кем-то выдан', *NoAfraidChangeLocators.pass_who_give)

        # Заполнение блока адреса регистрации
        # ____________________________________________________________________________________
        self.scroll_to_element(*NoAfraidChangeLocators.person1)
        self.input_city('Мос', *NoAfraidChangeLocators.inp_address)
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
    def anketa_required_fields(self, fio, whogiveandstreet):
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
        self.selenium_input(email, *NoAfraidChangeLocators.email)
        self.js_input('6420001900', *NoAfraidChangeLocators.passport)
        self.js_input('04092019', *NoAfraidChangeLocators.date_start)
        self.selenium_click(*Common_Locators.body)
        self.js_input('650002', *NoAfraidChangeLocators.division)
        self.selenium_input(whogiveandstreet, *NoAfraidChangeLocators.pass_who_give)

        # Заполнение блока адреса регистрации
        # ____________________________________________________________________________________
        self.scroll_to_element(*NoAfraidChangeLocators.person1)
        self.input_city('Мос', *NoAfraidChangeLocators.inp_address)
        self.selenium_input(whogiveandstreet, *NoAfraidChangeLocators.street)
        self.selenium_input('33', *NoAfraidChangeLocators.home)
        self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
        self.selenium_click(*NoAfraidChangeLocators.go_to_step_3)

    def anketa_null_fields_errors(self):
        self.wait_element(*NoAfraidChangeLocators.step_2)
        self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
        self.selenium_click(*NoAfraidChangeLocators.go_to_step_3)
        self.wait_element(*NoAfraidChangeLocators.surname_error)
        self.check_errors(*NoAfraidChangeLocators.surname_error, 'Обязательное поле')
        self.check_errors(*NoAfraidChangeLocators.firstname_error, 'Обязательное поле')
        self.check_errors(*NoAfraidChangeLocators.lastname_error, 'Обязательное поле')
        self.check_errors(*NoAfraidChangeLocators.birthday_error, 'Обязательное поле')
        self.check_errors(*NoAfraidChangeLocators.phone_error, 'Обязательное поле')
        self.check_errors(*NoAfraidChangeLocators.email_error, 'Обязательное поле')
        self.check_errors(*NoAfraidChangeLocators.passport_error, 'Обязательное поле')
        self.check_errors(*NoAfraidChangeLocators.date_start_error, 'Обязательное поле')
        self.check_errors(*NoAfraidChangeLocators.division_error, 'Обязательное поле')
        self.check_errors(*NoAfraidChangeLocators.pass_who_give_error, 'Обязательное поле')

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
        self.selenium_input(email, *NoAfraidChangeLocators.email)
        self.js_input('6420001900', *NoAfraidChangeLocators.passport)
        self.js_input('04092019', *NoAfraidChangeLocators.date_start)
        self.selenium_click(*Common_Locators.body)
        self.js_input('650002', *NoAfraidChangeLocators.division)
        self.selenium_input('Кем-то выдан', *NoAfraidChangeLocators.pass_who_give)

        # Заполнение блока адреса регистрации
        # ____________________________________________________________________________________
        self.scroll_to_element(*NoAfraidChangeLocators.person1)
        self.input_city('Мос', *NoAfraidChangeLocators.inp_address)
        self.selenium_input('Арсеньева', *NoAfraidChangeLocators.street)
        self.selenium_input('33', *NoAfraidChangeLocators.home)
        self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
        self.selenium_click(*NoAfraidChangeLocators.go_to_step_3)
# _______________________________________________________________________________________
    def anketa_validation_errors(self, testfio, textfields):
        self.wait_element(*NoAfraidChangeLocators.step_2)

        # Заполнение первого блока личных данных
        # ____________________________________________________________________________________
        self.selenium_input(testfio, *NoAfraidChangeLocators.surname)
        self.selenium_input(testfio, *NoAfraidChangeLocators.firstname)
        self.selenium_input(testfio, *NoAfraidChangeLocators.lastname)
        self.js_input('030819', *NoAfraidChangeLocators.birthday)
        self.scroll_to_element(*NoAfraidChangeLocators.phone)
        self.wait_element(*NoAfraidChangeLocators.phone)
        self.selenium_click(*NoAfraidChangeLocators.phone)
        self.selenium_input('99904036', *NoAfraidChangeLocators.phone)
        self.selenium_input('awjon94@gmail', *NoAfraidChangeLocators.email)
        self.js_input('6420001', *NoAfraidChangeLocators.passport)
        self.js_input('040920', *NoAfraidChangeLocators.date_start)
        self.selenium_click(*Common_Locators.body)
        self.js_input('6500', *NoAfraidChangeLocators.division)
        self.selenium_input('test', *NoAfraidChangeLocators.pass_who_give)


        # Заполнение блока адреса регистрации
        # ____________________________________________________________________________________
        self.scroll_to_element(*NoAfraidChangeLocators.person1)
        self.input_city('Мос', *NoAfraidChangeLocators.inp_address)
        self.selenium_input('test', *NoAfraidChangeLocators.street)
        self.js_input('6925', *NoAfraidChangeLocators.index)
        self.selenium_input(textfields, *NoAfraidChangeLocators.home)
        self.selenium_input(textfields, *NoAfraidChangeLocators.korpus)
        self.selenium_input(textfields, *NoAfraidChangeLocators.building)
        self.selenium_input(textfields, *NoAfraidChangeLocators.flat)
        self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
        self.selenium_click(*NoAfraidChangeLocators.go_to_step_3)
        self.wait_element(*NoAfraidChangeLocators.birthday_error)
#   Проверка ошибок
        self.check_errors(*NoAfraidChangeLocators.surname_error, 'Допустимы кирилические символы')
        self.check_errors(*NoAfraidChangeLocators.firstname_error, 'Допустимы кирилические символы')
        self.check_errors(*NoAfraidChangeLocators.lastname_error, 'Допустимы кирилические символы')
        self.check_errors(*NoAfraidChangeLocators.phone_error, 'Ошибка заполнения')
        self.check_errors(*NoAfraidChangeLocators.email_error, 'Неверный формат почты')
        self.check_errors(*NoAfraidChangeLocators.passport_error, 'Ошибка заполнения')
        self.check_errors(*NoAfraidChangeLocators.pass_who_give_error, 'Допустимы кирилические символы')
        self.check_errors(*NoAfraidChangeLocators.division_error, 'Ошибка заполнения')
        self.check_errors(*NoAfraidChangeLocators.street_error, 'Допустимы кирилические символы')
        self.check_errors(*NoAfraidChangeLocators.index_error, 'Ошибка заполнения')
#     ____________________________________________________________________________________________________________

    def age_check(self, age, sex):
        self.wait_element(*NoAfraidChangeLocators.step_2)
        # Заполнение первого блока личных данных
        # ____________________________________________________________________________________
        self.selenium_input('тестов', *NoAfraidChangeLocators.surname)
        self.selenium_input('тест', *NoAfraidChangeLocators.firstname)
        self.selenium_input('тестович', *NoAfraidChangeLocators.lastname)
        self.scroll_to_element(*NoAfraidChangeLocators.sex)
        self.select_sex(sex, *NoAfraidChangeLocators.sex)
        self.js_input(self.age(age), *NoAfraidChangeLocators.birthday)
        time.sleep(0.6)
        self.wait_element(*NoAfraidChangeLocators.phone)
        self.selenium_click(*NoAfraidChangeLocators.phone)
        self.selenium_input('9990403660', *NoAfraidChangeLocators.phone)
        self.selenium_input(email, *NoAfraidChangeLocators.email)
        self.js_input('6420001900', *NoAfraidChangeLocators.passport)
        self.js_input('04092019', *NoAfraidChangeLocators.date_start)
        self.selenium_click(*Common_Locators.body)
        self.js_input('650002', *NoAfraidChangeLocators.division)
        self.selenium_input('Кем-то выдан', *NoAfraidChangeLocators.pass_who_give)

        # Заполнение блока адреса регистрации
        # ____________________________________________________________________________________
        self.scroll_to_element(*NoAfraidChangeLocators.person1)
        self.input_city('Мос', *NoAfraidChangeLocators.inp_address)
        self.selenium_input('Арсеньева', *NoAfraidChangeLocators.street)
        self.selenium_input('33', *NoAfraidChangeLocators.home)
        self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
        self.selenium_click(*NoAfraidChangeLocators.go_to_step_3)
        if (18 <= age <= 64 and sex == 'male') or (18 <= age <= 59 and sex == 'famale'):
            if self.should_be(*Common_Locators.step3)==True:
                return True

            else:
                assert False, f"{self.driver.find_element(*NoAfraidChangeLocators.birthday_error).text}"
        else:
            self.wait_element(*NoAfraidChangeLocators.birthday_error)
            self.check_errors(*NoAfraidChangeLocators.birthday_error, 'Нарушены условия страхования')
        self.is_element_present(*Common_Locators.step3)

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
        self.selenium_input(email, *NoAfraidChangeLocators.email)
        self.js_input('6420001900', *NoAfraidChangeLocators.passport)
        self.js_input('04092019', *NoAfraidChangeLocators.date_start)
        self.selenium_click(*Common_Locators.body)
        self.js_input('650002', *NoAfraidChangeLocators.division)
        self.selenium_input('Кем-то выдан', *NoAfraidChangeLocators.pass_who_give)

        # Заполнение блока адреса регистрации
        # ____________________________________________________________________________________
        self.scroll_to_element(*NoAfraidChangeLocators.person1)
        self.input_city('Мос', *NoAfraidChangeLocators.inp_address)
        self.selenium_input('Арсеньева', *NoAfraidChangeLocators.street)
        self.selenium_input('33', *NoAfraidChangeLocators.home)
        self.scroll_to_element(*NoAfraidChangeLocators.personal_code)
        self.js_input(code, *NoAfraidChangeLocators.personal_code)
        self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
        self.selenium_click(*NoAfraidChangeLocators.go_to_step_3)
        if 0<len(code)<4:
            if self.should_be(*NoAfraidChangeLocators.personal_code_error)==True:
                self.check_errors(*NoAfraidChangeLocators.personal_code_error,
                                  'Числовое значение от 4 до 8 символов включительно')
            else:
                if self.should_be(*Common_Locators.step3)==True:
                    assert False, 'Некорректная валидация кода сотрудника'
                else: assert False, 'Что-то пошло не по плану'

        elif len(code)>8:
            assert len(self.driver.find_element(*NoAfraidChangeLocators.personal_code).get_attribute('value'))==8, 'удалось ввести 9ти значный код'
            return True
        else:
            return True

    def pass_date_start_negative(self, birth_day, days):
        self.js_input((date.today() - relativedelta
        (years=birth_day+1)).strftime('%d%m%Y'), *NoAfraidChangeLocators.birthday)

        self.js_input((date.today() + relativedelta
        (years=-1, days=days)).strftime('%d%m%Y'), *NoAfraidChangeLocators.date_start)

        self.js_click(*NoAfraidChangeLocators.go_to_step_3)
        self.should_be(*NoAfraidChangeLocators.date_start_error)
        if birth_day == 14:
            self.check_errors(*NoAfraidChangeLocators.date_start_error,
                'Дата выдачи паспорта некорректна: '
                'паспорт не может быть выдан ранее 14-ти лет с даты рождения')
        elif birth_day <= 0 or (birth_day == 20 and  days== 370):
            self.check_errors(*NoAfraidChangeLocators.date_start_error,
                'Дата больше текущей')

        else:
            self.check_errors(*NoAfraidChangeLocators.date_start_error,
                              'Дата выдачи паспорта некорректна: '
                              'срок действия указанного паспорта истек')



    def pass_date_start_positive(self, birth_day, days):
        self.wait_element(*NoAfraidChangeLocators.step_2)
        # Заполнение первого блока личных данных
        # ____________________________________________________________________________________
        self.selenium_input("Тест", *NoAfraidChangeLocators.surname)
        self.selenium_input("Тест", *NoAfraidChangeLocators.firstname)
        self.selenium_input("Тест", *NoAfraidChangeLocators.lastname)
        self.js_input((date.today() - relativedelta(years=birth_day+1)).strftime('%d%m%Y'), *NoAfraidChangeLocators.birthday)
        time.sleep(0.6)
        self.wait_element(*NoAfraidChangeLocators.phone)
        self.selenium_click(*NoAfraidChangeLocators.phone)
        self.selenium_input('9990403660', *NoAfraidChangeLocators.phone)
        self.selenium_input(email, *NoAfraidChangeLocators.email)
        self.js_input('6420001900', *NoAfraidChangeLocators.passport)
        self.js_input((date.today() + relativedelta(years=-1, days=days)).strftime('%d%m%Y'),
                      *NoAfraidChangeLocators.date_start)
        self.selenium_click(*Common_Locators.body)
        self.js_input('650002', *NoAfraidChangeLocators.division)
        self.selenium_input("Тест", *NoAfraidChangeLocators.pass_who_give)

        # Заполнение блока адреса регистрации
        # ____________________________________________________________________________________
        self.scroll_to_element(*NoAfraidChangeLocators.person1)
        self.input_city('Мос', *NoAfraidChangeLocators.inp_address)
        self.selenium_input("Тест", *NoAfraidChangeLocators.street)
        self.selenium_input('33', *NoAfraidChangeLocators.home)
        self.scroll_to_element(*NoAfraidChangeLocators.go_to_step_3)
        self.selenium_click(*NoAfraidChangeLocators.go_to_step_3)


