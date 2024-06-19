from selenium import webdriver
import os

dirpath = os.getcwd()
chrome_driver_path_used = dirpath + r'/features/resources/drivers/chromedriver.exe'

class Browser(object):

    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path=chrome_driver_path_used)
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()
    print('====== Opening Chrome browser ======')

    def closeBrowser(context):
        context.driver.close()
        # context.driver.quit()
