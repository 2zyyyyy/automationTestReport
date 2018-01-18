import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
import time
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import os

# 加载测试文件
# import test_case.test_baidu
# import test_case.test_crm

'''
    discover(start_dir, pattern='test*.py', top_level_dir=None)
'''


# ===========定义发送邮件===========
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg['From'] = 'android4google@163.com'
    msg['To'] = "309739685@qq.com"

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('android4google@163.com', 'zhangyun0714')
    smtp.sendmail('android4google@163.com', '309739685@qq.com', msg.as_string())
    smtp.quit()
    print('email has send out!')


# =====查找测试报告目录，找到最新生成的测试报告文件=====
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(discover)
    # testunit = unittest.TestSuite()

    #  定义测试用例的目录
    test_dir = 'D:\\2zyyyyy\\__MACOSX\\PythonProject\\automationTestReport\\test_case'
    test_Report = 'D:\\2zyyyyy\\__MACOSX\\PythonProject\\automationTestReport\\report'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    # 按照一定格式获取当前时间
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    # 定义报告存放路径
    fileName = test_Report + '\\' + now + 'result.html'
    fp = open(fileName, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况: ')
    runner.run(discover)  # 运行测试用例
    fp.close()  # 关闭报告文件

    new_report = new_report(test_Report)
    send_mail(new_report)  # 发送测试报告
# 终端在当前目录执行 python runTest.py >> report/log.txt 2>&1
