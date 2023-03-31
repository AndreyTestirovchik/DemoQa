from pages.forms_page import FormsPage


def test_login_form(browser):
    forms_page = FormsPage(browser)

    forms_page.visit()
    assert forms_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert forms_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert forms_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert not forms_page.user_email.get_dom_attribute('pattern') == ''
    forms_page.btn_submit.click_force()
    assert forms_page.user_form.get_dom_attribute('class') == 'was-validated'
