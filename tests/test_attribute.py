from pages.text_box_page import TextBoxPage
import allure


@allure.feature('check attr')
@allure.story('Проверка соответствия плейсхолдера')
@allure.severity(allure.severity_level.BLOCKER)
def test_placeholder(browser):
    text_box_page = TextBoxPage(browser)

    text_box_page.visit()
    assert text_box_page.full_name.get_dom_attribute('placeholder') == 'Full Name'


@allure.feature('check attr')
@allure.story('Проверка упавшего теста')
@allure.severity(allure.severity_level.BLOCKER)
def test_fail():
    assert 111 == 222
