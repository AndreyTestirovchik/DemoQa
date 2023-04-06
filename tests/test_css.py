from pages.text_box_page import TextBoxPage


def test_text_box_submit(browser):
    text_box_page = TextBoxPage(browser)

    text_box_page.visit()

    assert text_box_page.btn_submit.check_css('color', '#fff')
    assert text_box_page.btn_submit.check_css('backgroundColor', '#007bff')
    assert text_box_page.btn_submit.check_css('borderColor', '#007bff')
