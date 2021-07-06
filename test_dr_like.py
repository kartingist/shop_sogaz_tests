import pytest
from .pages.dr_like.step_1 import *
from .pages.dr_like.step_2 import *
from .pages.step_3_and_pay import *
import time
from .link import link



# links=link[1]

# @pytest.mark.parametrize('link', link,  scope='function')
# # @pytest.mark.parametrize('region', [0, 1, 2], scope='function')
# # @pytest.mark.parametrize('franchise', [50, 30, 20],   scope='function')
# @pytest.mark.parametrize('region', [0], scope='function')
# @pytest.mark.parametrize('franchise', [50],   scope='function')
# def test_full_run(browser, link, region, franchise):
#
#     link = link + 'accident/doctor_like/'
#     step_1 = Step_1(browser, link)
#     step_1.open()
#
#
#     step_1.close_popaps()
#     step_1.step1full(region, franchise)
#
#     step_2 = Step_2(browser, link)
#     step_2.should_be_step_2()
#     step_2.input_full_anketa()
#     time.sleep(3)
#
#     step_3 = Step_3(browser, link)
#     step_3.should_be_step_3()
#     step_3.get_input_code()
#     step_3.accept_checkbox()
#
#
#     if 'https://sogazrelease.support.zetest.site/' not in link and 'http://shop.sogaz.loc/' not in link:
#         pay_step = Pay_step(browser, link)
#         pay_step.sbp()
#         pay_step.go_to_pay()


@pytest.mark.parametrize('link', link,  scope='function')
def test_required_fields(browser, link):

    link = link + 'accident/doctor_like/'
    step_1 = Step_1(browser, link)
    step_1.open()

    step_1.close_popaps()
    step_1.step1base()

    step_2 = Step_2(browser, link)
    step_2.should_be_step_2()
    step_2.anketa_required_fields()

    step_3 = Step_3(browser, link)
    step_3.should_be_step_3()

