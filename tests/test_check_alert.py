import time

from pages.alert_page import AlertPage


def test_check_alert(browser):
    alert_page = AlertPage(browser)
    alert_page.visit()

    assert alert_page.btn_time_alert.exist()
    alert_page.btn_time_alert.click()
    assert not alert_page.alert()
    browser.refresh()
    alert_page.equal_url()
    alert_page.btn_time_alert.click()
    time.sleep(2)
    assert not alert_page.alert()
    browser.refresh()
    alert_page.equal_url()
    alert_page.btn_time_alert.click()
    time.sleep(4)
    assert not alert_page.alert()
    browser.refresh()
    alert_page.equal_url()
    alert_page.btn_time_alert.click()
    time.sleep(5)
    assert alert_page.alert()
