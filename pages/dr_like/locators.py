from selenium.webdriver.common.by import By



class DrLikeLocators:
    body = (By.CSS_SELECTOR, "body")
    # Попапы
    # _______________________________________________________________________
    popap1 = (By.XPATH, '/html/body/div[9]/div/div/div[1]/button')
    popap2 = (By.CSS_SELECTOR, 'body > div.cookiewrap > div.alert.cookiealert2.d-flex.justify-content-center.show > button')
    popap3 = (By.CSS_SELECTOR, 'body > div.cookiewrap > div.alert.cookiealert.show > div > button')

#     Шаг 1
    birthday_step1 = (By.XPATH, '//*[@id="form-step1"]/div[1]/div[1]/div/div/input')
    region1 = (By.XPATH, '//*[@id="form-step1"]/div[1]/div[3]/div[1]')
    programs = (By.XPATH, '//*[@id="form-step1"]/div[1]/div[5]/div[1]')
    sep1_calc = (By.XPATH, '//*[@id="program"]/div[1]/a')
    tarifs = (By.XPATH, '//*[@id="box-programm"]/div[2]/div')
    box_program = (By.XPATH, '//*[@id="step1"]/form/div[2]/div[1]')
    program1 = (By.XPATH, '//*[@id="step1"]/form/div[2]/div[1]/div[2]/div[1]')
    program2 = (By.XPATH, '//*[@id="step1"]/form/div[2]/div[1]/div[2]/div[2]')
    go_to_step_2 = (By.XPATH, '//*[@id="step1"]/form/div[2]/div[2]/div[2]/div[1]/a')

#     Шаг 2
#     Страхователь

    step_2 = (By.CSS_SELECTOR, '#form-createpolis > div:nth-child(3)')
    surname0 = (By.CSS_SELECTOR, '#surname0')
    surname0_error = (By.XPATH, '//*[@id="person0"]/div[1]/div[1]/div')

    firstname0 = (By.CSS_SELECTOR, '#firstname0')
    firstname0_error = (By.XPATH, '//*[@id="person0"]/div[1]/div[2]/div')

    lastname0 = (By.CSS_SELECTOR, '#lastname0')
    lastname0_error = (By.XPATH, '//*[@id="person0"]/div[1]/div[3]/div')


    sex0 = (By.CSS_SELECTOR, '#select2-sex0-container')
    sex_list0 = (By.XPATH, '#select2-sex0-results')

    birthday0 = (By.CSS_SELECTOR, '#birthday0')
    birthday0_error = (By.XPATH, '//*[@id="box-birthday0"]/label')

    phone0 = (By.CSS_SELECTOR, '#phone0')
    phone0_error = (By.XPATH, '//*[@id="person0"]/div[2]/div[3]/div')

    email= (By.CSS_SELECTOR, '#email')
    email_error = (By.XPATH, '//*[@id="person0"]/div[2]/div[4]/div')

    pass0 = (By.CSS_SELECTOR, '#pass0')
    pass0_error = (By.XPATH, '//*[@id="person0"]/div[3]/div[1]/div')

    date_start0 = (By.CSS_SELECTOR, '#date_start0')
    date_start0_error= (By.XPATH, '//*[@id="person0"]/div[3]/div[2]/div/div')

    division0 = (By.CSS_SELECTOR, '#division0')
    division0_error = (By.XPATH, '//*[@id="person0"]/div[3]/div[3]/div')

    pass_who_give0 = (By.CSS_SELECTOR, '#pass_who_give0')
    pass_who_give0_error = (By.XPATH, '//*[@id="person0"]/div[4]/div/div')

    # Адрес регистрации страхователя

    inp_address0 = (By.CSS_SELECTOR, "#select2-city0-container")
    inp_address_error0 = (By.CSS_SELECTOR, '#inp_address0 > div:nth-child(1) > div.col-sm-4.col-12 > div')
    input_city0 = (By.XPATH, "/html/body/span/span/span[1]/input")
    select_city0 = (By.XPATH, "//LI[@class='select2-results__option select2-results__option--highlighted'][1]")

    street0 = (By.CSS_SELECTOR, '#street0')
    street0_error = (By.XPATH, '//*[@id="inp_address0"]/div[1]/div[2]/div')

    index0 = (By.CSS_SELECTOR, '#index0')
    index0_error = (By.XPATH, '//*[@id="inp_address0"]/div[1]/div[3]/div')

    house0 = (By.CSS_SELECTOR, '#house0')
    house0_error = (By.XPATH, '//*[@id="inp_address0"]/div[2]/div[1]/div')

    korpus0 = (By.CSS_SELECTOR, '#korpus0')
    korpus0_error = (By.XPATH, '//*[@id="inp_address0"]/div[2]/div[2]/div')

    building0 = (By.CSS_SELECTOR, '#building0')
    building0_error = (By.XPATH, '//*[@id="inp_address0"]/div[2]/div[3]/div')

    flat0 = (By.CSS_SELECTOR, '#flat0')
    flat0_error = (By.XPATH, '//*[@id="inp_address0"]/div[3]/div[4]/div')

    birth_place0 = (By.CSS_SELECTOR, '#birth_place0')
    birth_place0_error = (By.XPATH, '//*[@id="person0"]/div[6]/div/div')

    # Адрес фактического места жительства страхователя

    checkbox1= (By.CSS_SELECTOR, '#live_place_block_0 > div.form-check.abc-checkbox > label')

    inp_address02 = (By.CSS_SELECTOR, "#select2-city02-container")
    inp_address_error02 = (By.XPATH, '//*[@id="live_place_block_0"]/div[2]/div[1]/div')
    input_city = (By.XPATH, "/html/body/span/span/span[1]/input")
    select_city = (By.XPATH, "//LI[@class='select2-results__option select2-results__option--highlighted'][1]")

    street02 = (By.CSS_SELECTOR, '#street02')
    street02_error = (By.XPATH, '//*[@id="live_place_block_0"]/div[2]/div[2]/div')

    index02 = (By.CSS_SELECTOR, '#index02')
    index02_error = (By.XPATH, '//*[@id="live_place_block_0"]/div[1]/div[3]/div')

    house02 = (By.CSS_SELECTOR, '#house02')
    house02_error = (By.XPATH, '//*[@id="live_place_block_0"]/div[2]/div[1]/div')

    korpus02 = (By.CSS_SELECTOR, '#korpus02')
    korpus02_error = (By.XPATH, '//*[@id="live_place_block_0"]/div[2]/div[2]/div')

    building02 = (By.CSS_SELECTOR, '#building02')
    building02_error = (By.XPATH, '//*[@id="live_place_block_0"]/div[2]/div[3]/div')

    flat02 = (By.CSS_SELECTOR, '#flat02')
    flat02_error = (By.XPATH, '//*[@id="live_place_block_0"]/div[3]/div[4]/div')

    # _________________________________________________________________________
    # Застрахованный
    surname1 = (By.CSS_SELECTOR, '#surname1')
    surname1_error = (By.XPATH, '//*[@id="person1"]/div[1]/div[1]/div')

    firstname1 = (By.CSS_SELECTOR, '#firstname1')
    firstname1_error = (By.XPATH, '//*[@id="person1"]/div[1]/div[2]/div')

    lastname1 = (By.CSS_SELECTOR, '#lastname1')
    lastname1_error = (By.XPATH, '//*[@id="person1"]/div[1]/div[3]/div')

    sex1 = (By.CSS_SELECTOR, '#select2-sex1-container')
    sex_list1 = (By.XPATH, '#select2-sex1-results')

    birthday1 = (By.CSS_SELECTOR, '#birthday1')
    birthday1_error = (By.XPATH, '//*[@id="box-birthday1"]/label')

    phone1 = (By.CSS_SELECTOR, '#phone1')
    phone1_error = (By.XPATH, '//*[@id="person1"]/div[2]/div[3]/div')

    email1 = (By.CSS_SELECTOR, '#email1')
    email1_error = (By.XPATH, '//*[@id="person1"]/div[2]/div[4]/div')

    type_doc= (By.CSS_SELECTOR, '#select2-document1-container')

    pass1 = (By.CSS_SELECTOR, '#pass1')
    pass1_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[1]/div')

    date_start1 = (By.CSS_SELECTOR, '#date_start1')
    date_start1_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[2]/div/div')

    division1 = (By.CSS_SELECTOR, '#division1')
    division1_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[3]/div')

    pass_who_give1 = (By.CSS_SELECTOR, '#pass_who_give1')
    pass_who_give1_error = (By.XPATH, '//*[@id="person1"]/div[4]/div/div')

    # Адрес регистрации застрахованного

    inp_address1 = (By.CSS_SELECTOR, "#select2-city1-container")
    inp_address_error1 = (By.CSS_SELECTOR, '#inp_address1 > div:nth-child(1) > div.col-sm-4.col-12 > div')
    input_city1 = (By.XPATH, "/html/body/span/span/span[1]/input")
    select_city1 = (By.XPATH, "//LI[@class='select2-results__option select2-results__option--highlighted'][1]")

    street1 = (By.CSS_SELECTOR, '#street1')
    street1_error = (By.XPATH, '//*[@id="inp_address1"]/div[1]/div[2]/div')

    index1 = (By.CSS_SELECTOR, '#index1')
    index1_error = (By.XPATH, '//*[@id="inp_address1"]/div[1]/div[3]/div')

    house1 = (By.CSS_SELECTOR, '#house1')
    house1_error = (By.XPATH, '//*[@id="inp_address1"]/div[2]/div[1]/div')

    korpus1 = (By.CSS_SELECTOR, '#korpus1')
    korpus1_error= (By.XPATH, '//*[@id="inp_address1"]/div[2]/div[2]/div')

    building1 = (By.CSS_SELECTOR, '#building1')
    building1_error = (By.XPATH, '//*[@id="inp_address1"]/div[2]/div[3]/div')

    flat1 = (By.CSS_SELECTOR, '#flat1')
    flat1_error = (By.XPATH, '//*[@id="inp_address1"]/div[3]/div[4]/div')

    birth_place1 = (By.CSS_SELECTOR, '#birth_place1')
    birth_place1_error = (By.XPATH, '//*[@id="person1"]/div[6]/div/div')

    # Адрес фактического места жительства застрахованного

    checkbox2 = (By.CSS_SELECTOR, '#live_place_block_1 > div.form-check.abc-checkbox > label')

    inp_address12 = (By.CSS_SELECTOR, "#select2-city12-container")
    inp_address_error12 = (By.XPATH, '//*[@id="live_place_block_1"]/div[2]/div[1]/div')
    input_city12 = (By.XPATH, "/html/body/span/span/span[1]/input")
    select_city12 = (By.XPATH, "//LI[@class='select2-results__option select2-results__option--highlighted'][1]")

    street12 = (By.CSS_SELECTOR, '#street12')
    street12_error = (By.XPATH, '//*[@id="live_place_block_1"]/div[2]/div[2]/div')

    index12 = (By.CSS_SELECTOR, '#index12')
    index12_error = (By.XPATH, '//*[@id="live_place_block_1"]/div[1]/div[3]/div')

    house12 = (By.CSS_SELECTOR, '#house12')
    house12_error = (By.XPATH, '//*[@id="live_place_block_1"]/div[2]/div[1]/div')

    korpus12 = (By.CSS_SELECTOR, '#korpus12')
    korpus12_error = (By.XPATH, '//*[@id="live_place_block_1"]/div[2]/div[2]/div')

    building12 = (By.CSS_SELECTOR, '#building12')
    building12_error = (By.XPATH, '//*[@id="live_place_block_1"]/div[2]/div[3]/div')

    flat12 = (By.CSS_SELECTOR, '#flat12')
    flat12_error = (By.XPATH, '//*[@id="live_place_block_1"]/div[3]/div[4]/div')

    go_to_step3 = (By.CSS_SELECTOR, '#step_btn_2 > a')

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
    card_pay = (By.CSS_SELECTOR, '#payLink')

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




















