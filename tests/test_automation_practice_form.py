import os
from selene import have
from selene.support.shared import browser

def test_fill_registrarion_form():
    browser.open("/automation-practice-form")

    #remove google_ads
    browser.execute_script("document.querySelectorAll('[id^=google_ads_iframe]')"
                           ".forEach(element => element.remove())")
    # remove footer
    browser.execute_script(
        "var el = document.querySelectorAll('#app > footer'); if (el.length > 0); { el[0].remove(); }")

    browser.element("#firstName").type("John")
    browser.element("#lastName").type("Doe")
    browser.element("#userEmail").type("johndoe@gmail.com")
    browser.element('[for="gender-radio-1"]').click()
    browser.element("#userNumber").type("1337228148")
    browser.element('#dateOfBirthInput').click()
    browser.element("[value='6']").click()
    browser.element("[value='1998']").click()
    browser.element('[aria-label="Choose Friday, July 3rd, 1998"]').click()
    browser.element('#subjectsInput').send_keys('English').press_enter()
    # browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text("Music")).click()
    browser.element("#uploadPicture").send_keys(os.path.abspath('../source/test.png'))
    browser.element('[placeholder="Current Address"]').type("bla-bla")
    browser.element("#state").click()
    browser.element("#react-select-3-input").type("NCR").press_enter()
    browser.element("#city").click()
    browser.element("#react-select-4-input").type("Noida").press_enter()
    browser.element("div button#submit").press_enter()

    #assertions
    browser.all("//tr/*[last()]").should(have.exact_texts('Values', 'John Doe',
                                                            'johndoe@gmail.com', 'Male', '1337228148', '03 July,1998',
                                                          'English', 'Music', 'test.png', 'bla-bla', 'NCR Noida'))

    browser.element("#closeLargeModal").click()

