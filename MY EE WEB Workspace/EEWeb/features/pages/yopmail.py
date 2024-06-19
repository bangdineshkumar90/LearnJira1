from selenium.webdriver.common.by import By
# from browser import Browser
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from pages.test_base import TestBase

test_base = TestBase()

delay_min = 3 # sec
delay_medium = 5 # sec
delay_max = 9 # sec

# Dynamic Web Elements
emailSubjectXpath = "//span[contains(text(),'xxxxxx')]"

class YopmailPageLocator(object):
    # Yopmail Page Locators
    ACCESS_WEB_LINK = (By.XPATH, "//p[contains(text(),'You can continue by clicking')]//a[contains(text(),'here')]")
    EMAIL_SEARCH_FIELD = (By.ID, "login")
    CHECK_INBOX_BUTTON = (By.XPATH, "//input[@type='submit' and @value='Check Inbox']")
    CHECK_NEW_EMAILS_BUTTON = (By.ID, "lrefr")
    # GET_STARTED_LINK = (By.XPATH, "//a[contains(text(),'Get started')]")
    # EMAIL_INFO_DETAILS = (By.XPATH, "//div[@class='main_intro_block']")
    # VERIFY_EMAIL_LINK = (By.XPATH, "//span[contains(text(),'verify your email')]/parent::a")
    
class YopmailPage(PageBase):
    # Yopmail Page Methods
    def method_search_email(self, email):
        self.enter_text(email, *YopmailPageLocator.EMAIL_SEARCH_FIELD)
        test_base.takesScreenshot()
        self.click_element(*YopmailPageLocator.CHECK_INBOX_BUTTON)

    def method_check_new_emails(self):
        self.click_element(*YopmailPageLocator.CHECK_NEW_EMAILS_BUTTON)
    
    def method_access_yopmail(self):
        self.click_element(*YopmailPageLocator.ACCESS_WEB_LINK)