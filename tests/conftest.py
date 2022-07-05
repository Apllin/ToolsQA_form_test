from selene.support.shared import browser
import pytest


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