from pages.links_page import Links


def test_window_tab(browser):
    links_page = Links(browser)
    links_page.visit()

    assert links_page.link_home.exist()
    assert links_page.link_home.get_text() == 'Home'
    assert links_page.link_home.get_dom_attribute('href') == 'https://demoqa.com'
    assert len(browser.window_handles) == 1
    links_page.link_home.click()
    assert len(browser.window_handles) == 2
