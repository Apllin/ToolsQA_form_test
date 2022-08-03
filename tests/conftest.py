from selene.support.shared import browser
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from utils import attach

DEFAULT_BROWSER_VERSION = '100.0'


def pytest_addoption(parser):
    parser.addoption(
        "--browser_version"
    )


@pytest.fixture(scope='function', autouse=True)
def browser_open_url():
    browser.config.base_url = 'https://demoqa.com'


@pytest.fixture(scope='function', autouse=True)
def browser_quit():
    yield
    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def browser_window_size():
    browser.config.window_width = 1800
    browser.config._window_height = 1300


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    # browser = Browser(Config(driver))
    browser.config.driver = driver

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)