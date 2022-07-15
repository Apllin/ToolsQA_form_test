from selene import have, command
from selene.core.entity import Element
from selene.support.shared import browser
from typing import Optional


class TagsInput:
    def __init__(self, element: Element):
        self.element = element
        self.container = self.element.element(
            './ancestor::*[contains(@id, "Wrapper")]'
        )
        self.value_labels = self.container.all(
            '[class*=-auto-complete__multi-value__label]'
        )

    def add(self, from_: str, autocomplete: Optional[str] = None):
        self.element.type(from_)
        browser.all(
            '.subjects-auto-complete__option'
        ).element_by(have.text(autocomplete or from_)).click()

    def autocomplete(self, from_: str):
        self.element.type(from_).press_tab()

    def should_have_texts(self, *values):
        self.value_labels.should(have.exact_texts(*values))


class DropDown:
    def __init__(self, element: Element):
        self.element = element

    def add(self, from_: Optional[str] = None, autocomplete_tab: Optional[str] = None):
        if from_:
            self.element.click()
            browser.all(
                "[id^=react-select-][id*=-option]").element_by(have.exact_text(from_)).click()
        elif autocomplete_tab:
            self.element.element(
                '[id^=react-select-][id*=-input]'
            ).type(autocomplete_tab).press_enter()


class DatePicker:
    def __init__(self, year, month, day):
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.year = year
        self.month = month
        self.day = day

    def add_data(self, option: str):
        self.date_of_birth.perform(command.js.set_value(option)).press_tab()

    def select_year(self):
        self.date_of_birth.click()
        browser.element('.react-datepicker__year-select').element(f'[value="{self.year}"]').click()
        return self

    def select_month(self):
        browser.element('.react-datepicker__month-select').element(f'[value="{self.month}"]').click()
        return self

    def select_day(self):
        browser.element(f'.react-datepicker__day--00{self.day}').click()
        return self
