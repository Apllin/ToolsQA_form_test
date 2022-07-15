from helpers.pages.student_registration_form_page import StudentRegistrationForm


class ApplicationManager:
    def __init__(self):
        self.student_form = StudentRegistrationForm()


app = ApplicationManager()
