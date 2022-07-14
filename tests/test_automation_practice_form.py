from helpers.controls import *
from helpers.helper import *


def test_fill_registrarion_form():
    browser.open("/automation-practice-form")
    remove_elements_on_page()

    browser.element("#firstName").type("John")
    browser.element("#lastName").type("Doe")
    browser.element("#userEmail").type("johndoe@gmail.com")
    browser.element('[for="gender-radio-1"]').click()
    browser.element("#userNumber").type("1337228148")

    date_of_birth = DatePicker(browser.element('#dateOfBirthInput'))
    (date_of_birth
     .select_year(1998)
     .select_month(6)
     .select_day(3))
    # date = DatePicker(browser.element('#dateOfBirthInput')).add_data('03 Jul 1998')

    subject = TagsInput(browser.element('#subjectsInput'))
    subject.add('Hin', autocomplete='Hindi')
    subject.autocomplete('English')

    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text("Music")).click()
    browser.element("#uploadPicture").send_keys(get_abs_path("test.png"))
    browser.element('[placeholder="Current Address"]').type("bla-bla")
    browser.element("#state").scroll_to()

    dropdown = DropDown(browser.element('#state'))
    dropdown.add(from_="NCR")
    dropdown = DropDown(browser.element('#city'))
    dropdown.add(autocomplete_tab="Noida")

    browser.element("div button#submit").press_enter()

    #assertions
    browser.all("//tr/*[last()]").should(have.exact_texts('Values', 'John Doe',
                                                            'johndoe@gmail.com', 'Male', '1337228148', '03 July,1998',
                                                          'Hindi, English', 'Music', 'test.png', 'bla-bla', 'NCR Noida'))

    browser.element("#closeLargeModal").click()

