from selenium.webdriver.common.by import By
# from browser import Browser
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

delay_min = 3 # sec
delay_medium = 5 # sec
delay_max = 9 # sec

class HeaderLocator(object):
    # Header Locators
    USER_ICON = (By.XPATH, "//i[@class='icon-white icon-user']")
    LOGOUT_LINK = (By.XPATH, "//a[contains(text(),'Log out')]")

class Header(PageBase):
    #  Header Page Methods
    def method_click_on_logout_link(self):
        self.click_element(*HeaderLocator.USER_ICON)
        self.click_element(*HeaderLocator.LOGOUT_LINK)
