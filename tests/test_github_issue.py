from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import allure

repository = "eroshenkoam/allure-example"
issue = "#76"


def test_github_selene():
    browser.open("https://github.com")

    (
        s(".header-search-input")
        .click()
        .send_keys(repository)
        .submit()
     )


    s(by.link_text(repository)).click()

    s("#issues-tab").click()

    s(by.partial_text(issue)).should(be.visible)


@allure.tag("GitHub")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "saveleva_a")
@allure.feature("Задачи в репозитории")
@allure.story("Пользователь может найти нужный Issue")
@allure.link("https://github.com", name="Testing")
def test_steps_dynamic():
    with allure.step("Open page github.com"):
        browser.open("https://github.com")

    with allure.step("Find repository '{repository}'"):
        (
            s(".header-search-input")
            .click()
            .send_keys(repository)
            .submit()
        )

    with allure.step("Go to repository"):
        s(by.link_text(repository)).click()
        s("#issues-tab").click()

    with allure.step("Check Issue {issue}"):
        s(by.partial_text(issue)).should(be.visible)


def test_steps_decorate():
    open_page("https://github.com")
    find_repository(repository)
    go_to_repository(repository)
    search_issue_number(issue)


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
