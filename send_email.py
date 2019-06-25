# coding=UTF-8
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
	#请自行修改下面的发送者和接受者
	sender = 'jasonzhang9309@163.com'
	receivers = ['466263371@qq.com','2218517002@qq.com']
	message = MIMEText('用python发送邮件联系。','plain','utf-8')
	message['From'] = Header('张继舒','utf-8')
	message['To'] = Header('张继舒','utf-8')
	message['Subject'] = Header('示例代码邮件','utf-8')
	print(message.as_string())
	"""
	smtper = SMTP('smtp.163.com')
	smtper.login(sender,'zjs.6743935')
	smtper.sendmail(sender,receivers,massage.as_string())
	print('邮件发送完成')
	"""
if __name__ == '__main__':
	main()
