from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from chat_page import ChatPage
from utils.locators import Locators


# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = Locators
        super().__init__(driver)  # Python3 version

    def check_qr_loaded(self):
        qr = self.wait_element(*self.locator.QR_CODE)
        if qr:
            return True
        return False

    def check_logged_in(self):
        if self.check_qr_loaded():
            search_field = self.wait_element(*self.locator.SEARCH_BOX)
            if search_field:
                return ChatPage(self.driver)



