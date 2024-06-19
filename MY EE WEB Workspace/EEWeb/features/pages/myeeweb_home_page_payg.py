from selenium.webdriver.common.by import By
import time
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


delay_min = 3 # sec
delay_medium = 5 # sec
delay_max = 20 # sec

#dynamic web elements
TopUpAmount = "//li[@class='ee-form-control pull-left']/label[@for='radioTopup_xxxxxx']"

class MyEEWebHomePagePaygLocator(object):
    # Home Page for PAYG Locators
    MENU_BUTTON = (By.XPATH, "//section[@id='menuIconContainer']/a")
    TOPUP_BUTTON = (By.XPATH, "//a[contains(@href,'/topup-my-device') and @class='navItem ']")
    VERIFY_REGISTERED_CARD_FIELD = (By.XPATH, "//span[@class='card-img cc-img-VISA-new-style']/input[@name='registerCards']")
    CVV_INPUT_FIELD = (By.XPATH, "//input[@name='ccvField-1']")
    MAKE_PAYMENT_BUTTON = (By.XPATH, "//div[@class='pull-right buttons-1']/input[@id='submitButton']")
    CONFIRM_PAYMENT_BUTTON = (By.XPATH, "//div[@class='pull-right']/input[@id='submitButton']")
    TOP_UP_CONFIRMATION_FIELD = (By.XPATH, "//div[@class='mod-notification-pane__title']/div/p")
    DONE_BUTTON = (By.XPATH, "//button[@class='cta-group__button button button-primary' and contains(text(),'DONE')]")
    ALLOWNACES_WINDOW_FIELD = (By.XPATH, "//section[@class='allowances-module white' and @id='allowance-module']")
    PAYG_BAN_FIELD = (By.XPATH, "//h3[@class='account-number']")


class MyEEWebHomePagePayg(PageBase):
    # PayG Home Page Methods
    def close_intro_page(self):
        self.colse_msg()

    def method_menu_click(self):
        self.click_element(*MyEEWebHomePagePaygLocator.MENU_BUTTON)

    def method_click_on_menu_button(self):
        self.click_element(*MyEEWebHomePagePaygLocator.MENU_BUTTON)
        self.click_element(*MyEEWebHomePagePaygLocator.TOPUP_BUTTON)

    def method_get_account_info(self):
        return self.get_text(*MyEEWebHomePagePaygLocator.PAYG_BAN_FIELD)

    def method_to_verify_registered_card(self):
        return self.check_element_exist(*MyEEWebHomePagePaygLocator.VERIFY_REGISTERED_CARD_FIELD)

    def method_topup_ammount(self,TopUpAmmount):
        TOPUPAMOUNT = self.prepareDynamicXpath(TopUpAmount, TopUpAmmount)
        self.click_element(By.XPATH, TOPUPAMOUNT)

    def method_to_enter_registered_card_details(self):
        self.click_element(*MyEEWebHomePagePaygLocator.CVV_INPUT_FIELD)
        self.click_element(*MyEEWebHomePagePaygLocator.MAKE_PAYMENT_BUTTON)

    def method_confirm_payment(self):
        self.click_element(*MyEEWebHomePagePaygLocator.CONFIRM_PAYMENT_BUTTON)
    
    def method_complete_payment(self):
        SUCCESS_MESSAGE = self.get_text(*MyEEWebHomePagePaygLocator.TOP_UP_CONFIRMATION_FIELD)
        self.click_element(*MyEEWebHomePagePaygLocator.DONE_BUTTON)
        return SUCCESS_MESSAGE

    def method_verify_data_usage(self):
        DATA_USAGE = self.get_inner_html(*MyEEWebHomePagePaygLocator.ALLOWNACES_WINDOW_FIELD)
        if "left of" in DATA_USAGE :
            return True
        else:
            return False
    
    def method_click_data_allowance_field(self):
        self.click_element(*MyEEWebHomePagePaygLocator.ALLOWNACES_WINDOW_FIELD)
    






        
    


    
        
