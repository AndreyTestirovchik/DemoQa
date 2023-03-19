from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_text_footer(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.text_footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_text_elements_center(browser):
    demo_qa_page = DemoQa(browser)
    elements = ElementsPage(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.btn_elements.click()
    assert elements.equal_url()
    assert elements.text_elements_center.get_text() == 'Please select an item from left to start practice.'


