from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from pages.test_base import TestBase
from pages.page_base import PageBase

test_base = TestBase()

@then(u'I Get The Required Output Values "{scenario_name}" and Loged Out From The TooKit Application')
def step_impl(context, scenario_name):
    context.header.method_click_on_logout_link()
    context.header.wait_for_page_title('Toolkit - Log in')
    test_base.takesScreenshot()
    test_base.storeAllSceenshotsIntoPDFFile(scenario_name)
