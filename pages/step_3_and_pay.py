from .base_page import BasePage
from .base_locators import Common_Locators
import time

class Step_3(BasePage):
    def should_be_step_3(self):
        assert self.should_be(*Common_Locators.step3), "Не выполнен переход на третий шаг"
        self.scroll_to_element(*Common_Locators.get_code)
        self.wait_element(*Common_Locators.email_confirm)
        # time.sleep(3)

    def get_input_code(self):
        self.selenium_click(*Common_Locators.get_code)
        self.wait_element(*Common_Locators.code)
        self.selenium_input(self.driver.find_element(*Common_Locators.code).text, *Common_Locators.codeConfirm)
        self.selenium_click(*Common_Locators.codeConfirmNext)
        time.sleep(1)
    def accept_checkbox(self):
        self.scroll_to_element(*Common_Locators.checkboxes)
        x = len(self.driver.find_elements(*Common_Locators.checkboxes))
        # Активируем
        for i in range(1, x+1):
            self.driver.execute_script(f"document.getElementById('check{i}').click()")
    def go_to_pay_click(self):
        self.selenium_click(*Common_Locators.step_to_pay)

class Pay_step(BasePage):
    def sbp(self):
        self.element_to_be_clickable(*Common_Locators.card_pay)
        self.selenium_click(*Common_Locators.card_pay)

    def go_to_pay(self):
        time.sleep(4)
        self.wait_element(*Common_Locators.pan)
        assert self.is_element_present(*Common_Locators.pan), "Не выполнен переход на эквайринг'"
        self.js_input('4111 1111 1111 1111', *Common_Locators.pan)
        time.sleep(0.2)
        self.driver.find_element(*Common_Locators.month).send_keys('12')
        self.driver.find_element(*Common_Locators.year).send_keys('26')
        self.js_input('123', *Common_Locators.cvc)
        self.js_click(*Common_Locators.pay_button)

        self.wait_element(*Common_Locators.payment_info)
        # payment_error_failed = self.should_be(*Common_Locators.payment_error_failed)
        payment_success_message= self.should_be(*Common_Locators.payment_success_message)
        # payment_error_suspended= self.should_be(*Common_Locators.payment_error_suspended)
        if payment_success_message == True:
            assert True
        else: assert False, 'Сбой оплаты'



