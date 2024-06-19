from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from pages.test_base import TestBase

test_base = TestBase()

delay_min = 3 # sec
delay_medium = 5 # sec
delay_max = 20 # sec

class PageBase(Browser):

    def prepareDynamicXpath(self, xpathValue, substitutionValue):
        return xpathValue.replace("xxxxxx", substitutionValue)

    def enter_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()
    
    def check_element_exist_cookies(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
        actions.perform()
    
    def colse_msg(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def enter_tet_with_sendkeys(self,username,Password):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB * 17)
        actions.send_keys(username)
        actions.send_keys(Keys.TAB * 2)
        actions.send_keys(Password)
        actions.send_keys(Keys.TAB * 4)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def navigate_url(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title
    
    def check_element_exist(self,*locator):
        return self.driver.find_element(*locator)
    
    def get_text(self, *locator):
        return self.driver.find_element(*locator).text
    
    def get_text_by_value(self,*locator):
        return self.driver.find_element(*locator).get_attribute('value')

    def wait_for_page_title(self, pagetitle):
        WebDriverWait(self.driver,delay_max).until(expected_conditions.title_contains(pagetitle))

    def wait_for_element_present(self, *locator):
        WebDriverWait(self.driver,delay_max).until(expected_conditions.visibility_of_element_located(*locator))

    def wait_for_text_present(self, *locator, eletxt):
        WebDriverWait(self.driver,delay_max).until(expected_conditions.text_to_be_present_in_element(*locator, eletxt))
    
    def get_inner_html(self, *locator):
        return self.driver.find_element(*locator).get_attribute('innerHTML')
    
    def get_outer_html(self, *locator):
        return self.driver.find_element(*locator).get_attribute('outerHTML')
    