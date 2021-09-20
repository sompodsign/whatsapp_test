import unittest
from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestWhatsapp(BaseTest):

    def test_001_search_number(self):
        print("\n" + str(test_cases(0)))
        page = MainPage(self.driver)
        page.check_logged_in()



