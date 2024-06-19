from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.page_base import PageBase
from pages.test_base import TestBase

test_base = TestBase()
@given(u'I Am On Yopmail Page')
def step_impl(context):
    try:
        context.yopmail.navigate_url('http://www.yopmail.com/en/')
        context.yopmail.method_access_yopmail()
        context.yopmail.wait_for_page_title('YOPmail - Disposable Email Address')
        assert_equal(context.yopmail.get_page_title(), "YOPmail - Disposable Email Address")
        test_base.cleanScreenShotFolder()
        test_base.takesScreenshot()
    except Exception as e:
        print('Exception Found: '+e)
        print('========== ToolKit URL Not Launched ==========')


@then(u'I Create Yopmil EmailID "{Email}"')
def step_impl(context, Email):
    try:
        context.yopmail.method_search_email(Email)
        context.yopmail.wait_for_page_title('YOPmail - Inbox')
    except Exception as e:
        print('Exception Found: '+e)
        print('========== ToolKit URL Not Launched ==========')