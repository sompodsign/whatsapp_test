import unittest
from selenium.webdriver.common.keys import Keys
import openpyxl as excel
import time
from tests.base_test import BaseTest
from utils.locators import Locators
from pages.base_page import BasePage


class ChatPage(BasePage):
    def __init__(self, driver):
        self.locator = Locators
        super(ChatPage, self).__init__(driver)  # Python2 version

    def read_contact(self, filename):
        file = excel.load_workbook(filename)
        sheet = file.active
        firstCol = sheet['A']
        file.close()
        return firstCol[1].value

    def login(self):
        self.wait_element(*self.locator.QR_CODE)
        self.wait_element_custom_time(*self.locator.SEARCH_BOX, time=50)

    def search_contact(self, number):
        time.sleep(1)
        search_field = self.find_element(*self.locator.SEARCH_BOX)
        search_field.send_keys(number)
        self.wait_element(*self.locator.MATCHED_CONTACT)
        return self.find_element(*self.locator.MATCHED_CONTACT)

    def send_message(self):
        contact_number = self.read_contact('contacts.xlsx')
        message = "Test Message"
        self.search_contact(contact_number).click()
        self.wait_element(*self.locator.MESSAGE_INPUT_FIELD)
        message_input_field = self.find_element(*self.locator.MESSAGE_INPUT_FIELD)
        message_input_field.send_keys(message)
        message_input_field.send_keys(Keys.ENTER)

    def last_message(self):
        self.wait_element(*self.locator.LAST_MESSAGE)
        message_elem = self.find_element(*self.locator.LAST_MESSAGE)
        time.sleep(2)
        if message_elem:
            return True
        return False

    def check_message_status(self):
        self.wait_element(*self.locator.LAST_MESSAGE)
        message_elem = self.find_element(*self.locator.LAST_MESSAGE)

    def send_message_to_matched_contact(self):
        self.send_message()
        time.sleep(2)
        return self.last_message()

    def write_excel(self, status='Sent', filename=''):
        wb = excel.Workbook()
        ws = wb.active
        ws['A1'], ws['B1'] = 'Contact', 'Status'
        ws['A2'], ws['B2'] = self.read_contact('contacts.xlsx'), status
        wb.save(filename)
        wb.close()

    def send_message_and_write_excel(self):
        self.send_message()
        time.sleep(5)
        print(self.get_url())
        if self.last_message():
            self.write_excel(filename='message_successful.xlsx')
