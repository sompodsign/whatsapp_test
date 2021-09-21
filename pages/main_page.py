
import os
import openpyxl as excel
from pages.base_page import BasePage
from pages.chat_page import ChatPage
from utils.locators import Locators
import time


# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = Locators
        super().__init__(driver)  # Python3 version

    def read_contact(self, filename):
        # file = os.path.abspath(filename)
        # print(file)
        file = excel.load_workbook(filename)
        sheet = file.active
        firstCol = sheet['A']
        file.close()
        return firstCol[1].value

    def login(self):
        self.wait_element(*self.locator.QR_CODE)
        self.wait_element_custom_time(*self.locator.SEARCH_BOX, time=50)

    def result_for_searched_contact(self):
        contact_number = self.read_contact('contacts.xlsx')
        search_field = self.find_element(*self.locator.SEARCH_BOX)
        search_field.send_keys(contact_number)
        self.wait_element(*self.locator.MATCHED_CONTACT)
        time.sleep(3)
        search_result = self.find_element(*self.locator.MATCHED_CONTACT)
        if search_result:
            print(f"Searched Contact: {contact_number}")
            return True
        return False
