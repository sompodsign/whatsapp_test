import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
import HtmlTestRunner
from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestWhatsappWeb(BaseTest):

    def test_001_verify_searched_contact(self):
        print("\n" + str(test_cases(0)))
        print("Please Scan the QR code with your smart phones whatsapp scanner")
        page = MainPage(self.driver)
        page.login()
        self.assertTrue(page.result_for_searched_contact())

    def test_002_verify_send_message(self):
        print("\n" + str(test_cases(1)))
        print("Please Scan the QR code with your smart phones whatsapp scanner")
        chat_page = ChatPage(self.driver)
        self.assertTrue(chat_page.send_message_to_matched_contact())

    def test_003_successful_message_sent(self):
        print("\n" + str(test_cases(2)))
        print("Please Scan the QR code with your smart phones whatsapp scanner")
        chat_page = ChatPage(self.driver)
        chat_page.send_message_and_write_excel()

    def test_004_seen_status(self):
        print("\n" + str(test_cases(3)))
        print("Please Scan the QR code with your smart phones whatsapp scanner")
        chat_page = ChatPage(self.driver)
        chat_page.seen_status_to_excel()

    def test_005_logout(self):
        print("\n" + str(test_cases(4)))
        print("Please Scan the QR code with your smart phones whatsapp scanner")
        chat_page = ChatPage(self.driver)
        chat_page.logout()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'))
