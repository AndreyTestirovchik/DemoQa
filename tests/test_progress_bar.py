import time
from pages.progress_bar import ProgressBar


def test_progress_bar_page(browser):
    progress_bar_page = ProgressBar(browser)

    progress_bar_page.visit()
    time.sleep(2)
    assert progress_bar_page.btn_start.exist()
    assert progress_bar_page.progress_bar.check_css('width', '0%')
    progress_bar_page.btn_start.click()
    while progress_bar_page.progress_bar.get_text() < '51%':
        time.sleep(1)
    progress_bar_page.btn_start.click()

