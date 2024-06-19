from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


delay_min = 3 # sec
delay_medium = 5 # sec
delay_max = 9 # sec

class JanrainLoginPageLocator(object):
    # Login Page Locators
    USERNAME_FIELD = (By.NAME, "signInEmailAddress")
    PASSWORD_FIELD = (By.NAME, "currentPassword")
    LOGIN_BUTTON = (By.XPATH, "//div[@class='capture_signin']//button[@class='md-raised md-primary md-block md-button md-ink-ripple'][contains(text(),'Sign In')]")
    REGION_SELECT = (By.NAME,"regionSelected")

class JanrainLoginPage(PageBase):
    # Login Page Methods
    
    def method_enter_credentials(self, username, password):
        self.enter_text(username, *JanrainLoginPageLocator.USERNAME_FIELD)
        self.enter_text(password, *JanrainLoginPageLocator.PASSWORD_FIELD)

    def method_click_on_login_button(self):
        self.click_element(*JanrainLoginPageLocator.LOGIN_BUTTON)

    def method_select_region(self):
        self.click_element(*JanrainLoginPageLocator.REGION_SELECT)
        self.enter_text("eu",*JanrainLoginPageLocator.REGION_SELECT)
        
