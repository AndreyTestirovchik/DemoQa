from components.components import WebElement
from pages.base_page import BasePage


class Slider(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/slider'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }
        self.icon = WebElement(driver, locator='#app > header > a')
        self.slider = WebElement(driver, locator='span > input')
        self.slider_value = WebElement(driver, locator='#sliderValue')
