import time
import allure
import pytest
from pages.modal_dialogs_page import ModalDialogs


@allure.title('Modal Windows on Modal Dialogs Page')
def test_check_modal(browser):
    modal_page = ModalDialogs(browser)
    modal_page.visit()

    pytest.mark.skipif(browser.title != modal_page.pageData['title'])
    assert modal_page.btn_small_modal.exist()
    assert modal_page.btn_large_modal.exist()
    modal_page.btn_small_modal.click()
    time.sleep(2)
    assert modal_page.modal_window.visible()
    assert modal_page.btn_close_small_modal.exist()
    assert modal_page.btn_close_small_modal.get_text() == 'Close'
    modal_page.btn_close_small_modal.click()
    time.sleep(2)
    assert not modal_page.modal_window.exist()
    modal_page.btn_large_modal.click()
    time.sleep(2)
    assert modal_page.modal_window.visible()
    assert modal_page.btn_close_large_modal.exist()
    assert modal_page.btn_close_large_modal.get_text() == 'Close'
    modal_page.btn_close_large_modal.click()
    time.sleep(2)
    assert not modal_page.modal_window.exist()
    time.sleep(2)

