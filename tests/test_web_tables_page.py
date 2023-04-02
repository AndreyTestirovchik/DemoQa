import time
import allure
from pages.web_tables import WebTables
from selenium.webdriver.common.keys import Keys


first_name_1 = 'Ivan'
first_name_2 = 'Vasya'
first_name_3 = 'Kolya'
last_name_1 = 'Ivanov'
last_name_2 = 'Pupkin'
last_name_3 = 'Sidorov'
user_email_1 = 'ivan.007@mail.com'
user_email_2 = 'vasya.008@mail.com'
user_email_3 = 'kolya.001@mail.com'
age_1 = '35'
age_2 = '28'
age_3 = '31'
salary_1 = '60000'
salary_2 = '40000'
salary_3 = '80000'
department_1 = 'QA'
department_2 = 'HR'
department_3 = 'Cleaning'


@allure.feature('Add, Edit and Delete strings in Web Tables')
@allure.severity(allure.severity_level.NORMAL)
def test_web_tables_add(browser):
    web_tables_page = WebTables(browser)

    web_tables_page.visit()
    assert web_tables_page.btn_add.exist()
    assert not web_tables_page.modal_window.exist()
    web_tables_page.btn_add.click()
    time.sleep(2)
    assert web_tables_page.modal_window.visible()
    assert web_tables_page.btn_submit.exist()
    web_tables_page.btn_submit.click()
    assert web_tables_page.modal_window.visible()
    web_tables_page.first_name.send_keys(first_name_1)
    web_tables_page.last_name.send_keys(last_name_1)
    web_tables_page.user_email.send_keys(user_email_1)
    web_tables_page.age.send_keys(age_1)
    web_tables_page.salary.send_keys(salary_1)
    web_tables_page.department.send_keys(department_1)
    web_tables_page.btn_submit.click()
    time.sleep(2)
    assert not web_tables_page.modal_window.exist()
    assert web_tables_page.active_strings_in_table.check_count_elements(4)
    assert first_name_1 in web_tables_page.table_body.get_text()
    assert last_name_1 in web_tables_page.table_body.get_text()
    assert user_email_1 in web_tables_page.table_body.get_text()
    assert age_1 in web_tables_page.table_body.get_text()
    assert salary_1 in web_tables_page.table_body.get_text()
    assert department_1 in web_tables_page.table_body.get_text()
    time.sleep(2)

    assert web_tables_page.btn_edit_new.exist()
    web_tables_page.btn_edit_new.click()
    time.sleep(2)
    assert web_tables_page.modal_window.visible()
    assert web_tables_page.first_name.get_dom_attribute('value') == first_name_1
    assert web_tables_page.last_name.get_dom_attribute('value') == last_name_1
    assert web_tables_page.user_email.get_dom_attribute('value') == user_email_1
    assert web_tables_page.age.get_dom_attribute('value') == age_1
    assert web_tables_page.salary.get_dom_attribute('value') == salary_1
    assert web_tables_page.department.get_dom_attribute('value') == department_1
    web_tables_page.first_name.clear()
    web_tables_page.first_name.send_keys(first_name_2)
    web_tables_page.first_name.send_keys(Keys.ENTER)
    time.sleep(2)
    assert not web_tables_page.modal_window.exist()
    assert web_tables_page.active_strings_in_table.check_count_elements(4)
    assert first_name_2 in web_tables_page.table_body.get_text()

    assert web_tables_page.btn_delete_new.exist()
    web_tables_page.btn_delete_new.click()
    time.sleep(2)
    assert web_tables_page.active_strings_in_table.check_count_elements(3)
    assert not first_name_2 in web_tables_page.table_body.get_text()
    assert not last_name_1 in web_tables_page.table_body.get_text()
    assert not user_email_1 in web_tables_page.table_body.get_text()
    assert not age_1 in web_tables_page.table_body.get_text()
    assert not salary_1 in web_tables_page.table_body.get_text()
    assert not department_1 in web_tables_page.table_body.get_text()
    time.sleep(2)


@allure.feature('NEXT and PREViOUS buttons')
@allure.severity(allure.severity_level.NORMAL)
def test_next_previous_btns(browser):
    web_tables_page = WebTables(browser)

    web_tables_page.visit()
    browser.refresh()
    time.sleep(2)
    web_tables_page.btn_select_rows.scroll_to_element()
    web_tables_page.select_5_rows.click()
    time.sleep(2)
    assert web_tables_page.strings_in_table.check_count_elements(5)

    web_tables_page.btn_next.click()
    assert web_tables_page.active_strings_in_table.check_count_elements(3)
    assert web_tables_page.btn_next.get_dom_attribute('disabled')
    web_tables_page.btn_previous.click()
    assert web_tables_page.active_strings_in_table.check_count_elements(3)
    assert web_tables_page.btn_previous.get_dom_attribute('disabled')
    assert web_tables_page.all_page_in_table.get_text() == '1'

    web_tables_page.btn_add.click()
    time.sleep(2)
    web_tables_page.first_name.send_keys(first_name_1)
    web_tables_page.last_name.send_keys(last_name_1)
    web_tables_page.user_email.send_keys(user_email_1)
    web_tables_page.age.send_keys(age_1)
    web_tables_page.salary.send_keys(salary_1)
    web_tables_page.department.send_keys(department_1)
    web_tables_page.btn_submit.click()
    time.sleep(2)
    web_tables_page.btn_add.click()
    time.sleep(2)
    web_tables_page.first_name.send_keys(first_name_2)
    web_tables_page.last_name.send_keys(last_name_2)
    web_tables_page.user_email.send_keys(user_email_2)
    web_tables_page.age.send_keys(age_2)
    web_tables_page.salary.send_keys(salary_2)
    web_tables_page.department.send_keys(department_2)
    web_tables_page.btn_submit.click()
    time.sleep(2)
    web_tables_page.btn_add.click()
    time.sleep(2)
    web_tables_page.first_name.send_keys(first_name_3)
    web_tables_page.last_name.send_keys(last_name_3)
    web_tables_page.user_email.send_keys(user_email_3)
    web_tables_page.age.send_keys(age_3)
    web_tables_page.salary.send_keys(salary_3)
    web_tables_page.department.send_keys(department_3)
    web_tables_page.btn_submit.click()
    time.sleep(2)
    assert web_tables_page.all_page_in_table.get_text() == '2'
    assert not web_tables_page.btn_next.get_dom_attribute('disabled')
    assert web_tables_page.btn_previous.get_dom_attribute('disabled')
    web_tables_page.btn_next.click()
    time.sleep(2)
    assert web_tables_page.visible_page_in_table.get_dom_attribute('value') == '2'
    assert web_tables_page.btn_next.get_dom_attribute('disabled')
    assert not web_tables_page.btn_previous.get_dom_attribute('disabled')
    assert web_tables_page.active_strings_in_table.check_count_elements(1)
    web_tables_page.btn_previous.click()
    time.sleep(2)
    assert web_tables_page.visible_page_in_table.get_dom_attribute('value') == '1'
    assert not web_tables_page.btn_next.get_dom_attribute('disabled')
    assert web_tables_page.btn_previous.get_dom_attribute('disabled')
    assert web_tables_page.active_strings_in_table.check_count_elements(5)
    time.sleep(2)


