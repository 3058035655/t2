# # -*- coding: utf-8 -*-
# from selenium import webdriver
# from time import sleep
# 
# WIDTH = 320
# HEIGHT = 640
# PIXEL_RATIO = 3.0
# UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'
# 
# mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
# options = webdriver.ChromeOptions()
# options.add_experimental_option('mobileEmulation', mobileEmulation)
# 
# driver = webdriver.Chrome(executable_path='chromedriver2.exe', chrome_options=options)
# driver.get('https://www.hongkunjinfu.com/hkjftest/mobile/index.do?method=getIndexPage')
# driver.set_window_size(WIDTH,HEIGHT)
# sleep(3)
# from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# binary = FirefoxBinary('C:\Program Files\Mozilla Firefox')
# driver = webdriver.Firefox(firefox_binary=binary)
# browser = driver.Firefox()
# browser.get("http://www.baidu.com")
# browser.find_element_by_id("kw").send_keys("selenium")
# browser.find_element_by_id("su").click()
# browser.quit()
#coding:utf-8
from selenium import webdriver
import time
# brower = webdriver.Chrome()
brower=webdriver.Firefox()
# brower=webdriver.Ie()

brower.get("http://www.baidu.com")
brower.find_element_by_id('kw').send_keys('selenium')
brower.find_element_by_id('su').click()

time.sleep(3)
brower.close()