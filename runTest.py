import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
import time
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import os
from email.mime.multipart import MIMEMultipart

# 加载测试文件
# import test_case.test_baidu
# import test_case.test_crm

'''
    discover(start_dir, pattern='test*.py', top_level_dir=None)
'''


# ===========定义发送邮件===========
def send_mail(file_new):
    from_addr = 'xxxxxx@163.com'
    from_pass = 'xxxxxx'
    to_addr = 'xxxxxx@qq.com'
    smtp_server = 'smtp.163.com'

    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()


    # 发送的附件
    # send_file = open(file_new, 'rb').read()
    att = MIMEText(mail_body, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename= "report.html"'

    # msg = MIMEText('自动化测试报告，详情查看附件')
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = Header('自动化测试报告', 'utf-8')
    msgRoot['From'] = from_addr
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtp_server)
    smtp.login(from_addr, from_pass)
    smtp.sendmail(from_addr, to_addr, msgRoot.as_string())
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
