import pytest
from .pages.dr_like.step_1 import *
from .pages.dr_like.step_2 import *
from .pages.step_3_and_pay import *
import time
from .link import link
from .pages.validate_data import *


link=link[0]
# link = str(links[0]) + 'accident/doctor_like/'
# doctor_like_premium

@pytest.mark.parametrize('link', link,  scope='function')
@pytest.mark.parametrize('region', [0, 1, 2], scope='function')
@pytest.mark.parametrize('franchise', [50, 30, 20],   scope='function')
# @pytest.mark.parametrize('region', [0], scope='function')
# @pytest.mark.parametrize('franchise', [50],   scope='function')
def test_full_run(browser, link, region, franchise):
    link = link + 'accident/doctor_like/'
    step_1 = Step_1(browser, link)
    step_1.open()


    step_1.close_popaps()
    step_1.step1full(region, franchise)

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.input_full_anketa()
    time.sleep(3)

    step_3 = Step_3(browser, link)
    step_3.should_be_step_3()
    step_3.get_input_code()
    step_3.accept_checkbox()


    if 'https://sogazrelease.support.zetest.site/' not in link and 'http://shop.sogaz.loc/' not in link:
        pay_step = Pay_step(browser, link)
        pay_step.sbp()
        pay_step.go_to_pay()

@pytest.mark.parametrize('link', link,  scope='function')
def test_min_info(browser, link):
    link = link + 'accident/doctor_like/'
    step_1 = Step_1(browser, link)
    step_1.open()

    step_1.close_popaps()
    step_1.step1base()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.anketa_min_data()

    step_3 = Step_3(browser, link)
    step_3.should_be_step_3()

@pytest.mark.parametrize('link', link,  scope='function')
@pytest.mark.parametrize('fio', CyrillicValidate_positive)
def test_fio_positive(browser, link, fio):
    whogiveandstreet = 'Тест'
    link = link + 'accident/doctor_like/'
    step_1 = Step_1(browser, link)
    step_1.open()

    step_1.close_popaps()
    step_1.step1base()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.anketa_fio_whogiveandstreet(fio, whogiveandstreet)

    step_3 = Step_3(browser, link)
    step_3.should_be_step_3()

@pytest.mark.parametrize('link', link,  scope='function')
@pytest.mark.parametrize('whogiveandstreet', CyrillicAndNumberValidate)
def test_whogiveandstreet_validate(browser, link, whogiveandstreet):
    fio = 'Тест'
    link = link + 'accident/doctor_like/'
    step_1 = Step_1(browser, link)
    step_1.open()

    step_1.close_popaps()
    step_1.step1base()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.anketa_fio_whogiveandstreet(fio, whogiveandstreet)

    step_3 = Step_3(browser, link)
    step_3.should_be_step_3()


@pytest.mark.parametrize('link', link,  scope='function')
def test_null_fields(browser, link):

    link = link + 'accident/doctor_like/'
    step_1 = Step_1(browser, link)
    step_1.open()

    step_1.close_popaps()
    step_1.step1base()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.anketa_null_fields_errors()

@pytest.mark.parametrize('link', link,  scope='function')
def test_anketa_validation_errors(browser, link):

    link = link + 'accident/doctor_like/'
    step_1 = Step_1(browser, link)
    step_1.open()

    step_1.close_popaps()
    step_1.step1base()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.anketa_validation_errors()

@pytest.mark.parametrize('link', link,  scope='function')
@pytest.mark.parametrize('testfio, textfields', CyrillicValidate_negative)
def test_fio_validation_errors(browser, link, testfio, textfields):

    link = link + 'accident/doctor_like/'
    step_1 = Step_1(browser, link)
    step_1.open()

    step_1.close_popaps()
    step_1.step1base()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.fio_validation_negative(testfio, textfields)

