from selenium.webdriver.common.by import By
class Common_Locators:

    body = (By.CSS_SELECTOR, "body")
    # Попапы
    # _______________________________________________________________________
    popap1 = (By.XPATH, '/html/body/div[9]/div/div/div[1]/button')
    popap2 = (By.CSS_SELECTOR, 'body > div.cookiewrap > div.alert.cookiealert2.d-flex.justify-content-center.show > button')
    popap3 = (By.CSS_SELECTOR, 'body > div.cookiewrap > div.alert.cookiealert.show > div > button')

    # Ввод города
    input_city = (By.XPATH, "/html/body/span/span/span[1]/input")
    select_city = (By.XPATH, "//LI[@class='select2-results__option select2-results__option--highlighted'][1]")

    # Выбор пола
    male = (By.XPATH, "//LI[@role='option'][text()='М']")
    famale = (By.XPATH, "//LI[@role='option'][text()='Ж']")

    # _______________________________________________________________________
    # Шаг 3

    step3 = (By.CSS_SELECTOR, '#step3-ajax_data')

    email_confirm = (By.CSS_SELECTOR, '#step3_inner-confirm > div.desigion__item-inner-email-confirm')
    get_code = (By.CSS_SELECTOR, "#get_code")
    code = (By.CSS_SELECTOR, "#hideOnLock > div > div:nth-child(3) > div > div > div:nth-child(3)")
    codeConfirm = (By.CSS_SELECTOR, "#codeConfirm")
    codeConfirmNext = (By.CSS_SELECTOR, "#codeConfirmNext")

    checkboxes = ((By.XPATH, '//*[@id="step3_inner-confirm"]/div[2]/div/div/div'))
    step_to_pay = (By.CSS_SELECTOR, '#step_btn_3')
    card_pay = (By.CSS_SELECTOR, '#payLink')

    # _______________________________________________________________________
    # Эквайринг

    pan = (By.CSS_SELECTOR, '#pan')
    month = (By.CSS_SELECTOR, '#month')
    year = (By.CSS_SELECTOR, '#year')
    cvc = (By.CSS_SELECTOR, '#cvc')
    pay_button = (By.CSS_SELECTOR, '#payment-form>div.btn-group>button.btn.btn-primary')
    cancel_button = (By.CSS_SELECTOR, '#payment-form > div.btn-group > button:nth-child(2)')
    payment_info = (By.CSS_SELECTOR, "body > div.container > div.payment-info")
    payment_info_message = (By.XPATH, '/html/body/div[1]/div[2]/h2')