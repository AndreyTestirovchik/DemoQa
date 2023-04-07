import time
from pages.slider import Slider
from selenium.webdriver import ActionChains


def test_slider(browser):
    slider_page = Slider(browser)
    action_chains = ActionChains(browser)
    slider_page.visit()

    assert slider_page.slider.exist()
    assert slider_page.slider_value.exist()
    assert slider_page.slider.get_dom_attribute('value') == '25'
    assert slider_page.slider_value.get_dom_attribute('value') == '25'
    action_chains.drag_and_drop_by_offset(slider_page.slider.find_element(), 2, 0).perform()
    time.sleep(2)
    assert slider_page.slider.get_dom_attribute('value') == '50'
    assert slider_page.slider_value.get_dom_attribute('value') == '50'
    time.sleep(2)
