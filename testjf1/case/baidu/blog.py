# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest, time, re
from utils.config import DATA_PATH



class TestNewsanbiaoday(unittest.TestCase):
    excel = DATA_PATH + '/sanbiao_day.xlsx'
    def test_newsanbiaoday(self):
        driver=webdriver.Chrome()
        driver.get("https://www.hongkunjinfu.com/loginAdmin.do?method=tologin")
        driver.find_element_by_xpath (".//*[@id='login']").send_keys ("yradmin")
        driver.find_element_by_xpath (".//*[@id='password']").send_keys ("a12345")
        time.sleep (2)
        # 手动输入验证码
        # driver.find_element_by_xpath (".//*[@id='apLogin']/div[1]/ul/li[3]/p[3]/img").send_keys(text)
        driver.find_element_by_id("button").submit()
        # driver.find_element_by_name('verifyCode').clear()
        #driver.find_element_by_xpath (".//*[@id='apLogin']/div[1]/ul/li[3]/p[3]/img").send_keys(text)
        #driver.find_element_by_xpath (".//*[@id='button']").click()
        driver.quit()

if __name__ == "__main__":
    unittest.main ()

