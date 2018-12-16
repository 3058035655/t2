import unittest
# from test.case.test_baidu6 import TestBaiDu
# from test.case.test_pclogin import TestLogin
# from test.case.test_xjniannianying import TestNewniannianying
# from test.case.test_xjxsbOK import TestNewxsb
# from test.case.test_xjsanbiao import TestNewsanbiao
# from test.case.test_xjsb_tiqian_day import TestNewsanbiaoday
# from test.case.test_xjsb_tiqian_month import TestNewsanbiaomonth
# from test.case.test_xjtyb import TestNewtyb
# from test.case.test_xjyyy_ycx import TestNewyyyycx
# from test.case.test_xjjjy_ycx import TestNewjjyycx
# from test.case.test_xjnny_ycx import TestNewnnyycx
# from test.case.test_tzyyy1 import TestTouziyyy1
# from test.case.test_tzjjy import TestTouzijjy
# from test.case.test_tznny import TestTouzinny
# from test.case.test_pp_y1_s1 import TestPPy1s1
# from test.case.test_pp_y2_s1 import TestPPy2s1
# from test.case.test_pp_y1_sn import TestPPy1sn
# from testjf1.case.register_bk_tixian_shfkok import Test_tx_shfk
# from testjf1.case.register_smyh_ok import Test_smyh
# from testjf1.case.test_login_newyyy33_pcinvest_shfk_ok import Test_Newyyy_pctz_shfk
# from testjf1.case.test_login_newyyyok import Test_Newyyy
# from testjf1.case.test_login_pf2_pclqredpackageok import Test_Pf_pclqredpackage
# from testjf1.case.test_login_tjwhite_nameok import Test_Tjwhitename
from testjf1.case.test_pc_loginok2 import Test_Pclogin2

from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH

if __name__=='__main__':
    suite=unittest.TestSuite()
    # 直接用addTest方法添加单个TestCase  test_pcLogin
    suite.addTest(Test_Pclogin2("test_pcLogin2"))
    # suite.addTest (TestBaiDu ("test_search"))
    # suite.addTest(TestLogin("login"))
    # suite.addTest(TestNewbkb("test_newbkb"))
    # suite.addTest(TestNewtjb("test_newtjb"))
    # suite.addTest (TestNewyyy ("test_newyyy"))  #新建月月盈
    # suite.addTest(TestNewjjy("test_newjjy"))
    # suite.addTest(TestNewniannianying("test_newniannianying"))
    # suite.addTest(TestNewxsb("test_newxsb"))
    # suite.addTest(TestNewsanbiao("test_newsanbiao"))   #新建散标
    # suite.addTest(TestNewsanbiaoday("test_newsanbiaoday"))
    # suite.addTest(TestNewsanbiaomonth("test_newsanbiaomonth"))
    # suite.addTest(TestNewtyb("test_newtyb"))
    # suite.addTest(Test_smyh("test_Login"))      #pc注册并且实名
    # suite.addTest(Test_Tjwhitename("test_Login")) #添加 投资白名单
    # suite.addTest(Test_Pf_pclqredpackage("test_Login"))  #发红包并pc领取
    # suite.addTest(Test_tx_shfk("test_Login"))

    # suite.addTest(Test_Newyyy("test_Login"))    #新建月月赢
    # suite.addTest(Test_Newyyy_pctz_shfk("test_Login"))  #建标-投资-放款
    # suite.addTest(TestNewyyyycx("test_newtyyy_ycx"))
    # suite.addTest(TestNewjjyycx("test_newjjy_ycx"))
    # suite.addTest(TestNewnnyycx("test_newtnny_ycx"))
    # suite.addTest(TestTouziyyy1("test_touziyyy"))
    # suite.addTest(TestTouzijjy("test_touzijjy"))
    # suite.addTest(TestTouzinny("test_touzinny"))
    # suite.addTest(TestPPy1s1("test_ppy1s1"))
    # suite.addTest(TestPPy2s1("test_ppy2s1"))
    # suite.addTest(TestPPy1sn("test_ppy1sn"))


    # runner = unittest.TextTestRunner (verbosity=2)
    # runner.run (suite)

    if __name__ == '__main__':
        report = REPORT_PATH + '\\report.html'
        print (report)
        with open (report, 'wb') as f:
            runner = HTMLTestRunner (f, verbosity=2, title='hkjf测试报告', description='修改html报告')
            runner.run (suite)
            e = Email (title='hkjf测试报告',
                       message='这是今天的测试报告，请查收！',
                       receiver='hongfeimou@hongkunjinfu.com',
                       # server='smtp.qq.com:465',
                       server='smtp.mxhichina.com:465',
                       sender='hongfeimou@hongkunjinfu.com',
                       password='.hongfei123',
                       path=report
                       )
            e.send ()

