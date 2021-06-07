import pytest
from .pages.oncology_page_logic import *
import time
from .link import link

links=link[1]


@pytest.mark.parametrize('link', links,  scope='function')
def test_base(browser, link):

    link = link + 'accident/oncology/'
    step_1 = Step_1(browser, link)
    step_1.open()
    step_1.close_popaps()
    step_1.step1()
    step_1.go_to_next_step()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.input_full_anketa()
    time.sleep(20)

    step_3 = Step_3(browser, link)
    step_3.should_be_step_3()
    step_3.get_input_code()
    step_3.accept_checkbox()
    if 'https://sogazrelease.support.zetest.site/' not in link and 'http://shop.sogaz.loc/' not in link:
        pay_step = Pay_step(browser, link)
        pay_step.go_to_pay()

