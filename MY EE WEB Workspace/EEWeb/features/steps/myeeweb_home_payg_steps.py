from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.test_base import TestBase
from pages.page_base import PageBase

test_base = TestBase()

@then(u'I Verify User Is Able To See Data Useage On MY EE Home Page')
def step_impl(context):
    try:
        context.myeeweb_home_page.close_intro_page()
        test_base.takesScreenshot()
        context.myeeweb_home_page_payg.method_click_data_allowance_field()
        test_base.takesScreenshot()
        assert_equal(context.myeeweb_home_page_payg.method_verify_data_usage(),True)
    except Exception as e:
        print('Exception Found: '+e)
        print('========== Verification of Data Usage Is Not Successfully ==========')

@then(u'I go to the TopUp Menu option')
def step_impl(context):
    try:
        test_base.takesScreenshot()
        context.myeeweb_home_page_payg.method_click_on_menu_button()
        time.sleep(50)
        #context.myeeweb_home_page_payg.wait_for_page_title("Top up")
        #assert_equal(context.myeeweb_home_page_payg.get_page_title(),"Top up")
        test_base.takesScreenshot()
    except Exception as e:
        print('Exception Found: '+e)
        print('========== Menu Operation Is Not Successfully ==========')

@then(u'I Select Payment Option With Registered Card And Confirm The Topup Ammount "{TopUpAmmount}"')
def step_impl(context, TopUpAmmount):
    try:
        test_base.takesScreenshot()
        context.myeeweb_home_page_payg.method_topup_ammount(TopUpAmmount)
        test_base.takesScreenshot()
        if context.myeeweb_home_page_payg.method_to_verify_registered_card() == True:
            context.myeeweb_home_page_payg.method_to_enter_registered_card_details()
        assert_equal(context.myeeweb_home_page_payg.get_page_title(),"My EE")
        context.myeeweb_home_page_payg.method_confirm_payment()
        test_base.takesScreenshot()
        assert_equal(context.myeeweb_home_page_payg.get_page_title(),"My EE")
    except Exception as e:
        print('Exception Found: '+e)
        print('========== Top Up Operation Is Not Successfully ==========')
       
@then(u'I Verify Topup Payment Successfull Done')
def step_impl(context):
    try:
        test_base.takesScreenshot()
        assert_equal(context.myeeweb_home_page_payg.method_complete_payment(),"Your top-up was successful.")
        context.myeeweb_home_page_payg.method_complete_payment()
        test_base.takesScreenshot()
    except Exception as e:
        print('Exception Found: '+e)
        print('========== Top Up complete Verification Is Not Successfully ==========')

@then(u'I Verify Account Information For PAYG "{BAN}"')
def step_impl(context,BAN):
    try:
        context.myeeweb_home_page_payg.method_menu_click()
        test_base.takesScreenshot()
        assert_equal(context.myeeweb_home_page_payg.method_get_account_info(),BAN)
        test_base.takesScreenshot()
    except Exception as e:
        print('Exception Found: '+e)
        print('========== Account Verification Is Not Successfully ==========')