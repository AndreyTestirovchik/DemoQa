from pages.web_tables import WebTables

column_class_asc = 'rt-th rt-resizable-header -sort-asc -cursor-pointer'


def test_sort_column(browser):
    web_tables_page = WebTables(browser)
    web_tables_page.visit()

    assert not column_class_asc in [web_tables_page.column_first_name.get_dom_attribute('class'),
                                    web_tables_page.column_last_name.get_dom_attribute('class'),
                                    web_tables_page.column_age.get_dom_attribute('class'),
                                    web_tables_page.column_email.get_dom_attribute('class'),
                                    web_tables_page.column_salary.get_dom_attribute('class'),
                                    web_tables_page.column_department.get_dom_attribute('class'),
                                    web_tables_page.column_action.get_dom_attribute('class')]
    web_tables_page.column_first_name.click()
    assert web_tables_page.column_first_name.get_dom_attribute('class') == column_class_asc
    assert not column_class_asc in [web_tables_page.column_last_name.get_dom_attribute('class'),
                                    web_tables_page.column_age.get_dom_attribute('class'),
                                    web_tables_page.column_email.get_dom_attribute('class'),
                                    web_tables_page.column_salary.get_dom_attribute('class'),
                                    web_tables_page.column_department.get_dom_attribute('class'),
                                    web_tables_page.column_action.get_dom_attribute('class')]
    web_tables_page.column_last_name.click()
    assert web_tables_page.column_last_name.get_dom_attribute('class') == column_class_asc
    assert not column_class_asc in [web_tables_page.column_first_name.get_dom_attribute('class'),
                                    web_tables_page.column_age.get_dom_attribute('class'),
                                    web_tables_page.column_email.get_dom_attribute('class'),
                                    web_tables_page.column_salary.get_dom_attribute('class'),
                                    web_tables_page.column_department.get_dom_attribute('class'),
                                    web_tables_page.column_action.get_dom_attribute('class')]
    web_tables_page.column_age.click()
    assert web_tables_page.column_age.get_dom_attribute('class') == column_class_asc
    assert not column_class_asc in [web_tables_page.column_first_name.get_dom_attribute('class'),
                                    web_tables_page.column_last_name.get_dom_attribute('class'),
                                    web_tables_page.column_email.get_dom_attribute('class'),
                                    web_tables_page.column_salary.get_dom_attribute('class'),
                                    web_tables_page.column_department.get_dom_attribute('class'),
                                    web_tables_page.column_action.get_dom_attribute('class')]
    web_tables_page.column_email.click()
    assert web_tables_page.column_email.get_dom_attribute('class') == column_class_asc
    assert not column_class_asc in [web_tables_page.column_first_name.get_dom_attribute('class'),
                                    web_tables_page.column_last_name.get_dom_attribute('class'),
                                    web_tables_page.column_age.get_dom_attribute('class'),
                                    web_tables_page.column_salary.get_dom_attribute('class'),
                                    web_tables_page.column_department.get_dom_attribute('class'),
                                    web_tables_page.column_action.get_dom_attribute('class')]
    web_tables_page.column_salary.click()
    assert web_tables_page.column_salary.get_dom_attribute('class') == column_class_asc
    assert not column_class_asc in [web_tables_page.column_first_name.get_dom_attribute('class'),
                                    web_tables_page.column_last_name.get_dom_attribute('class'),
                                    web_tables_page.column_age.get_dom_attribute('class'),
                                    web_tables_page.column_email.get_dom_attribute('class'),
                                    web_tables_page.column_department.get_dom_attribute('class'),
                                    web_tables_page.column_action.get_dom_attribute('class')]
    web_tables_page.column_department.click()
    assert web_tables_page.column_department.get_dom_attribute('class') == column_class_asc
    assert not column_class_asc in [web_tables_page.column_first_name.get_dom_attribute('class'),
                                    web_tables_page.column_last_name.get_dom_attribute('class'),
                                    web_tables_page.column_age.get_dom_attribute('class'),
                                    web_tables_page.column_email.get_dom_attribute('class'),
                                    web_tables_page.column_salary.get_dom_attribute('class'),
                                    web_tables_page.column_action.get_dom_attribute('class')]
    web_tables_page.column_action.click()
    assert web_tables_page.column_action.get_dom_attribute('class') == column_class_asc
    assert not column_class_asc in [web_tables_page.column_first_name.get_dom_attribute('class'),
                                    web_tables_page.column_last_name.get_dom_attribute('class'),
                                    web_tables_page.column_age.get_dom_attribute('class'),
                                    web_tables_page.column_email.get_dom_attribute('class'),
                                    web_tables_page.column_salary.get_dom_attribute('class'),
                                    web_tables_page.column_department.get_dom_attribute('class')]

