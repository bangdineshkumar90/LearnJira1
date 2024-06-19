from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()

@when(u'I Am On My EE Web Login Page')
def step_impl(context):
    try:
        context.myeeweb_login_page.navigate_url('https://pit4-id.intdigital.ee.co.uk/id/login')
        time.sleep(10)
        context.myeeweb_login_page.wait_for_page_title('My EE login')
        assert_equal(context.myeeweb_login_page.get_page_title(), "My EE login")
        test_base.cleanScreenShotFolder()
        test_base.takesScreenshot()
    except Exception as e:
        print('Exception Found: '+e)
        print('========== MY EE WEB URL Not Launched ==========')

@then(u'I Am Loged In To The My EE web Application With "{Email}" "{Password2}" and Navigate to My EE Web Home Page "{CustType}"')
def step_impl(context, Email, Password2, CustType):
    try:
        time.sleep(5)
        context.myeeweb_login_page.check_cookies_page_exist()
        #context.myeeweb_login_page.method_accept_cookies()
        assert_equal(context.myeeweb_login_page.get_page_title(), "My EE login")
        time.sleep(2)
        context.myeeweb_login_page.method_enter_credentials(Email, Password2)
        test_base.takesScreenshot()
        time.sleep(5)
        #context.myeeweb_login_page.method_click_on_login_button()
        if context.myeeweb_login_page.get_page_title() == "My EE":
            context.myeeweb_login_page.wait_for_page_title('My EE')
        elif context.myeeweb_login_page.get_page_title() == 'My EE - '+CustType+' Landing':
            context.myeeweb_login_page.wait_for_page_title('My EE - '+CustType+' Landing')
        time.sleep(5)
        test_base.takesScreenshot()
    except Exception as e:
        print('Exception Found: '+e)
        print('========== MY EE Web Login Is Not Successfully ==========')
