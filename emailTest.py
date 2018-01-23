from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart,MIMEBase
import smtplib
from email.header import Header

# 发送Email地址和口令:
from_addr = 'xxxxxx@163.com'
password = 'xxxxxx'

# 输入收件人信息:
to_addr = 'xxxxxx@qq.com'
# 输入SMTP服务器地址:
smtp_server = 'smtp.163.com'

# 发送的附件
# send_file = open('D:\\2zyyyyy\\__MACOSX\\PythonProject\\automationTestReport\\report\\log.txt', 'rb').read()
#
# att = MIMEText(send_file, 'base64', 'utf-8')
# att['Content-Type'] = 'application/octet-stream'
# att['Content-Disposition'] = 'attachment; filename= "report.html"'
#
# msg = MIMENonMultipart('related')
# msg['Subject'] = Header('放假通知', 'utf-8')
# msg['From'] = 'android4google@163.com'
# msg['To'] = "309739685@qq.com"
# msg.attach(send_file)
#
# server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
# server.set_debuglevel(1)  # 打印出和SMTP服务器交互的所有信息
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()
# print('success')
# 邮件主题
# subject = 'Python发送附件邮件'
#
# # 发送的附件
# send_file = open('D:\\2zyyyyy\\__MACOSX\PythonProject\\automationTestReport\\report\\2018-01-22 17_02_46result.html'
#                  , 'rb').read()
# att = MIMEText(send_file, 'base64', 'utf-8')
# att['Content-Type'] = "application/octet-stream"
# att['Content-Disposition'] = "attachment; filename='report.html'"
#
# msgRoot = MIMEMultipart('related')
# msgRoot['Subject'] = subject
# msgRoot.attach(att)
#
# smtp = smtplib.SMTP()
# smtp.connect(smtp_server)
# smtp.login(from_addr, password)
# smtp.sendmail(from_addr, to_addr, msgRoot.as_string())
# smtp.quit()

# 邮件对象:
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('C:\\Users\\admin\\Desktop\\image\\Q1.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    print('success')
    server.quit()
