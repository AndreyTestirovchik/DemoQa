from pages.forms_page import FormsPage
import time


def test_send_keys(browser):
    forms_page = FormsPage(browser)

    forms_page.visit()
    forms_page.first_name.send_keys('Ivan')
    forms_page.last_name.send_keys('Ivanov')
    forms_page.user_email.send_keys('ivan.ivanov.1997@gmail.com')
    forms_page.radio_btn_male.click()
    forms_page.phone_number.send_keys('89994554488')
    forms_page.check_box_music.click()
    forms_page.check_box_reading.click()
    forms_page.check_box_sports.click()
    # forms_page.subject.send_keys('goal')
    time.sleep(3)
