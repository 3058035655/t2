#-*- coding:utf-8 -*-
# import win32com.client
# autoit = win32com.client.Dispatch("AutoItX3.Control")
# autoit.Run("NotePad.exe")

import autoit
import unittest
import time
import sys
from actions import Actions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

sys.path.append('D:\\jftest1_CG\\test1')
class Test_Newyyy_pctz_shfk (unittest.TestCase):
    def test_pcLogin(self):
        fp = webdriver.FirefoxProfile(r"C:\Users\mhf\AppData\Roaming\Mozilla\Firefox\Profiles\cv6txwo2.default")
        driver = webdriver.Firefox(fp)
        # driver = webdriver.Firefox ()
        driver.get ("https://www.hongkunjinfu.com")
        WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.ID, 'login')))
        driver.find_element_by_id ('login').send_keys ('14510000051')
        #保存网页弹出框
        driver.find_element_by_id('login').send_keys(Keys.CONTROL+'s')
        time.sleep(2)
        # autoit.run("notepad.exe")
        # autoit.win_wait_active("[CLASS:Notepad]", 3)
        # autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
        # autoit.win_close("[CLASS:Notepad]")
        # autoit.control_click("[Class:#32770]", "Button2")
        # autoit.win_wait
        # autoit.win_wait_active("[CLASS:#32770]",3)
        autoit.win_activate('另存为')
        print("111111")
        autoit.control_focus('另存为','1001')
        print("22222222")
        autoit.win_wait("[Class:#32770]",10)

        autoit.control_set_text('另存为','Edit1','金服网页2')

        # autoit.control_send("[CLASS:#32770]", "Edit1", "hello world{!}")
        # autoit.control_click("[CLASS:#32770]", "Button2")
        autoit.control_click('另存为','Button2')
        driver.close()
if __name__ == '__main__':
    unittest.main ()


