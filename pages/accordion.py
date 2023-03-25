from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)
        self.section_1_heading = WebElement(driver, locator='#section1Heading')
        self.section_1_content = WebElement(driver, locator='#section1Content > p')
        self.section_2_content_1 = WebElement(driver, locator='#section2Content > p:nth-child(1)')
        self.section_2_content_2 = WebElement(driver, locator='#section2Content > p:nth-child(2)')
        self.section_3_content = WebElement(driver, locator='#section3Content > p')
