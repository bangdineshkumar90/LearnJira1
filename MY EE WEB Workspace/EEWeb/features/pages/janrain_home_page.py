from selenium.webdriver.common.by import By
import time
from pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


delay_min = 3 # sec
delay_medium = 5 # sec
delay_max = 9 # sec



class JanrainHomePageLocator(object):
    # Login Page Locators
    MANAGE_PROFILE_DROPDOWN = (By.XPATH, "//a[@class='md-button menu layout-row']//span[@class='title ng-binding flex'][contains(text(),'Manage Profiles')]")
    USER_BUTTON = (By.XPATH, "//div[@class='ng-scope layout-column']//button[@class='menu md-button ng-scope md-ink-ripple']")
    CREATE_PROFILE_BUTTON = (By.XPATH, "//a[@class='md-accent md-raised md-button ng-scope md-ink-ripple']")
    ASSIGNED_ROLES_DROPDOWN = (By.XPATH,"//div[3]//div[1]//div[1]//md-content[1]//div[1]//button[1]")
    ADD_NEWENTRY_BUTTON = (By.XPATH,"//button[@class='md-primary md-button md-ink-ripple']")
    CREATED_TIME_BUTTON = (By.XPATH,"//div[@class='inset lefts']//full-profile-form[@class='ng-isolate-scope']//div[@class='inset']//div[@class='ng-scope layout-column']//div[@class='md-padding-left layout-column']//div[@class='ng-scope layout-column']//div[@class='layout-align-start-stretch layout-row']//div//div//button[@class='md-icon-button md-button md-ink-ripple']")
    CREATED_TIME_OK_BUTTON = (By.XPATH,"//button[contains(text(),'OK')]")
    LABEL_FILED = (By.NAME,"assignedRoles.label")
    MANAGED_OBJECT_FILED = (By.NAME,"assignedRoles.managedObject")
    RELATED_MANAGED_OBJECT_FILED = (By.NAME,"assignedRoles.relatedManagedObject")
    ROLETYPE_FILED = (By.NAME,"assignedRoles.roleType")
    EMAIL_FILED = (By.NAME,"email")
    EMAIL_VERIFIED_TIME_BUTTON = (By.XPATH,"//div[14]//div[1]//div[1]//div[1]//div[1]//div[1]//mdp-time-picker[1]//div[1]//button[1]")
    EMAIL_VERIFIED_TIME_OK_BUTTON = (By.XPATH,"//button[contains(text(),'OK')]")
    GIVEN_NAME_FILED = (By.NAME,"givenName")
    PASSWORD_FILED = (By.NAME,"password")
    SAVE_BUTTON = (By.XPATH,"//button[@class='md-fab md-fab-bottom-right md-primary fixed-fab-button md-button md-ink-ripple']")
    SUCCESSFUL_SAVE_MSG = (By.XPATH,"//span[@class='md-toast-text ng-binding ng-scope']")
    VIEW_BUTTON = (By.XPATH,"//button[@class='md-highlight md-button ng-scope md-ink-ripple']")
    PROFILE_BUTTON = (By.XPATH,"//div[@class='layout-column flex']//div[4]//md-menu[1]//button[1]")
    SIGN_OUT_BUTTON = (By.XPATH,"//md-menu-content[@class='md-user-menu-content']//button[@class='md-button md-ink-ripple']")


class JanrainHomePage(PageBase):
    # Login Page Methods
    def method_click_on_user_button(self):
        self.click_element(*JanrainHomePageLocator.MANAGE_PROFILE_DROPDOWN)
        self.click_element(*JanrainHomePageLocator.USER_BUTTON)

    def method_click_on_createprofile_button(self):
        self.click_element(*JanrainHomePageLocator.CREATE_PROFILE_BUTTON)

    def method_click_on_assignedrole_button(self):
        self.click_element(*JanrainHomePageLocator.ASSIGNED_ROLES_DROPDOWN)
        self.click_element(*JanrainHomePageLocator.ADD_NEWENTRY_BUTTON)
        time.sleep(5)
        
    def method_to_fill_profile_info(self, BAN, RoleType, RelatedManagedObject,Mail):
        self.click_element(*JanrainHomePageLocator.CREATED_TIME_BUTTON)
        time.sleep(1)
        self.click_element(*JanrainHomePageLocator.CREATED_TIME_OK_BUTTON)
        time.sleep(2)
        # self.enter_text(BAN,*JanrainHomePageLocator.LABEL_FILED)
        # time.sleep(2)
        # self.enter_text(RoleType,*JanrainHomePageLocator.ROLETYPE_FILED)
        # time.sleep(2)
        # self.enter_text(RelatedManagedObject,*JanrainHomePageLocator.MANAGED_OBJECT_FILED)
        # time.sleep(2)
        if RoleType == "LegalOwner":
            self.enter_text(BAN,*JanrainHomePageLocator.LABEL_FILED)
            time.sleep(2)
            self.enter_text(RelatedManagedObject,*JanrainHomePageLocator.MANAGED_OBJECT_FILED)
            time.sleep(2)
            self.enter_text(RoleType,*JanrainHomePageLocator.ROLETYPE_FILED)
            time.sleep(2)

        elif RoleType == "EndUser":
            self.enter_text(CTN,*JanrainHomePageLocator.LABEL_FILED)
            time.sleep(2)
            self.enter_text(ManagedObject,*JanrainHomePageLocator.MANAGED_OBJECT_FILED)
            time.sleep(2)
            self.enter_text(RelatedManagedObject,*JanrainHomePageLocator.RELATED_MANAGED_OBJECT_FILED)
            time.sleep(2)
            self.enter_text(RoleType,*JanrainHomePageLocator.ROLETYPE_FILED)
            time.sleep(2)
        
        mail1 = Mail+"@yopmail.com"
        time.sleep(2)
        self.enter_text(mail1,*JanrainHomePageLocator.EMAIL_FILED)
        time.sleep(2)
        self.enter_text(Mail,*JanrainHomePageLocator.GIVEN_NAME_FILED)
        time.sleep(2)
        self.click_element(*JanrainHomePageLocator.EMAIL_VERIFIED_TIME_BUTTON)
        time.sleep(2)
        self.click_element(*JanrainHomePageLocator.EMAIL_VERIFIED_TIME_OK_BUTTON)
        time.sleep(2)
        self.enter_text("Password2",*JanrainHomePageLocator.PASSWORD_FILED)
        time.sleep(2)
        self.click_element(*JanrainHomePageLocator.SAVE_BUTTON)
        time.sleep(4)
        
    def method_to_verify_save_success(self):
        message = self.get_text(*JanrainHomePageLocator.SUCCESSFUL_SAVE_MSG)

        if message == "Full Record Profile successfully created":
            return "True"
        else:
            return "False"

    def method_log_out_from_Janrain(self):
        self.click_element(*JanrainHomePageLocator.PROFILE_BUTTON)
        time.sleep(2)
        self.click_element(*JanrainHomePageLocator.SIGN_OUT_BUTTON)
        time.sleep(2)


        
