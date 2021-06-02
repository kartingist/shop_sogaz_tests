import pytest
from .pages.no_afraid_page_logic import *
import time
from .link import link

links=link[1]



@pytest.mark.parametrize('link', links,  scope='function')
def test_base(browser, link):

    link = link + 'accident/no_afraid_change/#'
    step_1 = Step_1(browser, link)
    step_1.open()
    step_1.close_popaps()
    step_1.go_to_next_step()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.input_full_anketa()

    step_3 = Step_3(browser, link)
    step_3.should_be_step_3()
    step_3.get_input_code()
    step_3.accept_checkbox()
    if 'https://sogazrelease.support.zetest.site/' not in link and 'http://shop.sogaz.loc/' not in link:
        pay_step = Pay_step(browser, link)
        pay_step.go_to_pay()


@pytest.mark.parametrize('link', links,  scope='function')
def test_required_fields(browser, link ):

    link = link + 'accident/no_afraid_change/#'
    step_1 = Step_1(browser, link)
    step_1.open()
    step_1.close_popaps()
    step_1.go_to_next_step()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.anketa_required_fields()

    step_3 = Step_3(browser, link)
    step_3.should_be_step_3()
    step_3.get_input_code()
    step_3.accept_checkbox()

    if 'https://sogazrelease.support.zetest.site/' not in link and 'http://shop.sogaz.loc/' not in link:
        pay_step = Pay_step(browser, link)
        pay_step.go_to_pay()

@pytest.mark.parametrize('link', links,  scope='function')
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


@pytest.mark.parametrize('link', links,  scope='function')
def test_anketa_validation_errors(browser, link):
    link = link + 'accident/no_afraid_change/#'
    step_1 = Step_1(browser, link)
    step_1.open()
    step_1.close_popaps()
    step_1.go_to_next_step()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.anketa_validation_errors()
    #
    # step_3 = Step_3(browser, link)
    # step_3.should_be_step_3()

@pytest.mark.parametrize('link', links,  scope='function')
@pytest.mark.parametrize('age, sex', [(17, 'male'), (18, 'male'), (64, 'male'), (65, 'male'), (17, 'famale'), (18, 'famale'), (59, 'famale'), (60, 'famale')])
def test_age(browser, link, age, sex):
    link = link + 'accident/no_afraid_change/#'
    step_1 = Step_1(browser, link)
    step_1.open()
    step_1.close_popaps()
    step_1.go_to_next_step()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    # step_2.age_check(age, sex)
    if step_2.age_check(age, sex)==True:

        step_3 = Step_3(browser, link)
        step_3.should_be_step_3()

