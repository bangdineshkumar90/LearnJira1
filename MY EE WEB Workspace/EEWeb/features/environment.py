from selenium import webdriver
from browser import Browser
from pages.janrain_login_page import JanrainLoginPage
from pages.header import Header
from behave import *
from pages.home_page import HomePage
from pages.yopmail import YopmailPage
from pages.janrain_login_page import JanrainLoginPage
from pages.janrain_home_page import JanrainHomePage
from pages.myeeweb_login_page import MyEEWebLoginPage
from pages.myeeweb_home_page import MyEEWebHomePage
from pages.myeeweb_home_page_payg import MyEEWebHomePagePayg

def before_all(context):
    context.browser = Browser()
    context.yopmail = YopmailPage()
    context.janrain_login_page = JanrainLoginPage()
    context.janrain_home_page = JanrainHomePage()
    context.myeeweb_login_page = MyEEWebLoginPage()
    context.myeeweb_home_page = MyEEWebHomePage()
    context.myeeweb_home_page_payg = MyEEWebHomePagePayg()
    context.header = Header()
    context.home_page = HomePage()
    
def after_all(context):
    context.browser.closeBrowser()
    print('====== Closing the browser ======')

# def before_scenario(context, scenario):
#     if 'TC_' in str(scenario):
#         print ('===Before Scenario===' + str(scenario))
#         context.browser = Browser()
#         context.login_page = LoginPage()

# def after_scenario(context, scenario):
#     if 'TC_' in str(scenario):
#         print ('===After Scenario===' + str(scenario))
#         context.browser.close()
