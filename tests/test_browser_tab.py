from pages.browser_tab import BrowserTab
import time

#driver.window_handles - получение списка открытых вкладок
#driver.switch_to.window() - переход между открытыми вкладками


def test_browser_tab(browser):
    browser_tab_page = BrowserTab(browser)

    browser_tab_page.visit()
    assert len(browser.window_handles) == 1
    browser_tab_page.new_tab.click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://demoqa.com/sample'
    assert len(browser.window_handles) == 2

    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)
    assert browser_tab_page.equal_url()



