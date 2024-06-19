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
customerDetailsHeaderXpath = "//span[contains(@title,'xxxxxx')]/preceding-sibling::h4"

class HomePageLocator(object):
    # Home Page Locators

    CUSTOMER_SEARCH_FIELD = (By.XPATH, "//input[@type='text' and @name='Search Input Field']")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@title,'Search Button')]")
    CUSTOMER_VIEW_HEADER = (By.XPATH, "//h1[contains(text(),'Customer View')]")

    # Customer Details Section
    CUSTOMER_NAME = (By.XPATH, "//th[contains(text(),'Name')]/following-sibling::td")
    CUSTOMER_TYPE = (By.XPATH, "//th[contains(text(),'Type')]/following-sibling::td")
    CUSTOMER_ACC_NUM = (By.XPATH, "//th[contains(text(),'Account Number')]/following-sibling::td")

    # Customer View Section
    ACCOUNT_HOLDER = (By.XPATH, "//dt[contains(text(),'Account Holder')]/following-sibling::dd[1]")
    ACCOUNT_NUMBER = (By.XPATH, "//dt[contains(text(),'Account Number')]/following-sibling::dd[1]")
    MOBILE_NUMBER = (By.XPATH, "//dt[contains(text(),'Mobile Number')]/following-sibling::dd[1]")

class HomePage(PageBase):
    # Home Page Methods
    def method_customer_search(self, ctn):
        self.enter_text(ctn, *HomePageLocator.CUSTOMER_SEARCH_FIELD)
        time.sleep(2)
        test_base.takesScreenshot()
        self.click_element(*HomePageLocator.SEARCH_BUTTON)
        # self.wait_for_text_present(*HomePageLocator.CUSTOMER_VIEW_HEADER, "Customer View")

    def method_get_customer_details_header(self, ctn):
        CUSTOMER_DETAILS_HEADER = self.prepareDynamicXpath(customerDetailsHeaderXpath, ctn)
        return (self.driver.find_element(By.XPATH, CUSTOMER_DETAILS_HEADER).text).replace("Customer: ", "").strip()

    def method_get_customer_name(self):
        return self.get_text(*HomePageLocator.CUSTOMER_NAME)

    def method_get_customer_type(self):
        return self.get_text(*HomePageLocator.CUSTOMER_TYPE)

    def method_get_customer_account_number(self):
        return self.get_text(*HomePageLocator.CUSTOMER_ACC_NUM)

    def method_get_account_holder(self):
        return self.get_text(*HomePageLocator.ACCOUNT_HOLDER)

    def method_get_account_number(self):
        return self.get_text(*HomePageLocator.ACCOUNT_NUMBER)

    def method_get_mobile_number(self):
        return self.get_text(*HomePageLocator.MOBILE_NUMBER)
