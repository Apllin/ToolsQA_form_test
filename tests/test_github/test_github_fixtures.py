from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import pytest

chrome = pytest.fixture(params=[(1800, 1300), (1300, 1020), (900, 600)])


@chrome
def browser_size(request):
    return request


@pytest.fixture(scope='function', autouse=True)
def set_browser_size(browser_size):
    width = browser_size.param[0]
    height = browser_size.param[1]
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.mark.parametrize("browser_size", [(1800, 1300)], indirect=True)
def test_github_desktop(browser_size):
    browser.open("https://github.com")
    (
        s('a[href="/login"')
        .click()
     )
    s(".auth-form-header").should(have.exact_text("Sign in to GitHub"))

@pytest.mark.parametrize("browser_size", [(600, 500)], indirect=True)
def test_github_mobile(browser_size):
    browser.open("https://github.com")
    s('.octicon-three-bars').click()
    s('a[href="/login"').click()
    s(".auth-form-header").should(have.exact_text("Sign in to GitHub"))
