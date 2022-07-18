from helpers.controls import *
from helpers.helper import get_abs_path


class StudentRegistrationForm:

    def __init__(self):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.user_email = browser.element("#userEmail")
        self.user_number = browser.element("#userNumber")
        self.radiobutton = browser.element('[for="gender-radio-1"]')
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

    def set_radiobutton(self):
        self.radiobutton.click()
        return self

    def assert_subjects(self, *names):
        self.subjects.should_have_texts(*names)
        return self

    # def set_birthday(self):
    #     DatePicker(1998, 6, 3).select_year().select_month().select_day()
    #     return self

    def set_birthday(self, year, month, day):
        DatePicker().select_year(year).select_month(month).select_day(day)
        return self

    def set_checkbox(self, value: str):
        self.hobbies_checkbox.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def set_picture(self, name: str):
        self.add_file.send_keys(get_abs_path(name))
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
