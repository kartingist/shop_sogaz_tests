import pytest
from .link import link

from .pages.no_afraid_page import *
import time

link=link[1]
@pytest.mark.parametrize('link', link,  scope='function')
def test_opensite(browser, link):

    link = link + 'accident/no_afraid_change/#'
    step_1 = Step_1(browser, link)
    step_1.open()
    step_1.close_popaps()
    step_1.go_to_next_step()
    # time.sleep(5)
    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.input_first_block_FIO()
    step_3 = Step_3(browser, link)
    step_3.should_be_step_3()
    step_3.get_input_code()
    step_3.accept_checkbox()
    pay_step = Pay_step(browser, link)
    pay_step.go_to_pay()
    time.sleep(10)
