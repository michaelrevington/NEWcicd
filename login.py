import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#Chrome

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")

print(driver.title) #Title of the page
time.sleep(4)

driver.find_element(By.ID,"email").send_keys("minoshbalasuriya12@gmail.com")
driver.find_element(By.ID,"pass").send_keys("Golden12@#")
time.sleep(5)

driver.find_element(By.NAME,"login").click()
time.sleep(5)

act_title=driver.title
exp_title="(20+) Facebook"

if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")


time.sleep(20)
print(driver.title) #Title of the page
time.sleep(20)

driver.close() #close the browser