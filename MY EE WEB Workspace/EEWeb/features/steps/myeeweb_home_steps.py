from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.test_base import TestBase
from pages.page_base import PageBase

test_base = TestBase()

@then(u'I Verify Account Information "{BAN}"')
def step_impl(context,BAN):
    try:
        time.sleep(20)
        context.myeeweb_home_page.close_intro_page()
        test_base.takesScreenshot()
        assert_equal(context.myeeweb_home_page.method_get_info_by_attribute(),BAN)
    except Exception as e:
        print('Exception Found: '+e)
        print('========== Verification of Account Is Not Successfully ==========')
    
@then(u'Review the Plan Summery(PAYM)')
def step_impl(context):
    try:
        UserList = ['Plan', 'Bill date', 'Start date', 'End date', 'Plan length']
        context.myeeweb_home_page.close_intro_page()
        context.myeeweb_home_page.wait_for_page_title('My EE PAYM Landing')
        test_base.takesScreenshot()
        context.myeeweb_home_page.method_menu_operation_plan_details()
        context.myeeweb_home_page.wait_for_page_title('My EE Plan details')
        test_base.takesScreenshot()
        PlanSummaryList = context.myeeweb_home_page.method_get_table_plan_detail()
        assert_equal(context.myeeweb_home_page.method_verify_list(PlanSummaryList, UserList),True)

    except Exception as e:
        print('Exception Found: '+e)
        print('========== Review Plan summery Is Not Successfully ==========')

@then(u'I am Logged Out From MY EE Web Application')
def step_impl(context):
    try:
        time.sleep(2)
        context.myeeweb_home_page.method_log_out_EE_web_application()
    except Exception as e:
        print('Exception Found: '+e)
        print('========== Log out from MY EE WEB APP Is Not Successfully ==========')

@then(u'I go to the Bill Payment option')
def step_impl(context):
    try:
        context.myeeweb_home_page.close_intro_page()
        context.myeeweb_home_page.method_menu_operation_bill_payment()
        time.sleep(15)
        test_base.takesScreenshot()
        context.myeeweb_home_page.wait_for_page_title('Make Payment')
    except Exception as e:
        print('Exception Found: '+e)
        print('========== Bill payment operation Is Not Successfully ==========')
    
@then(u'I Verify EE PAYM Able To Make Bill Payment With Card Details "{Amount}"')
def step_impl(context,Amount):
    try:
        context.myeeweb_home_page.method_payment_amount_newcard(Amount)
        time.sleep(20)
        if assert_equal(context.myeeweb_home_page.get_page_title(),"Privacy error"):
            test_base.takesScreenshot()
            context.myeeweb_home_page.method_handle_privacy_error
            time.sleep(10)
        context.myeeweb_home_page.wait_for_page_title('My EE')
        test_base.takesScreenshot()
        time.sleep(10)
        context.myeeweb_home_page.method_credit_card_detals()
        test_base.takesScreenshot()
        time.sleep(10)
        context.myeeweb_home_page.method_comfirm_payment()
        test_base.takesScreenshot()
    except Exception as e:
        print('Exception Found: '+e)
        print('========== Fail to make payment for PAYM customer ==========')

@then(u'I go to the Upgrade Menu option')
def step_impl(context):
    try:
        context.myeeweb_home_page.close_intro_page()
        context.myeeweb_home_page.method_menu_operation_upgrade_payment()
        test_base.takesScreenshot()
        time.sleep(10)
        context.myeeweb_home_page.wait_for_page_title('My EE - Upgrades')
    except Exception as e:
        print('Exception Found: '+e)
        print('========== Upgrade menu operation Is Not Successfully ==========')

@then(u'I Select Device and Price Plan As Per Requierment And Added Addredss Detials And Account Information "{Device}" "{Plan}" "{AccountHolderName}" "{AccountNo}" "{SortCode}"')
def step_impl(context, Device, Plan, AccountHolderName, AccountNo, SortCode):
    try:
        context.myeeweb_home_page.wait_for_page_title('My EE - Upgrades')
        context.myeeweb_home_page.check_customer_upgrade_eligible()
        test_base.takesScreenshot()
        context.myeeweb_home_page.wait_for_page_title('Recommendations | Upgrade | EE')
        context.myeeweb_home_page.method_see_all_phone()
        test_base.takesScreenshot()
        context.myeeweb_home_page.wait_for_page_title('Pay Monthly Phones')
        context.myeeweb_home_page.method_select_device(Device)
        test_base.takesScreenshot()
        context.myeeweb_home_page.wait_for_page_title('Upgrade | '+device+' | Pay Monthly Deals & Contracts | EE')
        context.myeeweb_home_page.method_select_plan(Plan)
        test_base.takesScreenshot()
        context.myeeweb_home_page.wait_for_page_title('Benefits | Upgrade  | EE')
        context.myeeweb_home_page.method_addon_extras_offer()
        test_base.takesScreenshot()
        context.myeeweb_home_page.wait_for_page_title('Extras | Upgrade  | EE')
        context.myeeweb_home_page.method_addon_extras_offer()
        test_base.takesScreenshot()
        context.myeeweb_home_page.wait_for_page_title('Checkout summary | Upgrade | EE')
        context.myeeweb_home_page.method_account_details(AccountHolderName, AccountNo, SortCode)
        test_base.takesScreenshot()

    except Exception as e:
        print('Exception Found: '+e)
        print('========== Device And Price Plan Selection Is Not Successfully ==========')