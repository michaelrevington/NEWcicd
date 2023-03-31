import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


#Chrome

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")

print(driver.title) #Title of the page
time.sleep(4)

driver.find_element(By.LINK_TEXT,"Create new account").click()
time.sleep(4)

driver.find_element(By.NAME,"firstname").send_keys("minoshnew")
time.sleep(2)

driver.find_element(By.NAME,"lastname").send_keys("balasuriyanew")
time.sleep(2)

driver.find_element(By.NAME,"reg_email__").send_keys("+94740845221")
time.sleep(2)

driver.find_element(By.NAME,"reg_passwd__").send_keys("Golden12@#")
time.sleep(2)



driver.find_element(By.NAME,"birthday_day").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='day']/option[8]").click()
#driver.find_element(By.NAME,"birthday_day").find_element(By.XPATH,"//*[@id='day']/option[8]").click()  #correct
time.sleep(2)
driver.find_element(By.NAME,"birthday_day").click()
time.sleep(2)

driver.find_element(By.NAME,"birthday_month").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='month']/option[9]").click()
time.sleep(2)
driver.find_element(By.NAME,"birthday_month").click()
time.sleep(2)

driver.find_element(By.NAME,"birthday_year").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='year']/option[27]").click()
time.sleep(2)
driver.find_element(By.NAME,"birthday_year").click()
time.sleep(2)


driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input").click()
time.sleep(2)

driver.find_element(By.NAME,"websubmit").click()
time.sleep(2)



time.sleep(200)
print(driver.title) #Title of the page
time.sleep(20)

driver.close() #close the browser