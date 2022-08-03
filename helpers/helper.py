import os
import os.path
from pathlib import Path
from selene.support.shared import browser
import helpers


def recourse(path):
    file_path = str(Path(helpers.__file__)
                    .parent
                    .parent
                    .joinpath(f'source/{path}'))
    return os.path.abspath(file_path)


def remove_elements_on_page():
    # remove google_ads
    browser.execute_script("document.querySelectorAll('[id^=google_ads_iframe]')"
                           ".forEach(element => element.remove())")
    # remove footer
    browser.execute_script(
        "var el = document.querySelectorAll('#app > footer'); if (el.length > 0); { el[0].remove(); }")
