#-*- coding:utf-8 -*-
import unittest
import time
import sys

import re
import requests
from testjf1.common.db import Db
from testjf1.common.loginpage import LoginPage
from testjf1.interface.Dog import Dog
from testjf1.interface.test_多人投资ok import Test_duoren_invest
from utils.config import DATA_PATH, REPORT_PATH
from utils.file_reader import ExcelReader
sys.path.append('D:\\jftest1_CG\\test1')
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


n=3
d=Dog()
while n>0:
    print("你好")
    # # inverst = Test_duoren_invest()
    # inverst.test_Login()
    d.say()
    n=n-1


