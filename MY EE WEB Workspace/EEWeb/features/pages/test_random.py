from selenium import webdriver
import os

dirpath = os.getcwd()
chrome_driver_path_used = dirpath + r'/features/resources/drivers/chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver_path_used)
driver.implicitly_wait(30)
driver.set_page_load_timeout(30)
driver.maximize_window()

# click radio button
driver.navigate_url('https://www.google.com/')

ele = diver.find_elements_by_xpath("//div[@class='jhp big' and @id='searchform']")
txxt = ele.get_attribute('outerHTML')

print(txxt)