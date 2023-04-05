from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }
        self.icon = WebElement(driver, locator='#app > header > a')
        self.btns_menu_list = WebElement(driver, locator=':nth-child(3) > div > ul > li')
        self.btn_small_modal = WebElement(driver, locator='#showSmallModal')
        self.btn_large_modal = WebElement(driver, locator='#showLargeModal')
        self.modal_window = WebElement(driver, locator='.show > div > div')
        self.btn_close_small_modal = WebElement(driver, locator='#closeSmallModal')
        self.btn_close_large_modal = WebElement(driver, locator='#closeLargeModal')
