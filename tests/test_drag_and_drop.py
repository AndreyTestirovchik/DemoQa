import time
from pages.droppable import Droppable
from selenium.webdriver import ActionChains


def test_drag_and_drop(browser):
    droppable_page = Droppable(browser)
    action_chains = ActionChains(browser)

    droppable_page.visit()
    # assert droppable_page.drop.check_css('backgroundColor', None)
    action_chains.drag_and_drop(
        droppable_page.drag.find_element(),
        droppable_page.drop.find_element()
    ).perform()
    assert droppable_page.drop.check_css('backgroundColor', 'steelblue')
    time.sleep(2)
    action_chains.drag_and_drop_by_offset(droppable_page.drag.find_element(), -300, -300).perform()
    assert droppable_page.drop.check_css('backgroundColor', 'steelblue')
    time.sleep(3)
