# -*- coding: utf-8 -*-
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import sys

class BaseClass:
    def cur_file_dir(self):
        return self.cur_file_dir("historydata")

    def cur_file_dir(self,subdir):
        dir = self.base_dir() + "/" + subdir
        if not os.path.exists(dir):
            os.makedirs(dir)
        return dir


    def base_dir(self):
        path = sys.path[0]
        if os.path.isdir(path):
            return path
        elif os.path.isfile(path):
            return os.path.dirname(path)

    def replaceQuote(self,val):
        val = str(val)
        return val.replace("'","''")

    def convert_str(self,val):
        if isinstance(val, unicode):
            val = val.encode("utf-8")
        else:
            val = str(val)
        return val

    def send_mail(self, sub, content):
        self.send_mail_to(sub,content,["eliaozi@163.com"])

    def send_mail_to(self, sub, content,tolist):
        reload(sys)
        sys.setdefaultencoding('utf-8')

        mailto_list = tolist
        if len(mailto_list) == 0:
            return False
        mail_host = "smtp.exmail.qq.com"  # 设置服务器
        mail_user = "service@shangji.trade"  # 用户名
        mail_pass = "Ab123456"  # 口令
        mail_postfix = "shangji.trade"  # 发件箱的后缀
        try:
            s = smtplib.SMTP()
            s.connect(mail_host)
            s.login(mail_user, mail_pass)
            msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % (mail_user, mailto_list[0], sub, content))
            s.sendmail(mail_user, mailto_list, msg)
            s.close()
            return True
        except Exception, e:
            print str(e)
            return False
