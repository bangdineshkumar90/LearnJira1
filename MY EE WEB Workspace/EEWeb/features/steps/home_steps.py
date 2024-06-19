from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from pages.test_base import TestBase
from pages.page_base import PageBase

test_base = TestBase()

# @then(u'I Search Customer Details "{ctn}"')
# def step_impl(context, ctn):
#     context.home_page.method_customer_search(ctn)
#     time.sleep(20)
#     test_base.takesScreenshot()

# @then(u'I Validate The Customer Details "{ctn}" "{customerName}" "{customerType}" "{accountNumber}"')
# def step_impl(context, ctn, customerName, customerType, accountNumber):
#     assert_equal(context.home_page.method_get_customer_details_header(ctn), ctn)
#     assert_equal(context.home_page.method_get_customer_name(), customerName)
#     assert_equal(context.home_page.method_get_customer_type(), customerType)
#     assert_equal(context.home_page.method_get_customer_account_number(), accountNumber)

# @then(u'I Validate The Customer View Details "{accountHolder}" "{accountNumber}" "{ctn}"')
# def step_impl(context, accountHolder, accountNumber, ctn):
#     assert_equal(context.home_page.method_get_account_holder(), accountHolder)
#     assert_equal(context.home_page.method_get_account_number(), accountNumber)
#     assert_equal(context.home_page.method_get_mobile_number(), ctn)

# @then(u'I Navigated To "{toolname}" Application and Get The Required Output Values "{scenario_name}" "{ctn}"')
# def step_impl(context, toolname, scenario_name, ctn):
#     context.home_page.method_customer_search(toolname)
#     search_datetime = test_base.getCurrentDateTime()
#     test_base.generateResultCSV(scenario_name, ctn, search_datetime)
#     time.sleep(20)
#     test_base.takesScreenshot()

# @then(u'I Find Customer Details "{ctn}" and Get The Required Output Values "{scenario_name}"')
# def step_impl(context, ctn, scenario_name):
#     context.home_page.method_customer_search(ctn)
#     search_datetime = test_base.getCurrentDateTime()
#     test_base.generateResultCSV(scenario_name, ctn, search_datetime)
#     time.sleep(20)
#     test_base.takesScreenshot()

# @then(u'I Navigated To Albert "{toolname}" Application and Get The Required Output Values "{scenario_name}" "{ctn}"')
# def step_impl(context, toolname, scenario_name, ctn):
#     context.home_page.method_customer_search(toolname)
#     search_datetime = test_base.getCurrentDateTime()
#     test_base.generateResultCSV(scenario_name, ctn, search_datetime)
#     time.sleep(20)
#     test_base.takesScreenshot()
