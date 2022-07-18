from helpers.pages.student_registration_form_page import *


class StudentRegistrationSteps:
    def __init__(self):
        self.form = StudentRegistrationForm()

    def fill_form(self, first_name, last_name, email, number, *values):
        self.form.set_first_name(first_name)
        self.form.set_last_name(last_name)
        self.form.set_user_email(email)
        self.form.set_user_number(number)
        self.form.set_radiobutton()
        self.form.add_subjects(*values)

        return self
