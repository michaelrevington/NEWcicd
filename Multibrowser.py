
import time
from lib2to3.pgen2 import driver

from selenium import webdriver

#driver=webdriver.Chrome(excutable_path="C:\Drivers\chromedriver_win32.exe")
#driver = webdriver.Chrome(ChromeDriverManager().install())

browser = webdriver.Chrome()
#browser  = webdriver.Ie()
#browser = webdriver.Firefox()


browser.get("https://newtours.demoaut.com/")

#print (driver.title)    #Title of the page

#driver.close()  #close the browser

print(browser.title) #Title of the page

print (browser.current_url) #returns the URL of the page

#print (browser.page_source) #HTML code for the page


time.sleep(2)   # sleep time for browser
browser.close() #close the browser
