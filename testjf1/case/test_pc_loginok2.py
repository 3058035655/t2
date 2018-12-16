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
class Test_Pclogin2(unittest.TestCase):
    def test_pcLogin2(self):
        # driver = webdriver.Chrome ()
        driver=webdriver.Firefox()
        driver.maximize_window ()
        driver.get(url)
        WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
        driver.find_element_by_id ('login').send_keys ('14510000051')
        js = "document.getElementById('password').style.display='block'"  # 编写JS语句
        driver.execute_script (js)  # 执行JS
        driver.find_element_by_id ('password').send_keys ('a12345')
        driver.find_element_by_xpath (".//*[@id='logindiv']/div/div[2]").click()
        time.sleep (2)
        t=driver.find_element_by_xpath("html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/p").text
        print(t)
        self.assertEqual(t,"总资产")
        # # os.path.basename (文件路径)  # 获取文件名
        # os.path.dirname ("")  # 获取目录
        # driver.get_screenshot_as_file("D:/t金服_测试/report/shotcut/总资产.png")
        pic = ImageGrab.grab()
        pic.save('D:/t金服_测试/report/shotcut/总资产全屏.jpg')
        logger.info(t)
        driver.close()

if __name__ == '__main__':
    unittest.main ()

