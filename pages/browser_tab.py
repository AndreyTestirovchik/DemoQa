from components.components import WebElement
from pages.base_page import BasePage


class BrowserTab(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/browser-windows'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }
        self.icon = WebElement(driver, locator='#app > header > a')
        self.new_tab = WebElement(driver, locator='#tabButton')
