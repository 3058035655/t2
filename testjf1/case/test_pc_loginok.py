#-*- coding:utf-8 -*-
import unittest
import time
import sys

import requests
import xlrd
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from db import Db
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from testjf1.common.loginpage import LoginPage

class Test_Newyyy_pctz_shfk (unittest.TestCase):
    def test_pcLogin(self):

        driver = webdriver.Chrome ()
        driver.get ('https://www.hongkunjinfu.com/hkjf/index.do?method=getIndexPage')
        WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
        driver.find_element_by_id ('login').send_keys ('14510000051')
        time.sleep (1)
        e1 = driver.find_element_by_xpath (".//*[@id='txt2']")
        action = ActionChains (driver)
        action.move_to_element (e1).click ().send_keys ("8b08c0bd2c536072a4bed2ddebcc4f01a73549106e04d12659aed56cf938d6b72f3a53149b488e4a309f2fe9851d8d3ad60a429cbe4e82dd16cfb1206dc7c7752ddf861a79374247777d76d3188061738b196fddd53e3f0ae1044c525fa9f35de6cfa0ce69dd2f2e30e4211acfd8a4d806d9c22bb5130aa68eceda6cc78c9630").perform ()

        driver.find_element_by_xpath (".//*[@id='logindiv']/div/div[2]").submit ()
        # driver.find_element_by_xpath (".//*[@id='txt2']").send_keys('a12345')
        # driver.find_element_by_xpath (".//*[@id='logindiv']/div/div[2]").click()
        time.sleep (1)
        driver.get("http://192.168.1.249:9901/hkjf")
        # address=("http://192.168.1.249:9901/hkjf/investControllerFront.do?method=detail&code=ed791706-92f7-4435-b6f6-aa944ed87f4c")
        time.sleep(10)
        driver.close()
if __name__ == '__main__':
    unittest.main ()

