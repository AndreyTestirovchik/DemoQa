from components.components import WebElement
from pages.base_page import BasePage


class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }
        self.icon = WebElement(driver, locator='#app > header > a')
        self.btn_add = WebElement(driver, locator='#addNewRecordButton')
        self.modal_window = WebElement(driver, locator='.show > div > div')
        self.btn_submit = WebElement(driver, locator='#submit')
        self.first_name = WebElement(driver, locator='#firstName')
        self.last_name = WebElement(driver, locator='#lastName')
        self.user_email = WebElement(driver, locator='#userEmail')
        self.age = WebElement(driver, locator='#age')
        self.salary = WebElement(driver, locator='#salary')
        self.department = WebElement(driver, locator='#department')
        self.table_body = WebElement(driver, locator='.rt-tbody')
        self.btn_edit_new = WebElement(driver, locator='#edit-record-4')
        self.btn_delete_new = WebElement(driver, locator='#delete-record-4')

        self.btn_delete_row = WebElement(driver, locator='[title="Delete"]')

        self.btn_select_rows = WebElement(driver, locator='.-pageSizeOptions > select')
        self.size_option_table = WebElement(driver, locator='.-pageSizeOptions')
        self.select_5_rows = WebElement(driver, locator='select > option:nth-child(1)')
        self.strings_in_table = WebElement(driver, locator='rt-tr-group', locator_type='class')
        self.active_strings_in_table = WebElement(driver, locator='action-buttons', locator_type='class')
        self.btn_previous = WebElement(driver, locator='.-previous > button')
        self.btn_next = WebElement(driver, locator='.-next > button')
        self.all_page_in_table = WebElement(driver, locator='.-pageInfo > span')
        self.visible_page_in_table = WebElement(driver, locator='input[type=number]')
        self.no_rows_found = WebElement(driver, locator='div.rt-noData')
