from selenium.webdriver.common.by import By
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


delay_min = 3 # sec
delay_medium = 5 # sec
delay_max = 9 # sec

class MyEEWebLoginPageLocator(object):
    # Login Page Locators
    ACCEPT_COOKIES_BUTTON = (By.XPATH,"//button[@class='btn js-modal-close cookie-banner__btn-accept'][1]")
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='capture_signIn_traditionalSignIn_signInButton']")
    DONE_BUTTON = (By.XPATH, "//a[@class='button-primary filled-button']")

class MyEEWebLoginPage(PageBase):
    # Login Page Methods
    def check_cookies_page_exist(self):
        self.check_element_exist_cookies()

    def method_accept_cookies(self):
        self.click_element(*MyEEWebLoginPageLocator.ACCEPT_COOKIES_BUTTON)

    def method_enter_credentials(self, Mail, Password):
        username = Mail+"@yopmail.com"
        #self.wait_for_element_present(*MyEEWebLoginPageLocator.USERNAME_FIELD)
        self.enter_tet_with_sendkeys(username,Password)
        # self.enter_text(username, *MyEEWebLoginPageLocator.USERNAME_FIELD)
        # self.enter_text(Password, *MyEEWebLoginPageLocator.PASSWORD_FIELD)

    def method_click_on_login_button(self):
        self.click_element(*MyEEWebLoginPageLocator.LOGIN_BUTTON)

