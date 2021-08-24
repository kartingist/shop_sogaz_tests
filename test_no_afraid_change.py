import pytest
from .pages.no_afraid_change.step_2 import *
from .pages.step_3_and_pay import *
import time
from .link import link
from .pages.validate_data import *


link=link[3]

# 1) полный прогон с оплатой
@pytest.mark.parametrize('link', link,  scope='function')
def test_full_run(browser, link):

    link = link + 'accident/no_afraid_change/#'
    step_1 = Step_1(browser, link)
    step_1.open()
    step_1.close_popaps()
    step_1.select_program()
    step_1.go_to_next_step()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.input_full_anketa()

    step_3 = Step_3(browser, link)
    step_3.should_be_step_3()
    if 'https://shop.sogaz.ru/' not in link:
        step_3.get_input_code()
        step_3.accept_checkbox()
        step_3.go_to_pay_click()
        if 'https://sogazrelease.support.zetest.site/' not in link and 'http://shop.sogaz.loc/' not in link:
            pay_step = Pay_step(browser, link)
            pay_step.go_to_pay()


# 2) позитивные тесты полей ФИО
@pytest.mark.parametrize('link', link,  scope='function')
@pytest.mark.parametrize('fio', CyrillicValidate_positive)
def test_fio_positive(browser, link, fio):
    whogiveandstreet='Тест'
    link = link + 'accident/no_afraid_change/#'
    step_1 = Step_1(browser, link)
    step_1.open()
    step_1.close_popaps()
    step_1.go_to_next_step()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.anketa_required_fields(fio, whogiveandstreet)

    step_3 = Step_3(browser, link)
    step_3.should_be_step_3()

# 3) позитивные тесты полей кем выдан и улица
@pytest.mark.parametrize('link', link,  scope='function')
@pytest.mark.parametrize('whogiveandstreet', CyrillicAndNumberValidate)
def test_whogiveandstreet_validate(browser, link, whogiveandstreet):
    fio='Тест'
    link = link + 'accident/no_afraid_change/#'
    step_1 = Step_1(browser, link)
    step_1.open()
    step_1.close_popaps()
    step_1.go_to_next_step()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.anketa_required_fields(fio, whogiveandstreet)

    step_3 = Step_3(browser, link)
    step_3.should_be_step_3()

# 4) проверка ошибок обязательных полей
@pytest.mark.parametrize('link', link,  scope='function')
def test_null_fields_errors(browser, link ):

    link = link + 'accident/no_afraid_change/#'
    step_1 = Step_1(browser, link)
    step_1.open()
    step_1.close_popaps()
    step_1.go_to_next_step()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.anketa_null_fields_errors()

    step_3 = Step_3(browser, link)
    step_3.should_be_step_3()

# 5) негативные проверки полей ФИО и позитивные для текстовых полей(перенести в другой тест)
@pytest.mark.parametrize('link', link,  scope='function')
@pytest.mark.parametrize('testfio, textfields', CyrillicValidate_negative)
def test_anketa_validation_errors(browser, link, testfio, textfields):
    link = link + 'accident/no_afraid_change/#'
    step_1 = Step_1(browser, link)
    step_1.open()
    step_1.close_popaps()
    step_1.go_to_next_step()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.anketa_validation_errors(testfio, textfields)

# 6) проверка возраста клиента
@pytest.mark.parametrize('link', link,  scope='function')
@pytest.mark.parametrize('age, sex', BirthdayValidate)
def test_age(browser, link, age, sex):
    link = link + 'accident/no_afraid_change/#'
    step_1 = Step_1(browser, link)
    step_1.open()
    step_1.close_popaps()
    step_1.go_to_next_step()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.age_check(age, sex)
#
# 7) проверка валидации кода сотрудника
@pytest.mark.parametrize('link', link,  scope='function')
@pytest.mark.parametrize('code', PersonalCodeValidate)
def test_validate_personal_code(browser, link, code):
    link = link + 'accident/no_afraid_change/#'
    step_1 = Step_1(browser, link)
    step_1.open()
    step_1.close_popaps()
    step_1.go_to_next_step()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    if step_2.personal_code_check(code)==True:
        step_3 = Step_3(browser, link)
        step_3.should_be_step_3()

# 8) негативные проверки даты выдачи паспорта
@pytest.mark.parametrize('link', link,  scope='function')
@pytest.mark.parametrize('birth_day, days', DateStartPassNegValidate)
def test__negative_pass_date_start_validate(browser, link, birth_day, days):
    link = link + 'accident/no_afraid_change/#'
    step_1 = Step_1(browser, link)
    step_1.open()
    step_1.close_popaps()
    step_1.go_to_next_step()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.pass_date_start_negative(birth_day, days)

# 9) позитивные проверки даты выдачи паспорта
@pytest.mark.parametrize('link', link,  scope='function')
@pytest.mark.parametrize('birth_day, days', DateStartPassPosValidate)
def test_positive_pass_date_start_validate(browser, link, birth_day, days):
    link = link + 'accident/no_afraid_change/#'
    step_1 = Step_1(browser, link)
    step_1.open()
    step_1.close_popaps()
    step_1.go_to_next_step()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.pass_date_start_positive(birth_day, days)
    step_3 = Step_3(browser, link)
    step_3.should_be_step_3()
