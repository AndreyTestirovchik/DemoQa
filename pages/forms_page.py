from components.components import WebElement
from pages.base_page import BasePage


class FormsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }
        self.first_name = WebElement(driver, locator='#firstName')
        self.last_name = WebElement(driver, locator='#lastName')
        self.user_email = WebElement(driver, locator='#userEmail')
        self.radio_btn_male = WebElement(driver, locator='#genterWrapper > div:nth-child(2) >  div:nth-child(1)')
        self.radio_btn_female = WebElement(driver, locator='#genterWrapper > div:nth-child(2) > div:nth-child(2)')
        self.radio_btn_other = WebElement(driver, locator='#genterWrapper > div:nth-child(2) >  div:nth-child(3)')
        self.phone_number = WebElement(driver, locator='#userNumber')
        self.date_of_birth = WebElement(driver, locator='#dateOfBirthInput')
        self.subject = WebElement(driver, locator='subjectsContainer > div')
        self.check_box_sports = WebElement(driver, locator='#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)')
        self.check_box_reading = WebElement(driver, locator='#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)')
        self.check_box_music = WebElement(driver, locator='#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)')
