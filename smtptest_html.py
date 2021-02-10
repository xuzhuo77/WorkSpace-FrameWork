import smtplib
from email.mime.text import MIMEText
from email.header import Header
from  smtptest import qingqiu
# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "403863214@qq.com"  # 用户名
mail_pass = "gipbepzrowlabhgj"  # 授权码

sender = '403863214@qq.com'
receivers = ['403863214@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 使用Python发送HTML格式的邮件

mail_msg = qingqiu()

message = MIMEText(mail_msg, 'html', 'utf-8')

message['From'] = Header("菜鸟教程", 'utf-8')  # 括号里的对应发件人邮箱昵称（随便起）、发件人邮箱账号
message['To'] = Header("测试", 'utf-8')  # 括号里的对应收件人邮箱昵称、收件人邮箱账号

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')


smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25)  # 发件人邮箱中的SMTP服务器，端口是25
smtpObj.login(mail_user, mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
print("邮件发送成功")
