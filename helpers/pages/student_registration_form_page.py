from selene.support.shared.jquery_style import s
from helpers.controls import *
from helpers.helper import recourse


class StudentRegistrationForm:

    def __init__(self):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.user_email = browser.element("#userEmail")
        self.user_number = browser.element("#userNumber")
        self.gender = browser.element('#genterWrapper')
        self.subjects = TagsInput(browser.element('#subjectsInput'))
        self.submit_button = browser.element('#submit')
        self.hobbies_checkbox = browser.element('#hobbiesWrapper')
        self.add_file = browser.element("#uploadPicture")
        self.address = browser.element('[placeholder="Current Address"]')

    def set_first_name(self, value: str):
        self.first_name.type(value)
        return self

    def set_last_name(self, value: str):
        self.last_name.type(value)
        return self

    def set_user_email(self, value: str):
        self.user_email.type(value)
        return self

    def set_user_number(self, value: str):
        self.user_number.type(value)
        return self

    def add_subjects(self, *values):
        for value in values:
            self.subjects.add(value)
        return self

    def submit(self):
        self.submit_button.press_enter()
        # perform(command.js.click)
        return self

    def set_gender(self, value: str):
        self.gender.all('.custom-radio').element_by(have.exact_text(value)).click()
        return self

    def assert_subjects(self, *names):
        self.subjects.should_have_texts(*names)
        return self


    def set_birthday(self, year, month, day):
        DatePicker().select_year(year).select_month(month).select_day(day)
        return self

    def set_checkbox(self, value: str):
        self.hobbies_checkbox.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def set_picture(self, file: str):
        s('#uploadPicture').send_keys(recourse(file))
        return self

    def set_address(self, address: str):
        self.address.type(address)
        return self

    def set_state(self, value: str):
        DropDown(browser.element('#state')).add(from_=value)
        return self

    def set_city(self, value: str):
        DropDown(browser.element('#city')).add(autocomplete_tab=value)
        return self