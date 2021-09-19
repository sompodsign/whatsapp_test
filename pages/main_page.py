from pages.base_page import BasePage
from pages.LoginModal import LoginModal
from pages.chat_page import ChatPage
from utils.locators import *


# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = Locators
        super().__init__(driver)  # Python3 version

    def close_popup_modal(self):
        try:
            return LoginModal(self.find_element(*self.locator.POPUP).click())
        except:
            print('popup was not there')

    def click_user_icon(self):
        self.close_popup_modal()
        self.find_element(*self.locator.USER_ICON).click()
        self.wait_element(*self.locator.USERNAME)
        return LoginModal(self.driver)
