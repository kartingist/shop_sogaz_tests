from selenium.webdriver.common.by import By



class NoAfraidChangeLocators:
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

    # # Шаг 2 (new)
    # # заполнение личных данных
    # # _______________________________________________________________________
    # step_2 = (By.CSS_SELECTOR, "#step2")
    # surname = (By.CSS_SELECTOR, "#person0surname")
    # surname_error=(By.CSS_SELECTOR, "#person1 > div.row.form-group.noPaddings > div:nth-child(1) > div")
    # firstname = (By.CSS_SELECTOR, "#person0firstname")
    # firstname_error = (By.CSS_SELECTOR, '#person1 > div.row.form-group.noPaddings > div:nth-child(2) > div')
    # lastname = (By.CSS_SELECTOR, "#person0lastname")
    # lastname_error = (By.CSS_SELECTOR, '#person1 > div.row.form-group.noPaddings > div:nth-child(3) > div')
    # sex = (By.CSS_SELECTOR, '#select2-person0sex-container')
    # sex_list = (By.XPATH, '//*[@id="select2-person0sex-results"]')
    # male = (By.XPATH, "//LI[@role='option'][text()='М']")
    # famale = (By.XPATH, "//LI[@role='option'][text()='Ж']")
    # birthday = (By.CSS_SELECTOR, "#person0birthday")
    # birthday_error = (By.XPATH, '// *[ @ id = "box-birthday0"] / div')
    # phone = (By.CSS_SELECTOR, "#person0phone")
    # phone_error = (By.XPATH, '//*[@id="person1"]/div[2]/div[3]/div')
    # email = (By.CSS_SELECTOR, "#person0email")
    # email_error = (By.XPATH, '//*[@id="person1"]/div[2]/div[4]/div')
    # passport = (By.CSS_SELECTOR, "#person0pass")
    # passport_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[1]/div')
    # date_start = (By.CSS_SELECTOR, "#person0date_start")
    # date_start_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[2]/div/div')
    # division = (By.CSS_SELECTOR, "#person0division")
    # division_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[3]/div')
    # pass_who_give = (By.CSS_SELECTOR, "#person0pass_who_give")
    # pass_who_give_error = (By.XPATH, '//*[@id="person1"]/div[4]/div/div')
    #
    # # заполнение адреса регистрации
    # person1 = (By.CSS_SELECTOR, "#person1>p") # блок регистрации
    # inp_address = (By.CSS_SELECTOR, "#inp_address0 > div:nth-child(1) > div.col-sm-4.col-12 > span > span.selection > span")
    # inp_address_error = (By.CSS_SELECTOR, '#inp_address0 > div:nth-child(1) > div.col-sm-4.col-12 > div')
    # city = (By.XPATH, "//INPUT[@class='select2-search__field']")
    # select_city = (By.XPATH, "//LI[@class='select2-results__option select2-results__option--highlighted'][1]")
    # street = (By.CSS_SELECTOR, "#person0street")
    # street_error = (By.XPATH, '//*[@id="inp_address0"]/div[1]/div[2]/div')
    # index = (By.CSS_SELECTOR, "#person0index")
    # index_error = (By.XPATH, '//*[@id="inp_address0"]/div[1]/div[3]/div')
    # home = (By.CSS_SELECTOR, "#person0house")
    # home_error = (By.XPATH, '//*[@id="inp_address0"]/div[2]/div[1]/div')
    # korpus = (By.CSS_SELECTOR, "#person0korpus")
    # building = (By.CSS_SELECTOR, "#person0building")
    # flat = (By.CSS_SELECTOR, "#person0flat")
    # birth_place = (By.CSS_SELECTOR, "#person0birth_place")
    # personal_code = (By.CSS_SELECTOR, "#person0personal_code")
    # personal_code_error = (By.CSS_SELECTOR, "#person1 > div:nth-child(9) > div > div")
    # go_to_step_3 = (By.CSS_SELECTOR, "#form-createpolis>div.buttons_bottom>div.buy.choose>a")

    # Шаг 2 (old)
    # заполнение личных данных
    # _______________________________________________________________________
    step_2 = (By.CSS_SELECTOR, "#step2")
    surname = (By.CSS_SELECTOR, "#surname")
    surname_error=(By.CSS_SELECTOR, "#person1 > div.row.form-group.noPaddings > div:nth-child(1) > div")
    firstname = (By.CSS_SELECTOR, "#firstname")
    firstname_error = (By.CSS_SELECTOR, '#person1 > div.row.form-group.noPaddings > div:nth-child(2) > div')
    lastname = (By.CSS_SELECTOR, "#lastname")
    lastname_error = (By.CSS_SELECTOR, '#person1 > div.row.form-group.noPaddings > div:nth-child(3) > div')
    sex = (By.CSS_SELECTOR, '#select2-sex-container')
    sex_list = (By.XPATH, '//*[@id="select2-sex-results"]')
    male = (By.XPATH, "//LI[@role='option'][text()='М']")
    famale = (By.XPATH, "//LI[@role='option'][text()='Ж']")
    birthday = (By.CSS_SELECTOR, "#birthday")
    birthday_error = (By.XPATH, '// *[ @ id = "box-birthday0"] / div')
    phone = (By.CSS_SELECTOR, "#phone")
    phone_error = (By.XPATH, '//*[@id="person1"]/div[2]/div[3]/div')
    email = (By.CSS_SELECTOR, "#email")
    email_error = (By.XPATH, '//*[@id="person1"]/div[2]/div[4]/div')
    passport = (By.CSS_SELECTOR, "#pass")
    passport_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[1]/div')
    date_start = (By.CSS_SELECTOR, "#date_start")
    date_start_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[2]/div/div')
    division = (By.CSS_SELECTOR, "#division")
    division_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[3]/div')
    pass_who_give = (By.CSS_SELECTOR, "#pass_who_give")
    pass_who_give_error = (By.XPATH, '//*[@id="person1"]/div[4]/div/div')

    # заполнение адреса регистрации
    person1 = (By.CSS_SELECTOR, "#person1>p") # блок регистрации
    inp_address = (By.CSS_SELECTOR, "#inp_address0 > div:nth-child(1) > div.col-sm-4.col-12 > span > span.selection > span")
    inp_address_error = (By.CSS_SELECTOR, '#inp_address0 > div:nth-child(1) > div.col-sm-4.col-12 > div')
    city = (By.XPATH, "//INPUT[@class='select2-search__field']")
    select_city = (By.XPATH, "//LI[@class='select2-results__option select2-results__option--highlighted'][1]")
    street = (By.CSS_SELECTOR, "#street")
    street_error = (By.XPATH, '//*[@id="inp_address0"]/div[1]/div[2]/div')
    index = (By.CSS_SELECTOR, "#index")
    index_error = (By.XPATH, '//*[@id="inp_address0"]/div[1]/div[3]/div')
    home = (By.CSS_SELECTOR, "#house")
    home_error = (By.XPATH, '//*[@id="inp_address0"]/div[2]/div[1]/div')
    korpus = (By.CSS_SELECTOR, "#korpus")
    building = (By.CSS_SELECTOR, "#building")
    flat = (By.CSS_SELECTOR, "#flat")
    birth_place = (By.CSS_SELECTOR, "#birth_place")
    personal_code = (By.CSS_SELECTOR, "#personal_code")
    personal_code_error = (By.CSS_SELECTOR, "#person1 > div:nth-child(9) > div > div")
    go_to_step_3 = (By.CSS_SELECTOR, "#form-createpolis>div.buttons_bottom>div.buy.choose>a")

    # Шаг 3
    # заполнение личных данных
    # _______________________________________________________________________
    step3 = (By.CSS_SELECTOR, '#step3-ajax_data')
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










