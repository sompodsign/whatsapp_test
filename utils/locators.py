from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class Locators(object):
    QR_CODE = (By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/canvas[1]")
    SEARCH_BOX = (By.XPATH, "//div[@role='textbox']")
    SEARCH_RESULT = (By.XPATH, "//div[contains(text(),'Contacts')]")
    MATCHED_CONTACT = (By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]")
    MESSAGE_INPUT_FIELD = (By.CSS_SELECTOR, "div[role='textbox'][contenteditable='true'][data-tab='9']")
    LAST_MESSAGE = (By.CSS_SELECTOR, "div[class='_2wUmf message-out focusable-list-item'] div[class='_1Gy50']")
    STATUS = (By.CSS_SELECTOR, "div[class='_2wUmf message-out focusable-list-item'] div[class='_2F01v']")
    VERTICAL_DOT_MENU = (By.XPATH, "//header/div[2]/div[1]/span[1]/div[3]/div[1]/span[1]")
    LOGOUT = (By.XPATH, "//div[contains(text(),'Log out')]")
