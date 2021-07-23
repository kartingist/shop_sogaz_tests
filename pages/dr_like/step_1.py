from .locators import *
from ..base_page import BasePage



class Step_1(BasePage):

    def step1full(self, region, franchise):
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
            self.selenium_click(*DrLikeLocators.go_to_step_2)

    def step1base(self):
        self.js_input('03081994', *DrLikeLocators.birthday_step1)
        self.driver.execute_script(f"document.getElementById('at_work{0}').click()")
        self.driver.execute_script(f"document.getElementById('franchise{50}').click()")
        self.selenium_click(*DrLikeLocators.sep1_calc)
        if self.cnt(*DrLikeLocators.tarifs)==0:
            assert False, 'Отсутствуют программы страхования'
        else:
            self.wait_element(*DrLikeLocators.box_program)
            self.selenium_click(*DrLikeLocators.program1)
            self.scroll_to_element(*DrLikeLocators.go_to_step_2)
            self.selenium_click(*DrLikeLocators.go_to_step_2)

