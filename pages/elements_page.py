from pages.base_page import BasePage
from components.components import WebElement


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }
        self.text_elements_please = WebElement(driver, locator='div.col-md-6')
        self.text_elements = WebElement(driver, locator='div.playgound-header > div')
        self.icon = WebElement(driver, locator='div.playgound-header > div')
        self.btn_sidebar_first = WebElement(driver, locator='div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, locator='div:nth-child(1) > div > ul > #item-0 > span')
        self.btn_sidebar_first_checkbox = WebElement(driver, locator='div:nth-child(1) > div > ul > #item-1 > span')
        self.btns_first_menu = WebElement(driver, locator='div:nth-child(1) > div > ul > li')
