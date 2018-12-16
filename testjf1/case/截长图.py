import autoit
import time
autoit.run("notepad.exe")
autoit.win_wait_active("[CLASS:Notepad]", 3)
autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
autoit.win_close("[CLASS:Notepad]")
time.sleep(100)
autoit.control_click("[Class:#32770]", "Button2")
time.sleep(100)

#-*- coding:utf-8 -*-
# import win32com.client
# autoit = win32com.client.Dispatch("AutoItX3.Control")
# autoit.Run("NotePad.exe")
# import autoit
# import unittest
# import time
# import sys
# from datetime import datetime
# from actions import Actions
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
#
# sys.path.append('D:\\jftest1_CG\\test1')
# class Test_Newyyy_pctz_shfk (unittest.TestCase):
#     def test_pcLogin(self):
#         fp = webdriver.FirefoxProfile(r"C:\Users\mhf\AppData\Roaming\Mozilla\Firefox\Profiles\cv6txwo2.default")
#         driver = webdriver.Firefox(fp)
#         # driver = webdriver.Firefox ()
#         driver.get ("https://www.csdn.net/")
#         WebDriverWait (driver, 10).until (EC.presence_of_element_located ((By.LINK_TEXT, '博客')))
#         #获取浏览器窗口
#         autoit.win_activate('CSDN-专业IT技术社区 - Mozilla Firefox')
#         print("1111")
#         autoit.send('{LCTRL down}'+'{LSHIFT down}'+'{! down}')
#         # autoit.send('{LCTRL down}' + '{LALT down}' + '{a down}')
#         # driver.find_element_by_id('login').send_keys(Keys.CONTROL + Keys.SHIFT + '!')
#         time.sleep(2)
#         autoit.win_wait('截取的图片另存为...')
#         print("2222")
#         autoit.control_focus('截取的图片另存为...','1001')
#         print("3333")
#         autoit.win_wait("[Class:#32770]",10)
#         t = datetime.now().strftime('%Y%m%d%H%M%S')
#         name='百度首页'+t
#         # autoit.control_set_text('截取的图片另存为...','Edit1','金服网页102')
#         autoit.control_set_text('截取的图片另存为...','Edit1',name)
#         autoit.control_click('截取的图片另存为...','Button2')
#         driver.close()
#
# if __name__ == '__main__':
#     unittest.main ()
#

