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

    # Шаг 2
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
    # _______________________________________________________________________
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

class DrLikeStep1:
    birthday_step1 = (By.XPATH, '//*[@id="form-step1"]/div[1]/div[1]/div/div/input')
    region1 = (By.XPATH, '//*[@id="form-step1"]/div[1]/div[3]/div[1]')
    programs = (By.XPATH, '//*[@id="form-step1"]/div[1]/div[5]/div[1]')
    sep1_calc = (By.XPATH, '//*[@id="program"]/div[1]/a')
    tarifs = (By.XPATH, '//*[@id="box-programm"]/div[2]/div')
    box_program = (By.XPATH, '//*[@id="step1"]/form/div[2]/div[1]')
    program1 = (By.XPATH, '//*[@id="step1"]/form/div[2]/div[1]/div[2]/div[1]')
    program2 = (By.XPATH, '//*[@id="step1"]/form/div[2]/div[1]/div[2]/div[2]')
    go_to_step_2 = (By.XPATH, '//*[@id="step1"]/form/div[2]/div[2]/div[2]/div[1]/a')

class DrLikeStep2:
#     Адрес фактического места жительства
    checkbox1 = (By.XPATH, '//*[@id="form-createpolis"]/div[1]/div/div[7]/div[1]/label')


    inp_address = (By.XPATH, "(//SPAN[@class='select2-selection__rendered'])[3]")
    inp_address_error = (By.XPATH, '')
    city = (By.XPATH, "//INPUT[@class='select2-search__field']")
    select_city = (By.XPATH, "//LI[@class='select2-results__option select2-results__option--highlighted'][1]")
    street = (By.XPATH, '//*[@id="form-createpolis"]/div[1]/div/div[7]/div[2]/div[2]/input')
    # street_error = (By.XPATH, '//*[@id="inp_address0"]/div[1]/div[2]/div')
    index = (By.CSS_SELECTOR, "#index02")
    # index_error = (By.XPATH, '//*[@id="inp_address0"]/div[1]/div[3]/div')
    home = (By.CSS_SELECTOR, "#house02")
    # home_error = (By.XPATH, '//*[@id="inp_address0"]/div[2]/div[1]/div')
    korpus = (By.CSS_SELECTOR, "#korpus02")
    building = (By.CSS_SELECTOR, "#building02")
    flat = (By.CSS_SELECTOR, "#flat02")

#     Застрахованный
    checkbox2 = (By.CSS_SELECTOR, '#form-createpolis > div:nth-child(4) > div.form-check.abc-checkbox > label')
class SBP:
    card_pay = (By.CSS_SELECTOR, '#payLink')

class OncologyStep1:
    programs = (By.XPATH, "(//P[@class='desigion__item-inner-td-head line_1'])")
    program1 = (By.XPATH, "(//P[@class='desigion__item-inner-td-head line_1'])[2]")
    program2 = (By.XPATH, "(//P[@class='desigion__item-inner-td-head line_1'])[3]")
    program3 = (By.XPATH, "(//P[@class='desigion__item-inner-td-head line_1'])[4]")
    program4 = (By.XPATH, "(//P[@class='desigion__item-inner-td-head line_1'])[5]")
    go_to_step_2 = (By.CSS_SELECTOR, '#step_btn_1 > a')
class OncologyStep2:
# Застрахованное лицо
    checkbox = (By.CSS_SELECTOR, "#form-desigion > div.form-check.abc-checkbox > label")
    body = (By.CSS_SELECTOR, '#person__body')
    surname = (By.ID, "surname1")
    surname_error = (By.XPATH, "(//DIV[@class='invalid-feedback'])[1]")
    firstname = (By.ID, "firstname1")
    firstname_error = (By.XPATH, '//*[@id="person1"]/div[1]/div[2]/div')
    lastname = (By.ID, "lastname1")
    lastname_error = (By.XPATH, '//*[@id="person1"]/div[1]/div[3]/div')
    sex = (By.XPATH, '//*[@id="select2-sex0-container"]')
    sex_list = (By.XPATH, '//*[@id="select2-sex0-results"]')
    male = (By.XPATH, "//LI[@role='option'][text()='М']")
    famale = (By.XPATH, "//LI[@role='option'][text()='Ж']")
    birthday = (By.ID, "birthday1")
    birthday_error = (By.XPATH, '// *[ @ id = "box-birthday0"] / div')
    phone = (By.ID, "phone1")
    phone_error = (By.XPATH, '//*[@id="person1"]/div[2]/div[3]/div')
    email = (By.ID, "email1")
    email_error = (By.XPATH, '//*[@id="person1"]/div[2]/div[4]/div')
    passport = (By.ID, "pass1")
    passport_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[1]/div')
    date_start = (By.ID, "date_start1")
    date_start_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[2]/div/div')
    division = (By.ID, "division1")
    division_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[3]/div')
    pass_who_give = (By.ID, "pass_who_give1")
    pass_who_give_error = (By.XPATH, '//*[@id="person1"]/div[4]/div/div')
# Застрахованное лицо > Адрес места жительства (регистрации)
# _______________________________________________________________________
    inp_address = (By.CSS_SELECTOR, "#select2-city11-container")
    inp_address_error = (By.XPATH, '')
    city = (By.CSS_SELECTOR, "body > span > span > span.select2-search.select2-search--dropdown > input")
    select_city = (By.XPATH, "//LI[@class='select2-results__option select2-results__option--highlighted'][1]")
    street = (By.CSS_SELECTOR, "#street1")
    street_error = (By.XPATH, '//*[@id="podpisant__container"]/div[5]/div[2]/div')
    index = (By.CSS_SELECTOR, "#index1")
    index_error = (By.XPATH, '//*[@id="inp_address0"]/div[1]/div[3]/div')
    home = (By.CSS_SELECTOR, "#house1")
    home_error = (By.XPATH, '//*[@id="inp_address0"]/div[2]/div[1]/div')
    korpus = (By.CSS_SELECTOR, "#korpus1")
    building = (By.CSS_SELECTOR, "#building1")
    flat = (By.CSS_SELECTOR, "#flat1")
    birth_place = (By.CSS_SELECTOR, "#birth_place")

    go_to_step_3 = (By.CSS_SELECTOR, "#step_btn_2 > a")
class Anketa:
    step_2 = (By.CSS_SELECTOR, "#form-createpolis > div.desigion__item-inner-person.person__block_detail.visible")
    surname = (By.ID, "surname")
    #step2 > form > div:nth-child(3) > div.row.form-group.noPaddings > div:nth-child(1) > input
    surname_error=(By.XPATH, "(//DIV[@class='invalid-feedback'])[1]")
    firstname = (By.ID, "firstname")
    firstname_error = (By.XPATH, '//*[@id="person1"]/div[1]/div[2]/div')
    lastname = (By.ID, "lastname")
    lastname_error = (By.XPATH, '//*[@id="person1"]/div[1]/div[3]/div')
    sex = (By.XPATH, '//*[@id="select2-sex0-container"]')
    sex_list = (By.XPATH, '//*[@id="select2-sex0-results"]')
    male = (By.XPATH, "//LI[@role='option'][text()='М']")
    famale = (By.XPATH, "//LI[@role='option'][text()='Ж']")
    birthday = (By.ID, "birthday")
    birthday_error = (By.XPATH, '// *[ @ id = "box-birthday0"] / div')
    phone = (By.ID, "phone")
    phone_error = (By.XPATH, '//*[@id="person1"]/div[2]/div[3]/div')
    email = (By.ID, "email")
    email_error = (By.XPATH, '//*[@id="person1"]/div[2]/div[4]/div')
    passport = (By.ID, "pass")
    passport_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[1]/div')
    date_start = (By.ID, "date_start")
    date_start_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[2]/div/div')
    division = (By.ID, "division")
    division_error = (By.XPATH, '//*[@id="person1"]/div[3]/div[3]/div')
    pass_who_give = (By.ID, "pass_who_give")
    pass_who_give_error = (By.XPATH, '//*[@id="person1"]/div[4]/div/div')

    # заполнение адреса регистрации
    # _______________________________________________________________________
    person1 = (By.CSS_SELECTOR, "#form-createpolis > div:nth-child(3) > div > p") # блок регистрации
    inp_address = (By.CSS_SELECTOR, "#select2-city1-container")
    inp_address_error = (By.XPATH, '')
    city = (By.CSS_SELECTOR, "body > span > span > span.select2-search.select2-search--dropdown > input")
    select_city = (By.XPATH, "//LI[@class='select2-results__option select2-results__option--highlighted'][1]")
    street = (By.CSS_SELECTOR, "#street")
    street_error = (By.XPATH, '//*[@id="podpisant__container"]/div[5]/div[2]/div')
    index = (By.CSS_SELECTOR, "#index")
    index_error = (By.XPATH, '//*[@id="inp_address0"]/div[1]/div[3]/div')
    home = (By.CSS_SELECTOR, "#house")
    home_error = (By.XPATH, '//*[@id="inp_address0"]/div[2]/div[1]/div')
    korpus = (By.CSS_SELECTOR, "#korpus")
    building = (By.CSS_SELECTOR, "#building")
    flat = (By.CSS_SELECTOR, "#flat")
    birth_place = (By.CSS_SELECTOR, "#birth_place")











