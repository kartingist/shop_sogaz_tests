import pytest
from .pages.dr_like.dr_like_page_logic import *
import time
from .link import link



# links=link[1]

# оставим до лучших времен...

@pytest.mark.parametrize('link', link,  scope='function')
@pytest.mark.parametrize('region', [0, 1, 2], scope='function')
@pytest.mark.parametrize('franchise', [50, 30, 20],   scope='function')
# @pytest.mark.parametrize('region', [0], scope='function')
# @pytest.mark.parametrize('franchise', [50],   scope='function')
def test_base(browser, link, region, franchise):

    link = link + 'accident/doctor_like/'
    step_1 = Step_1(browser, link)
    step_1.open()


    step_1.close_popaps()
    step_1.step1(region, franchise)


    step_1.go_to_next_step()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.input_full_anketa()
    time.sleep(3)

    step_3 = Step_3(browser, link)
    step_3.should_be_step_3()
    step_3.get_input_code()
    step_3.accept_checkbox()

    pay_step = Pay_step(browser, link)
    pay_step.sbp()
    if 'https://sogazrelease.support.zetest.site/' not in link and 'http://shop.sogaz.loc/' not in link:
        pay_step.go_to_pay()

