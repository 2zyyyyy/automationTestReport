from email.mime.text import MIMEText
import smtplib
from email.header import Header

msg = MIMEText('真的不知道是什么原因', 'plain', 'utf-8')
msg['Subject'] = Header('放假通知', 'utf-8')
msg['From'] = 'android4google@163.com'
msg['To'] = "309739685@qq.com"
# 输入Email地址和口令:
from_addr = 'android4google@163.com'
password = 'zhangyun0714'

# 输入收件人信息:
to_addr = '309739685@qq.com'
# 输入SMTP服务器地址:
smtp_server = 'smtp.163.com'

server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)  # 打印出和SMTP服务器交互的所有信息
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
print('success')
