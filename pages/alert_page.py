from components.components import WebElement
from pages.base_page import BasePage


class AlertPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }
        self.icon = WebElement(driver, locator='#app > header > a')
        self.btn_alert = WebElement(driver, locator='#alertButton')
        self.btn_confirm = WebElement(driver, locator='#confirmButton')
        self.confirm_result = WebElement(driver, locator='#confirmResult')
        self.btn_promt = WebElement(driver, locator='#promtButton')
        self.promt_result = WebElement(driver, locator='#promptResult')