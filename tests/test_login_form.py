from pages.forms_page import FormsPage
import time


def test_send_keys(browser):
    forms_page = FormsPage(browser)

    forms_page.visit()
    assert not forms_page.modal_dialog.exist()
    time.sleep(2)
    forms_page.first_name.send_keys('Ivan')
    forms_page.last_name.send_keys('Ivanov')
    forms_page.user_email.send_keys('ivan.ivanov@gmail.com')
    forms_page.gender_radio_1.click_force()
    forms_page.user_number.send_keys('89994554488')
    time.sleep(2)
    forms_page.btn_submit.click_force()
    time.sleep(2)

    assert forms_page.modal_dialog.exist()
    forms_page.btn_close_modal.click_force()

