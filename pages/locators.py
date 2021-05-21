from selenium.webdriver.common.by import By



class NoAfraidChangeLocators():
    body = (By.CSS_SELECTOR, "body")
    # Попапы
    # _______________________________________________________________________
    popap1 = (By.CSS_SELECTOR, 'body > div.cookiewrap > div.alert.cookiealert2.d-flex.justify-content-center.show > button')
    popap2 = (By.CSS_SELECTOR, 'body > div.cookiewrap > div.alert.cookiealert.show > div > button')

    # Шаг 1
    # _______________________________________________________________________
    program = (By.CSS_SELECTOR, "#form-step1 > div > div:nth-child(2) > div")
    go_to_step_2 = (By.CSS_SELECTOR, "#step_btn_one > a")

    # Шаг 2
    # заполнение личных данных
    # _______________________________________________________________________
    surname = (By.CSS_SELECTOR, "#person1 > div.row.form-group.noPaddings > div:nth-child(1) > input")
    firstname = (By.CSS_SELECTOR, "#person1 > div.row.form-group.noPaddings > div:nth-child(2) > input")
    lastname = (By.CSS_SELECTOR, "#person1 > div.row.form-group.noPaddings > div:nth-child(3) > input")
    birthday = (By.CSS_SELECTOR, "#person1 > div:nth-child(2) > div.col-sm-3.col-6 > div > input")
    phone = (By.CSS_SELECTOR, "#person1 > div:nth-child(2) > div.col-sm-3.col-9 > input")
    email = (By.CSS_SELECTOR, "#person1 > div:nth-child(2) > div.col-sm-4.col-9 > input")
    passport = (By.CSS_SELECTOR, "#person1 > div.row.align-items-start.form-group > div.col-sm-4.col-xs-12 > input")
    date_start = (By.CSS_SELECTOR, "#person1 > div.row.align-items-start.form-group > div.col-sm-3.col-md-4.col-xs-12 > div > input")
    division = (By.CSS_SELECTOR, "#person1 > div.row.align-items-start.form-group > div.col-sm-4.col-12 > input")
    pass_who_give = (By.CSS_SELECTOR, "#person1 > div:nth-child(4) > div > input")
    # заполнение адреса регистрации
    # _______________________________________________________________________

    person1 = (By.CSS_SELECTOR, "#person1>p") # блок регистрации
    inp_address = (By.CSS_SELECTOR, "#inp_address0>div:nth-child(1)>div.col-sm-4.col-12>span>span.selection>span>span.select2-selection__rendered")
    city = (By.XPATH, "//INPUT[@class='select2-search__field']")
    select_city = (By.XPATH, "//LI[@class='select2-results__option select2-results__option--highlighted'][1]")
    street = (By.CSS_SELECTOR, "#inp_address0 > div:nth-child(1) > div.col-sm-5.col-12 > input")
    index = (By.CSS_SELECTOR, "#inp_address0 > div:nth-child(1) > div.col-sm-3.col-7 > input")
    home = (By.CSS_SELECTOR, "#inp_address0 > div:nth-child(2) > div:nth-child(1) > input")
    korpus = (By.CSS_SELECTOR, "#inp_address0 > div:nth-child(2) > div:nth-child(2) > input")
    building = (By.CSS_SELECTOR, "#inp_address0 > div:nth-child(2) > div:nth-child(3) > input")
    flat = (By.CSS_SELECTOR, "#inp_address0 > div:nth-child(2) > div:nth-child(4) > input")
    birth_place = (By.CSS_SELECTOR, "#person1 > div:nth-child(8) > div > input")
    personal_code = (By.CSS_SELECTOR, "#person1 > div:nth-child(9) > div > input")
    go_to_step_3 = (By.CSS_SELECTOR, "#form-createpolis>div.buttons_bottom>div.buy.choose>a")

    # Шаг 3
    # заполнение личных данных
    # _______________________________________________________________________
    item_iner_step_3 = (By.CSS_SELECTOR, '#step3')
    email_confirm = (By.CSS_SELECTOR, '#step3_inner-confirm > div.desigion__item-inner-email-confirm')
    get_code = (By.CSS_SELECTOR, "#get_code")
    code = (By.CSS_SELECTOR, "#hideOnLock > div > div:nth-child(3) > div > div > div:nth-child(3)")
    codeConfirm = (By.CSS_SELECTOR, "#codeConfirm")
    codeConfirmNext = (By.CSS_SELECTOR, "#codeConfirmNext")

    checkboxes = ((By.XPATH, '//*[@id="step3_inner-confirm"]/div[2]/div/div/div'))
    step_to_pay = (By.CSS_SELECTOR, '#step_btn_3')
    # Эквайринг
    # _______________________________________________________________________
    pan = (By.CSS_SELECTOR, '#pan')
    month = (By.CSS_SELECTOR, '#month')
    year = (By.CSS_SELECTOR, '#year')
    cvc = (By.CSS_SELECTOR, '#cvc')
    pay_button = (By.CSS_SELECTOR, '#payment-form>div.btn-group>button.btn.btn-primary')
    payment_info = (By.CSS_SELECTOR, "body > div.container > div.payment-info")
    payment_info_message = (By.XPATH, '/html/body/div[1]/div[2]/h2')




