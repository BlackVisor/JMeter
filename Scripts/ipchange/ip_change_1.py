#!/usr/bin/python
#coding=utf-8
"""
chenwenkun
"""
import os
import smtplib
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email.Header import Header
import sys
import time
import os
#sender = 'cwk7524@163.com'
sender = '272624898@qq.com'
#receiver = raw_input('请输入要接受到的QQ邮箱：')
receiver = '1154500712@qq.com'
# receiver = '7152418@qq.com'
smtpserver = 'smtp.qq.com'
#username = 'cwk7524@163.com'
username = '272624898@qq.com'
password = 'zxnvissiogwcbibh'
tit = time.strftime('%Y/%m/%d %H:%S',time.localtime())
tit = str(tit)
internetIP = os.popen("curl ident.me").read()
print (internetIP)
#internetIP = str(internetIP)
#print internetIP
subject = 'IP changed to %s' %(internetIP)
#邮件标题


filename = 'ip_old.txt'

if not os.path.exists(filename):
	os.system(r"touch {}".format(filename))
f2 = open('ip_old.txt','r')
ip_old = f2.readline()
#print (ip_old)
f2.close()

if ip_old == internetIP:
	print ("IP not changed")
else:
	print ("IP changed!")
	internetIP = str(internetIP)
	#message = "ip changed!"+ "time" + tit ,"Now ip is"+ internetIP
	#print message
	msg = MIMEText('change %s time %s'%(internetIP,tit))
	msg['From'] = sender
	msg['To'] =  receiver 
	msg['Subject'] = Header(subject+ '@'+tit,'utf-8')
	#smtp = smtplib.SMTP()

	f3 = open('ip_old.txt','w')
	f3.write(str(internetIP))
	f3.close()
	smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
	#smtp.connect('smtp.qq.com')
	smtp.login(username,password)
	smtp.sendmail(sender,receiver,msg.as_string())
	print ("send succeed")
	smtp.quit()
	print ("-----------------------------")
