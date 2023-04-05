import time
import allure
from pages.alert_page import AlertPage
#accept - подтверждение alerta
#dismiss - отмена (Cancel) alerta
#send_keys - ввод данных в alert


@allure.title('Проверка окна alert')
def test_alert(browser):
    alert_page = AlertPage(browser)

    alert_page.visit()
    assert not alert_page.alert()

    alert_page.btn_alert.click()
    time.sleep(2)
    assert alert_page.alert()
    alert_page.alert().accept()


@allure.title('Подтверждение alert')
def test_alert_text(browser):
    alert_page = AlertPage(browser)

    alert_page.visit()
    alert_page.btn_alert.click()
    time.sleep(2)
    assert alert_page.alert().text == 'You clicked a button'
    alert_page.alert().accept()
    assert not alert_page.alert()


@allure.title('Отмена alert')
def test_confirm(browser):
    alert_page = AlertPage(browser)

    alert_page.visit()
    alert_page.btn_confirm.click()
    time.sleep(2)
    alert_page.alert().dismiss()
    assert alert_page.confirm_result.get_text() == 'You selected Cancel'


@allure.title('Проверка ввода текста в alert')
def test_prompt(browser):
    alert_page = AlertPage(browser)
    name = 'Ivan'

    alert_page.visit()
    alert_page.btn_promt.click()
    time.sleep(2)
    alert_page.alert().send_keys(name)
    alert_page.alert().accept()
    assert alert_page.promt_result.get_text() == 'You entered ' + name
    time.sleep(2)

