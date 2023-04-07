from pages.web_tables import WebTables


def test_sort_column(browser):
    web_tables_page = WebTables(browser)
    column_class_asc = 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    columns_all = ["web_tables_page.column_first_name.get_dom_attribute('class')",
                   "web_tables_page.column_last_name.get_dom_attribute('class')",
                   "web_tables_page.column_age.get_dom_attribute('class')",
                   "web_tables_page.column_email.get_dom_attribute('class')",
                   "web_tables_page.column_salary.get_dom_attribute('class')",
                   "web_tables_page.column_department.get_dom_attribute('class')",
                   "web_tables_page.column_action.get_dom_attribute('class')"]

    columns_for_first_name = list(columns_all)
    columns_for_last_name = list(columns_all)
    columns_for_age = list(columns_all)
    columns_for_email = list(columns_all)
    columns_for_salary = list(columns_all)
    columns_for_department = list(columns_all)
    columns_for_action = list(columns_all)

    web_tables_page.visit()
    assert not column_class_asc in columns_all
    web_tables_page.column_first_name.click()
    assert web_tables_page.column_first_name.get_dom_attribute('class') == column_class_asc
    del columns_for_first_name[0]
    assert not column_class_asc in columns_for_first_name
    web_tables_page.column_last_name.click()
    assert web_tables_page.column_last_name.get_dom_attribute('class') == column_class_asc
    del columns_for_last_name[1]
    assert not column_class_asc in columns_for_last_name
    web_tables_page.column_age.click()
    assert web_tables_page.column_age.get_dom_attribute('class') == column_class_asc
    del columns_for_age[2]
    assert not column_class_asc in columns_for_age
    web_tables_page.column_email.click()
    assert web_tables_page.column_email.get_dom_attribute('class') == column_class_asc
    del columns_for_email[3]
    assert not column_class_asc in columns_for_email
    web_tables_page.column_salary.click()
    assert web_tables_page.column_salary.get_dom_attribute('class') == column_class_asc
    del columns_for_salary[4]
    assert not column_class_asc in columns_for_salary
    web_tables_page.column_department.click()
    assert web_tables_page.column_department.get_dom_attribute('class') == column_class_asc
    del columns_for_department[5]
    assert not column_class_asc in columns_for_department
    web_tables_page.column_action.click()
    assert web_tables_page.column_action.get_dom_attribute('class') == column_class_asc
    del columns_for_action[6]
    assert not column_class_asc in columns_for_action

