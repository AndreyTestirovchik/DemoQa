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
        self.gender_radio_1 = WebElement(driver, locator='#gender-radio-1')
        self.gender_radio_2 = WebElement(driver, locator='#gender-radio-2')
        self.gender_radio_3 = WebElement(driver, locator='#gender-radio-3')
        self.user_number = WebElement(driver, locator='#userNumber')
        self.btn_submit = WebElement(driver, locator='#submit')
        self.modal_dialog = WebElement(driver, locator='body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, locator='#closeLargeModal')
        self.date_of_birth = WebElement(driver, locator='#dateOfBirthInput')
        # self.subject = WebElement(driver, locator='subjectsContainer > div')
        self.check_box_sports = WebElement(driver, locator='#hobbiesWrapper > .col-sm-12 > div:nth-child(1)')
        self.check_box_reading = WebElement(driver, locator='#hobbiesWrapper > .col-sm-12 > div:nth-child(2)')
        self.check_box_music = WebElement(driver, locator='#hobbiesWrapper > .col-sm-12 > div:nth-child(3)')
