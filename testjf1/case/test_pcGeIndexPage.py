#-*- coding:utf-8 -*-
import unittest
import time
import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
from utils.log import logger
import os
sys.path.append('D:\\jftest1_CG\\test1')
from testjf1.common.loginpage import LoginPage
from PIL import ImageGrab
from utils.config import Config
url = Config().get ('QTURL')
print(url)
class Test_PcIndexPage(unittest.TestCase):
    def test_pcLogin(self):
        # driver = webdriver.Chrome ()
        driver=webdriver.Firefox()
        driver.maximize_window ()
        driver.get(url)
        WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
        sy=driver.find_element_by_xpath("html/body/div[2]/div[2]/div/ul/li[1]/a").text
        smjj=driver.find_element_by_xpath("html/body/div[2]/div[2]/div/ul/li[2]/a").text
        hydl=driver.find_element_by_xpath(".//*[@id='logindiv']/div/h1").text
        self.assertEqual(sy,"首页")
        self.assertEqual(smjj,"私募基金")
        self.assertEqual(hydl,"欢迎登录")
        pic = ImageGrab.grab()
        pic.save('D:/t金服_测试/report/shotcut/金服PC首页.jpg')
        # logger.info(t)
        t=driver.find_element_by_xpath("html/body/div[4]/ul/li[1]/div/h3")#精英团队
        t1=driver.find_element_by_xpath("html/body/div[4]/ul/li[1]/div/div/img")#精英团队图片
        driver.execute_script("arguments[0].scrollIntoView();", t1)  #滚动到指定元素位置
        #截长图
        # driver = webdriver.Chrome()
        # driver.get('png/')
        # driver.save_screenshot('screenshot.png')
        # left = element.location['x']
        # top = element.location['y']
        # right = element.location['x'] + element.size['width']
        # bottom = element.location['y'] + element.size['height']
        # im = Image.open('screenshot.png')
        # im = im.crop((left, top, right, bottom))
        # im.save('screenshot.png')
        driver.close()

if __name__ == '__main__':
    unittest.main ()

