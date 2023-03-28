from pages.modal_dialogs_page import ModalDialogs
from pages.demoqa import DemoQa


def test_modal_elements(browser):
    modal_dialogs_page = ModalDialogs(browser)

    modal_dialogs_page.visit()
    assert modal_dialogs_page.btns_menu_list.check_count_elements(count=5)


def test_navigation_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)
    demo_qa_page = DemoQa(browser)

    modal_dialogs_page.visit()
    modal_dialogs_page.refresh()
    modal_dialogs_page.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demo_qa_page.equal_url()
    assert browser.title == demo_qa_page.pageData['title']
    browser.set_window_size(1000, 1000)



