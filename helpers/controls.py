from selene import have, command
from selene.core.entity import Element
from selene.support.shared import browser
from typing import Optional

class TagsInput:
    def __init__(self, element: Element):
        self.element = element

    def add(self, from_: str, autocomplete: Optional[str] = None):
        self.element.type(from_)
        browser.all(
            '.subjects-auto-complete__option'
        ).element_by(have.text(autocomplete or from_)).click()


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
    def __init__(self, element: Element):
        self.element = element


    def add_data(self, option: str):
        self.element.perform(command.js.set_value(option)).press_tab()

    def select_year(self, option: int):
        self.element.click()
        browser.element('.react-datepicker__year-select').element(f'[value="{option}"]').click()

    def select_month(self, option: int):
        browser.element('.react-datepicker__month-select').element(f'[value="{option}"]').click()

    def select_day(self, option: int):
        browser.element(f'.react-datepicker__day--00{option}').click()

