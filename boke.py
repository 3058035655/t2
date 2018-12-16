import time
from selenium import webdriver
driver=webdriver.Chrome()
print(driver.get_cookies())
driver.get("http://192.168.1.249:9901/hkjf/loginAdmin.do?method=tologin")
print(driver.get_cookies())
