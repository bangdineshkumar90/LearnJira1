from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@then(u'I Am On Janrain Login Page')
def step_impl(context):
    try:
        context.janrain_login_page.navigate_url('https://console.janrain.com/#/login')
        context.janrain_login_page.wait_for_page_title('Janrain Console')
        assert_equal(context.janrain_login_page.get_page_title(), "Janrain Console")
        test_base.takesScreenshot()
    except Exception as e:
        print('Exception Found: '+e)
        print('========== Janrain URL Not Launched ==========')

@then(u'I Enter The Login Details "{Username}" "{Password}" And Navigate To Janrain Home Page')
def step_impl(context, Username, Password):
    try:
        context.janrain_login_page.method_enter_credentials(Username, Password)
        context.janrain_login_page.method_select_region()
        test_base.takesScreenshot()
        context.janrain_login_page.method_click_on_login_button()
        context.janrain_login_page.wait_for_page_title('Janrain Console')
        time.sleep(5)
        test_base.takesScreenshot()
    except Exception as e:
        print('Exception Found: '+e)
        print('========== Janrain Login Is Not Successfully ==========')

@then(u'I Create User Profile For Legal Owner "{BAN}" "{RoleType}" "{RelatedManagedObject}" "{Email}" and Logged Out From Application')
def step_impl(context, BAN, RoleType, RelatedManagedObject, Email):
    try:
        context.janrain_home_page.method_click_on_user_button()
        context.janrain_home_page.method_click_on_createprofile_button()
        context.janrain_home_page.method_click_on_assignedrole_button()
        test_base.takesScreenshot()
        context.janrain_home_page.method_to_fill_profile_info(BAN, RoleType, RelatedManagedObject, Email)
        time.sleep(2)
        assert_equal(context.janrain_home_page.method_to_verify_save_success(),"True")
        test_base.takesScreenshot()
        context.janrain_home_page.method_log_out_from_Janrain()
        test_base.takesScreenshot()
    except Exception as e:
        print('Exception Found: '+e)
        print('========== Profile creation process Is Not Successfully ==========')

    


