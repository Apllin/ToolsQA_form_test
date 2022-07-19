from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import allure


def test_github_selene():
    browser.open("https://github.com")

    s(".header-search-input").click()
    s(".header-search-input").send_keys("eroshenkoam/allure-example")
    s(".header-search-input").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.partial_text("#76")).should(be.visible)

@allure.tag("GitHub")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "saveleva_a")
@allure.feature("Задачи в репозитории")
@allure.story("Пользователь может найти нужный Issue")
@allure.link("https://github.com", name="Testing")
def test_steps_dynamic():
    with allure.step("Open page github.com"):
        browser.open("https://github.com")

    with allure.step("Find repository 'eroshenkoam/allure-example'"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()

    with allure.step("Go to repository"):
        s(by.link_text("eroshenkoam/allure-example")).click()
        s("#issues-tab").click()

    with allure.step("Check Issue #76"):
        s(by.partial_text("#76")).should(be.visible)

def test_steps_decorate():
    open_page("https://github.com")
    find_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    search_issue_number("#76")


@allure.step('Зайти на страницу {url}')
def open_page(url: str):
    browser.open(url)

@allure.step('Найти в поиске репозиторий {repository_name}')
def find_repository(repository_name: str):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repository_name)
    s(".header-search-input").submit()

@allure.step('Перейти в репозиторий {repository_name}')
def go_to_repository(repository_name: str):
    s(by.link_text(repository_name)).click()
    s("#issues-tab").click()


@allure.step('Проверить наличие Issue {number}')
def search_issue_number(number: str):
    s(by.partial_text(number)).should(be.visible)