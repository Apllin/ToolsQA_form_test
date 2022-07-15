from helpers.controls import *
from helpers.helper import *
from helpers.steps.app_manager import app


def test_fill_registrarion_form():
    browser.open("/automation-practice-form")
    remove_elements_on_page()

    (app.student_form
     .fill_form("John", "Doe", "johndoe@gmail.com", "1337228148", 'Hindi', 'English')
     .set_birthday()
     .set_checkbox("Music")
     .set_picture("test.png")
     .set_address("bla-bla")
     )

    browser.element("#state").scroll_to()

    (app.student_form
     .set_state("NCR")
     .set_city("Noida")
     .submit()
     )


    #assertions
    browser.all("//tr/*[last()]").should(have.exact_texts('Values', 'John Doe',
                                                            'johndoe@gmail.com', 'Male', '1337228148', '03 July,1998',
                                                          'Hindi, English', 'Music', 'test.png', 'bla-bla', 'NCR Noida'))

    browser.element("#closeLargeModal").click()

