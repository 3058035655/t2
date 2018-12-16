#coding=utf8
'''
random.randint(a, b):用于生成一个指定范围内的整数。
其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
random.choice(sequence)：从序列中获取一个随机元素
参数sequence表示一个有序类型（列表，元组，字符串）
'''
import csv
import json
import time
import threading
from random import randint,choice
#创建请求函数
import requests
from urllib3.connection import HTTPConnection

from testjf1.common.db import Db
from utils.config import DATA_PATH

excel = DATA_PATH + '/test.csv'
with open(excel, "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
    for col in reader:
        # print(col)
        db = Db ()
        connection = db.connection
        cursor = db.cursor
        # cursor.execute ("SELECT message_note from sys_tel_message where tel='13301302026'")
        cursor.execute ("SELECT code from bidd_info where title='m季季81602'")
        connection.commit ()
        t = cursor.fetchall ()
        # a=t['tel']
        code = t[0]['code']
        # print ('标的code:', code)
        tel=col

def postRequest(threadNum):

  #定义需要进行发送的数据

    #接口
  # requrl ="http://192.168.1.249:9901/hkjf/login.do?method=indexlogin"
  requrl = "http://192.168.1.249:9901/hkjf/login.do?method=indexlogin"
  #请求服务,例如：www.baidu.com
  hostServer="192.168.1.249"
  #连接服务器
  conn = HTTPConnection(hostServer)
  #发送请求
  # conn.request(method="POST",url=requrl,body=postData)
  content = {'login': tel,
             'password': '2971055a690ad019e9fc08a9971080ccfd6a8b588c69acc28383a12d9cfdcb135a60550a4df643b9967c5fab90ce4eb8e3970c2c093fefe299662ac44e868763d281e8708ab625528d55c6a777b2700bcb9daf7e7e0c6805ffd13760d4ac0120d6f43c2dc05fc38fcff485eedd8859d79200ddb7a9a606b8548fa1d8def1dacc',
             'pwdLevel': '2', 'verify_code': '请输入计算结果', 'randCode': '请输入您的6位验证码',
             'commendPhone': '请输入推荐码(推荐人手机号后8位)',
             'loginregister': '请输入您的手机号', 'passwordresgister': '', 'token': '', 'modulus': '',
             'exponent': '', 'newToken': '', 'phoneId': '', 'code': '',
             'utype': '', 'csrftoken': '', 'pwdLevel': ''
             }
  response= requests.post ('http://192.168.1.249:9901/hkjf/login.do?method=indexlogin',data=content)
  #获取请求响应

  #打印请求状态
  if response.status_code in range(200,300):
    print (u"线程"+str(threadNum)+u"状态码："+str(response.status_code))
  conn.close()
def run(threadNum,internTime,duration):
  #创建数组存放线程
  threads=[]
  try:
    #创建线程
    for i in range(1,threadNum):
      #针对函数创建线程
      t=threading.Thread(target=postRequest,args=(i,))
      #把创建的线程加入线程组
      threads.append(t)
  except Exception as e:
      print (e)
  try:
    #启动线程
    for thread in threads:
        thread.setDaemon(True)
        thread.start()
        time.sleep(internTime)
    #等待所有线程结束
    for thread in threads:
        thread.join(duration)
  except Exception as e:
      print (e)
if __name__ == '__main__':
  # startime=time.strftime("%Y%m%d%H%M%S")
  startime='20180904094854'
  now=time.strftime("%Y%m%d%H%M%S")
  duratiion=input(u"输入持续运行时间:")
  while (startime+str(duratiion))!=now:
    run(10,1,int(duratiion))
    now=time.strftime("%Y%m%d%H%M%S")
