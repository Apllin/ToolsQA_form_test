import os.path

from selene.support.shared import browser


def get_abs_path(path):
    return str(
        os.path.abspath(f'../source/{path}')
    )


def remove_elements_on_page():
    # remove google_ads
    browser.execute_script("document.querySelectorAll('[id^=google_ads_iframe]')"
                           ".forEach(element => element.remove())")
    # remove footer
    browser.execute_script(
        "var el = document.querySelectorAll('#app > footer'); if (el.length > 0); { el[0].remove(); }")
