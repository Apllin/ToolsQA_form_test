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
        self.element = element.perform(command.js.scroll_into_view)

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
    def __init__(self):
        self.date_of_birth = browser.element('#dateOfBirthInput')


    def add_data(self, option: str):
        self.date_of_birth.perform(command.js.set_value(option)).press_tab()

    def select_year(self, year):
        self.date_of_birth.click()
        browser.element('.react-datepicker__year-select').element(f'[value="{year}"]').click()
        return self

    def select_month(self, month):
        browser.element('.react-datepicker__month-select').element(f'[value="{month}"]').click()
        return self

    def select_day(self, day):
        browser.element(f'.react-datepicker__day--00{day}').click()
        return self
