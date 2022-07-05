from selene import be
from selene.support.shared import browser

def test_add_edit_delete_fills():
    browser.open("/webtables")

    #add new line
    browser.element("#addNewRecordButton").click()
    browser.element("#firstName").type("John")
    browser.element("#lastName").type("Doe")
    browser.element("#userEmail").type("johndoe@gmail.com")
    browser.element("#age").type("2")
    browser.element("#salary").type("100")
    browser.element("#department").type("test")
    browser.element("#submit").click()

    #edit 2nd line
    browser.element("#edit-record-2").click()

    id = ["#firstName", "#lastName", "#age", "#salary", "#department"]
    for i in id:
        browser.element(i).type("1")
    browser.element("#userEmail").type("m")
    browser.element("#submit").click()

    #delete 3rd line
    browser.element("#delete-record-3").click()

    #assertions: add line, edit line, delete line

    #add line:
    elements = ['//*[text()="John"]', '//*[text()="Doe"]', '//*[text()="johndoe@gmail.com"]', '//*[text()="2"]',
                '//*[text()="100"]', '//*[text()="test"]']
    for element in elements:
        browser.element(element).should(be.visible)

    # edit line:
    xpath = ['//*[text()="Alden1"]', '//*[text()="Cantrell1"]', '//*[text()="alden@example.comm"]', '//*[text()="45"]',
                '//*[text()="120001"]', '//*[text()="Compliance1"]']
    for element in xpath:
        browser.element(element).should(be.visible)

    # delete line:
    browser.element('//*[text()="Kierra"]').should(be.not_.visible)