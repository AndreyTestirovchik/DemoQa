import time

from pages.text_box_page import TextBoxPage


def test_text_box(browser):
    text_box_page = TextBoxPage(browser)
    name = 'Ivan'
    current_address = 'Ivanovskaya 5'

    text_box_page.visit()
    text_box_page.full_name.send_keys(name)
    text_box_page.current_address.send_keys(current_address)
    text_box_page.btn_submit.click_force()
    time.sleep(2)
    assert name in text_box_page.output.get_text()
    assert current_address in text_box_page.output.get_text()
