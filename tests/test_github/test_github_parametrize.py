from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import pytest


@pytest.fixture(scope='function', params=[(1800, 1300), (1300, 1020)])
def set_browser_size_desktop(request):
    width = request.param[0]
    height = request.param[1]
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(scope='function', params=[(900, 600), (850, 700)])
def set_browser_size_mobile(request):
    width = request.param[0]
    height = request.param[1]
    browser.config.window_width = width
    browser.config.window_height = height


def test_github_desktop(set_browser_size_desktop):
    browser.open("https://github.com")
    (
        s('a[href="/login"')
        .click()
     )
    s(".auth-form-header").should(have.exact_text("Sign in to GitHub"))


def test_github_mobile(set_browser_size_mobile):
    browser.open("https://github.com")
    s('.octicon-three-bars').click()
    s('a[href="/login"').click()
    s(".auth-form-header").should(have.exact_text("Sign in to GitHub"))