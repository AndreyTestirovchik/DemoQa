from pages.forms_page import FormsPage
from selenium.webdriver.common.keys import Keys


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
    forms_page.btn_state.scroll_to_element()
    forms_page.btn_state.click()
    time.sleep(2)
    forms_page.input_state.send_keys(Keys.UP)
    forms_page.input_state.send_keys(Keys.ENTER)
    time.sleep(2)
    forms_page.btn_select_city.click()
    time.sleep(2)
    forms_page.input_select_city.send_keys(Keys.DOWN)
    forms_page.input_select_city.send_keys(Keys.ENTER)
    time.sleep(2)


