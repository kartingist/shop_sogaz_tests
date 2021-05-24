from selenium.webdriver.common.by import By



class NoAfraidChangeLocators():
    body = (By.CSS_SELECTOR, "body")
    # Попапы
    # _______________________________________________________________________
    popap1 = (By.XPATH, '/html/body/div[9]/div/div/div[1]/button')
    popap2 = (By.CSS_SELECTOR, 'body > div.cookiewrap > div.alert.cookiealert2.d-flex.justify-content-center.show > button')
    popap3 = (By.CSS_SELECTOR, 'body > div.cookiewrap > div.alert.cookiealert.show > div > button')

    # Шаг 1
    # _______________________________________________________________________
    program = (By.CSS_SELECTOR, "#form-step1 > div > div:nth-child(2) > div")
    go_to_step_2 = (By.CSS_SELECTOR, "#step_btn_one > a")

    # Шаг 2
    # заполнение личных данных
    # _______________________________________________________________________
    step_2 = (By.CSS_SELECTOR, "#form-createpolis > div.desigion__item-inner-person.person__block_detail.visible")
    surname = (By.CSS_SELECTOR, "#person1 > div.row.form-group.noPaddings > div:nth-child(1) > input")
    surname_error=(By.XPATH, "(//DIV[@class='invalid-feedback'])[1]")
    firstname = (By.CSS_SELECTOR, "#person1 > div.row.form-group.noPaddings > div:nth-child(2) > input")
    firstname_error = (By.XPATH, '//*[@id="person1"]/div[1]/div[2]/div')
    lastname = (By.CSS_SELECTOR, "#person1 > div.row.form-group.noPaddings > div:nth-child(3) > input")
    lastname_error = (By.XPATH, '//*[@id="person1"]/div[1]/div[3]/div')
    birthday = (By.CSS_SELECTOR, "#person1 > div:nth-child(2) > div.col-sm-3.col-6 > div > input")
    birthday_error = (By.XPATH, '// *[ @ id = "box-birthday0"] / div')
    phone = (By.CSS_SELECTOR, "#person1 > div:nth-child(2) > div.col-sm-3.col-9 > input")
    phone_error = (By.XPATH, '//*[@id="person1"]/div[2]/div[3]/div')
    email = (By.CSS_SELECTOR, "#person1 > div:nth-child(2) > div.col-sm-4.col-9 > input")
    email_error = (By.XPATH, '//*[@id="person1"]/div[2]/div[4]/div')
    passport = (By.CSS_SELECTOR, "#person1 > div.row.align-items-start.form-group > div.col-sm-4.col-xs-12 > input")
    passport_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[1]/div')
    date_start = (By.CSS_SELECTOR, "#person1 > div.row.align-items-start.form-group > div.col-sm-3.col-md-4.col-xs-12 > div > input")
    date_start_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[2]/div/div')
    division = (By.CSS_SELECTOR, "#person1 > div.row.align-items-start.form-group > div.col-sm-4.col-12 > input")
    division_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[3]/div')
    pass_who_give = (By.CSS_SELECTOR, "#person1 > div:nth-child(4) > div > input")
    pass_who_give_error = (By.XPATH, '//*[@id="person1"]/div[4]/div/div')

    # заполнение адреса регистрации
    # _______________________________________________________________________
    person1 = (By.CSS_SELECTOR, "#person1>p") # блок регистрации
    inp_address = (By.CSS_SELECTOR, "#inp_address0>div:nth-child(1)>div.col-sm-4.col-12>span>span.selection>span>span.select2-selection__rendered")
    inp_address_error = (By.XPATH, '')
    city = (By.XPATH, "//INPUT[@class='select2-search__field']")
    select_city = (By.XPATH, "//LI[@class='select2-results__option select2-results__option--highlighted'][1]")
    street = (By.CSS_SELECTOR, "#inp_address0 > div:nth-child(1) > div.col-sm-5.col-12 > input")
    street_error = (By.XPATH, '//*[@id="inp_address0"]/div[1]/div[2]/div')
    index = (By.CSS_SELECTOR, "#inp_address0 > div:nth-child(1) > div.col-sm-3.col-7 > input")
    home = (By.CSS_SELECTOR, "#inp_address0 > div:nth-child(2) > div:nth-child(1) > input")
    home_error = (By.XPATH, '//*[@id="inp_address0"]/div[2]/div[1]/div')
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
    cancel_button = (By.CSS_SELECTOR, '#payment-form > div.btn-group > button:nth-child(2)')
    payment_info = (By.CSS_SELECTOR, "body > div.container > div.payment-info")
    payment_info_message = (By.XPATH, '/html/body/div[1]/div[2]/h2')




