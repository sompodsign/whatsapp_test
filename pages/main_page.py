from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.locators import Locators


# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = Locators
        super().__init__(driver)  # Python3 version

    def click_login_btn(self):
        pass

