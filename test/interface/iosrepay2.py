import threading
import unittest
from datetime import time

import pymysql


import requests
import json

class TestInvest(unittest.TestCase):



   def test_loginios(self):
        l = ['13301307172', '13301128639']
        for i in l:
            tel=i
            content = {'access_token': '7f21f9a9-ea81-47bf-8b0c-368addb11a47', 'appVersion': '2.6.0', 'login': tel, 'mobileIp': '0.0.0.0',
                       'mobileMAC': '4a:00:00:97:47:b1', 'mobileModel': '0', 'iPad Air 2': '123', 'mobileUDID': '44AB0480-96FC-4AEA-9737-EB7A05FDDF7F',
                       'mobileVersion': 'iOS 11.0.3', 'passwd': 'nuxgK1A=','randomCode': '123', 'passLength': '6', 'password':
                           'ptKAkEOVQwm62ghGYgyay/Y56eOIdeNIjx3ztZe8Wh9e8GRqdK0r9dAUXfYqbEaqXgJww17cM8Q2eZdZOhIOb6+2lMT6gYl9JhADOJmiHg5VnBWPLOPkLjlptw5EYzJKNIi93P6ENJhujs5xLGcMuMd8vySBqeQtMRPQURKGI3c='   }

            r = requests.post ('http://192.168.1.249:9922/hkjfapp/user/doLogin',data=content)  # 发送请求

            print (r.text)  # 获取响应报文
            print (r.status_code)
            print ("123")
            c = r.cookies
            print(c)
            for key, value in c.items ():
                print (key, '==', value)
            s=c.values()
            print(s)
            # 查询还款code，去usercode
            connection = pymysql.connect(host='192.168.1.249', port=3307, user='dev_db_user', password='yrSuper001',
                                         db='finance_qa',
                                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            cursor = connection.cursor()
            # cursor.execute ("SELECT message_note from sys_tel_message where tel='13301302026'")
            # cursor.execute ("SELECT code FROM bidd_info where title=%s", (cell_value,))
            # cursor.execute("SELECT id from bid_info where name='m散标按日52905'")
            cursor.execute("SELECT code FROM loginuser where tel=%s", (tel))
            # 提交SQL
            connection.commit()
            t = cursor.fetchall()
            # a=t['tel']
            usercode= t[0]['code']
            cursor.execute("SELECT code FROM loan_repay_plan where borrows_code=%s", (usercode))
            # 提交SQL
            connection.commit()
            t = cursor.fetchall()
            # a=t['tel']
            loancode = t[0]['code']
            # 还款
            content1 = {'access_token': '7f21f9a9-ea81-47bf-8b0c-368addb11a47','passLength': '6', 'payPass': 'rP4i6bpuaRkHGyrtNTnvisblfUyI0HpIyMrJ//NuF3RPDtpYZj6NpVgibLLJMCWxdhwuaWdbdar4seC5OaEXUamze0vVtGRzrVksQPLYcnVVp3w4m9/60X8rckFDRzO2qSpQMf/vhMNN1Hsvy/9Cwt1TDkrcOM4K6zfNavWXJBI=',
                        'repayCode': loancode, 'sessionId': s,'userCode': usercode}

            r1 = requests.post ('http://192.168.1.249:9922/hkjfapp/loanBid/repay', data=content1,cookies=c)  # 发送请求

            # return r.json
            print (r1.text)  # 获取响应报文
            print (r1.status_code)
            print ("还款结果")

   list = ['13301307172', '13301128639',]
   threads = []
   files = range (len (list))
   # 创建线程   :

   for i in files:
    t = threading.Thread (target=test_loginios, args=(list[i],))
    threads.append (t)

   if __name__ == '__main__':
    # 启动线程
    for i in files:
        threads[i].start ()
   for i in files:
    threads[i].join ()
    print('end:%s' % time.ctime ())


