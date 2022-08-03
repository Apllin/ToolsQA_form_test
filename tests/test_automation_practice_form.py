from helpers.controls import *
from helpers.helper import *
from helpers.steps.app_manager import app, form
import allure

def test_fill_registration_form(setup_browser):
    browser = setup_browser
    with allure.step("Open registration form"):
        browser.open("/automation-practice-form")
        remove_elements_on_page()
    with allure.step("Fill form"):
        form.steps_fill_form.fill_form("John", "Doe", "johndoe@gmail.com", "1337228148", "Male", 'Hindi', 'English')

        (app.page_student_form
         .set_birthday(1998, 6, 3)
         .set_checkbox("Music")
         .set_picture("test.png")
         .set_address("bla-bla")
         .set_state("NCR")
         .set_city("Noida")
         .submit()
         )

    with allure.step("Check form results"):
        browser.all("//tr/*[last()]").should(have.exact_texts('Values', 'John Doe',
                                                            'johndoe@gmail.com', 'Male', '1337228148', '03 July,1998',
                                                          'Hindi, English', 'Music', 'test.png', 'bla-bla', 'NCR Noida'))

    browser.element("#closeLargeModal").click()
