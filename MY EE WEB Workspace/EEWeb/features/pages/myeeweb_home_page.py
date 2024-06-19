from selenium.webdriver.common.by import By
import time
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


delay_min = 3 # sec
delay_medium = 5 # sec
delay_max = 10 # sec

#dynamic web elements
DeviceSelectionXpath = "//*[@href='/auth/mobile-phones/upg-pay-monthly/xxxxxx/details']"
PlanSelectionXpath = "//strong[contains(text(), 'xxxxxx')]/ancestor::div[@class='plan-item__header']/following-sibling::div//form/button[contains(text(),'Choose this plan')]"
EachRowXpath = "//div[@id='planDetailsCollapse']//table//tbody/tr[xxxxxx]/td[1]"

class MyEEWebHomePageLocator(object):
    # Menu Locators
    MENU_BUTTON = (By.XPATH, "//body/div[@id='eed-off-canvas']/div/div[@id='main']/section/button[1]")
    BAN_FIELD = (By.NAME, "ctnNo")
    ACCOUNT_BUTTON = (By.XPATH,"//a[@id='landing_burgermenu_account_settings']")
    PLAN_BUTTON = (By.XPATH, "//a[@id='landing_burgermenu_my_plan']")
    PLAN_DETAILS = (By.XPATH, "//a[contains(text(),'Plan details')]")

    # Plan Details locator
    PLAN_DETAIL_FIELD = (By.XPATH, "//div[@id='planDetailsCollapse']/h2[contains(text(),'Plan Details')]")   
    PLAN_DETAIL_TABLE = (By.XPATH, "//div[@id='planDetailsCollapse']//table")
    TABLE_ROWS_COUNT = (By.XPATH, "//div[@id='planDetailsCollapse']//table//tbody/tr")

    #Upgrade locators
    OFFER_UPGRADE_BUTTON = (By.XPATH, "//*[@id='landing_burgermenu_offers_and_upgrade']")
    NEXT_UPGRADE_BUTTON = (By.XPATH, "//*[@id='next_upgrade_date']/a")
    LOG_OUT_BUTTON = (By.XPATH, "//span[contains(text(),'Log out') and @class='eed-header-auth__text eed-logout']")
    BILL_BUTTON = (By.XPATH, "//a[@id='landing_burgermenu_bills_and_payments']")
    PAY_BILL_CARD_BUTTON = (By.XPATH, "//a[contains(text(),'Pay by bill card')]")
    AMOUNT_INPUT = (By.NAME, "topUpAmount")
    NEXT_BUTTON = (By.XPATH, "//button[@id='confirm-amount']")
    CARD_TYPE_FIELD = (By.XPATH, "//*[@id='cardType']")
    NAME_ON_CARD_FIELD = (By.NAME, "nameOnCard")
    CARD_NUMBER_FIELD = (By.NAME, "creditCardNumber")
    EXPIRY_DATE_MONTH = (By.NAME, "expirationMonth")
    EXPIRY_DATE_YEAR = (By.NAME, "expirationYear")
    CVV_FIELD = (By.NAME, "cardSecurityCode")
    CONTINUE_BUTTON = (By.XPATH, "//*[@id='btnContinue']")
    PAY_NOW_BUTTON = (By.XPATH, "//*[@id='paymentConfirmationId]")
    ADVANCE_BUTTON = (By.XPATH, "//*[@id='details-button']")
    PRIVACY_LINK = (By.XPATH, "//*[@id='proceed-link']")
    UPGRADE_NOW_BUTTON = (By.XPATH, "//*[@id='device-plan']/div[2]/a")
    SEE_ALL_PHONE = (By.XPATH, ".//*[@href='/auth/mobile-phones/upg-pay-monthly/gallery?lnk=main_upgrade_gallery']")
    SEE_ALL_PLANS = (By.XPATH, "//a[@class='btn btn--secondary see-all-plans see-all-plans__cta display-inline-block trigger-click']")
    SEE_MORE_PLANS = (By.XPATH,"//*[@id='cards-gallery']/a/span")
    NEXT_BUTTON = (By.XPATH, "//*[@id='btnCheckoutLinkTop']")
    DELIVERY_METHOD_RADIO_BUTTON = (By.XPATH, "//a[@id='select-standard-delivery']/span[2]/span")
    ACCOUNT_HOLDER_NAME_FIELD = (By.XPATH, "//input[@id='holderName']")
    BANK_ACCOUNT_NUMBER_FIELD = (By.XPATH, "//input[@id='accountNumber']")
    SORT_CODE_FIELD1 = (By.XPATH, "//input[@id='sortCode1']")
    SORT_CODE_FIELD2 = (By.XPATH, "//input[@id='sortCode2']")
    SORT_CODE_FIELD3 = (By.XPATH, "//input[@id='sortCode3']")

class MyEEWebHomePage(PageBase):
    # Login Page Methods
    def close_intro_page(self):
        self.colse_msg()

    def method_menu_operation_plan_details(self):
        self.click_element(*MyEEWebHomePageLocator.MENU_BUTTON)
        self.click_element(*MyEEWebHomePageLocator.PLAN_BUTTON)
        self.click_element(*MyEEWebHomePageLocator.PLAN_DETAILS)
    
    def method_get_info_by_attribute(self):
        return self.get_text_by_value(*MyEEWebHomePageLocator.BAN_FIELD)

    def method_log_out_EE_web_application(self):
        self.click_element(*MyEEWebHomePageLocator.LOG_OUT_BUTTON)

    def method_menu_operation_bill_payment(self):
        self.click_element(*MyEEWebHomePageLocator.MENU_BUTTON)
        self.click_element(*MyEEWebHomePageLocator.BILL_BUTTON)
        self.click_element(*MyEEWebHomePageLocator.PAY_BILL_CARD_BUTTON)

    def method_payment_amount_newcard(self,amount):
        self.enter_text(amount,*MyEEWebHomePageLocator.AMOUNT_INPUT)
        self.click_element(*MyEEWebHomePageLocator.NEXT_BUTTON)

    def method_credit_card_detals(self):
        self.enter_text("visa",*MyEEWebHomePageLocator.CARD_TYPE_FIELD)
        self.enter_text("Anusha",*MyEEWebHomePageLocator.NAME_ON_CARD_FIELD)
        self.enter_text("4929420045850815",*MyEEWebHomePageLocator.CARD_NUMBER_FIELD)
        self.enter_text("02",*MyEEWebHomePageLocator.EXPIRY_DATE_MONTH)
        self.enter_text("2024",*MyEEWebHomePageLocator.EXPIRY_DATE_YEAR)
        self.enter_text("123",*MyEEWebHomePageLocator.CVV_FIELD)
        self.click_element(*MyEEWebHomePageLocator.CONTINUE_BUTTON)
    
    def method_comfirm_payment(self):
        self.click_element(*MyEEWebHomePageLocator.PAY_NOW_BUTTON)

    def method_handle_privacy_error(self):
        self.click_element(*MyEEWebHomePageLocator.ADVANCE_BUTTON)
        self.click_element(*MyEEWebHomePageLocator.PRIVACY_LINK)

    def method_menu_operation_upgrade_payment(self):
        self.click_element(*MyEEWebHomePageLocator.MENU_BUTTON)
        self.click_element(*MyEEWebHomePageLocator.OFFER_UPGRADE_BUTTON)
        self.click_element(*MyEEWebHomePageLocator.NEXT_UPGRADE_BUTTON)
    
    def method_see_all_phone(self):
        self.click_element(*MyEEWebHomePageLocator.SEE_ALL_PHONE)
    
    def method_select_device(self, Device):
        DYNAMIC_DEVICE_SELECTION = self.prepareDynamicXpath(DeviceSelectionXpath, Device)
        self.click_element(By.XPATH, DYNAMIC_DEVICE_SELECTION)

    def method_select_plan(self, Plan):
        selectplan = Plan.split()
        self.click_element(*MyEEWebHomePageLocator.SEE_ALL_PLANS)
        self.click_element(*MyEEWebHomePageLocator.SEE_MORE_PLANS)
        DYNAMIC_PLAN_SELECTION = self.prepareDynamicXpath(PlanSelectionXpath, selectplan[1])
        self.click_element(By.XPATH, DYNAMIC_PLAN_SELECTION)
    
    def method_addon_extras_offer(self):
        self.click_element(*MyEEWebHomePageLocator.NEXT_BUTTON)
    
    def method_account_details(self, AccountHolderName, AccountNo, SortCode):
        self.click_element(*MyEEWebHomePageLocator.DELIVERY_METHOD_RADIO_BUTTON)
        self.enter_text(AccountHolderName, *MyEEWebHomePageLocator.ACCOUNT_HOLDER_NAME_FIELD)
        self.enter_text(AccountNo, *MyEEWebHomePageLocator.BANK_ACCOUNT_NUMBER_FIELD)
        self.enter_text(SortCode[0:2],*MyEEWebHomePageLocator.SORT_CODE_FIELD1)
        self.enter_text(SortCode[2:4],*MyEEWebHomePageLocator.SORT_CODE_FIELD2)
        self.enter_text(SortCode[4:6],*MyEEWebHomePageLocator.SORT_CODE_FIELD3)
    
    def check_customer_upgrade_eligible():
        if assert_equal(self.check_element_exist(*MyEEWebHomePageLocator.UPGRADE_NOW_BUTTON),"True"):
            self.click_element(*MyEEWebHomePageLocator.UPGRADE_NOW_BUTTON)
        else:
            print("Upgrade is not eleigible")

    def method_get_table_plan_detail(self):
        self.check_element_exist(*MyEEWebHomePageLocator.PLAN_DETAIL_FIELD)
        self.click_element(*MyEEWebHomePageLocator.PLAN_DETAIL_FIELD)
        ROW_COUNT = len(TABLE_ROWS_COUNT)
        PlanSummaryList = []
        
        for rows in ROW_COUNT:
            counter = 1
            DYNAMIC_ROW_DATA = self.prepareDynamicXpath(DeviceSelectionXpath, counter)
            PlanSummaryList.append(self.get_text(By.XPATH, DYNAMIC_ROW_DATA))
            print(PlanSummaryList[counter])
            counter = counter + 1
        return PlanSummaryList
    
    def method_verify_list(self, PlanSummaryList, UserList):
        if(set(UserList).issubset(set(PlanSummaryList))): 
            return True
        else:
            return False
        

        


    
        
    
    
    






        
    


    
        
