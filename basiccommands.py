import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



#Chrome
#browser = webdriver.Chrome()
driver = webdriver.Chrome()

#browser.get("https://www.facebook.com/")
driver.get("https://www.facebook.com/")
time.sleep(5)
print(driver.title) #Title of the page

driver.find_element(By.LINK_TEXT,"Forgotten password?").click()
time.sleep(5)
#print (browser.current_url) #returns the URL of the page

#print (browser.page_source) #HTML code for the page

driver.get("https://www.facebook.com/pages/create/?ref_type=registration_form")
time.sleep(5)

driver.find_element(By.CLASS_NAME,"signup_btn").click()
#driver.find_elements_by_xpath("//*['@id=blueBarDOMInspector']/div/div[2]/div/div/span/a").click()
print(driver.title) #Title of the page
time.sleep(2)
driver.back()
time.sleep(5)

print(driver.title)

driver.forward()
time.sleep(5)

print(driver.title)

time.sleep(5) # sleep time for browser
driver.close() #close the browser


