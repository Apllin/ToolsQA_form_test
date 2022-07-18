from helpers.pages.student_registration_form_page import StudentRegistrationForm
from helpers.steps.student_registration_steps import StudentRegistrationSteps


class ApplicationManager:
    def __init__(self):
        self.page_student_form = StudentRegistrationForm()
        self.steps_fill_form = StudentRegistrationSteps()


app = ApplicationManager()
form = ApplicationManager()
