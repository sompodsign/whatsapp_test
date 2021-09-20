import unittest
from tests.base_test import BaseTest
from utils.locators import Locators


class ChatPage(BaseTest):
    def __init__(self, driver):
        self.locator = Locators
        super(ChatPage, self).__init__(driver)

    def enter_target_number(self):
        pass
