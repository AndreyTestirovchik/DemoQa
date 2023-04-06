import time
import pytest
from pages.accordion import Accordion
from pages.alert_page import AlertPage
from pages.demoqa import DemoQa
from pages.browser_tab import BrowserTab


@pytest.mark.parametrize('pages', [Accordion, AlertPage, BrowserTab, DemoQa])
def test_seo_meta(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.meta.exist()
    assert page.meta.get_dom_attribute('name') == 'viewport'
    assert page.meta.get_dom_attribute('content') == 'width=device-width,initial-scale=1'

