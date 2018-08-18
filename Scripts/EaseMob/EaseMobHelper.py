# -*- coding: utf-8 -*-
import datetime
import gzip
import json
import urllib
import urllib2
from time import sleep
from BaseClass import *
import time

class EaseMobHelper:

    def __init__(self,outputfnc,t,s,e,inter):
        self.funcoutput = outputfnc
        self.expire = 0
        #self.target = 1000686
        #self.idstart = 1000671
        #self.idend = 1001193
        self.target = t
        self.idstart = s
        self.idend = e
        self.idcurrent = self.idstart + 0
        self.interval = 1
        self.index = 0
        if inter > 0 and inter < 10001:
            self.interval = inter / 1000
        else:
            self.interval = 1

        self.baseclass = BaseClass()
        self.easemobtoken=''
        self.stop = 0
        self.pause = 0
        self.isdev = 1


    def getToken(self):
        unixnow = time.mktime(datetime.datetime.now().timetuple())
        if self.expire > 0 and self.expire > unixnow:
            return self.easemobtoken
        try:
            opener = urllib2.build_opener()

            #prod
            uri = 'http://a1.easemob.com/oujia/offerplus/token'
            params = {"grant_type": "client_credentials", "client_id": "YXA6CEiYAKoREeatV6k9CXXDKw","client_secret": "YXA6CQFXQxDAOk1DRIv3m7cxYmVwH7U"}
            #dev
            if(self.isdev==1):
                uri = 'http://a1.easemob.com/oujia/offerplusdev/token'
                params = {"grant_type": "client_credentials", "client_id": "YXA6aPduEGH0Eeee3rNDykMcXw","client_secret": "YXA6aWTnlUhR49ttMgVsMHVeotxPUYA"}

            loginHeaders = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.0 Chrome/30.0.1599.101 Safari/537.36',
                'Content-Type': 'application/json'
            }
            httpHandler = urllib2.HTTPHandler(debuglevel=1)
            httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
            opener = urllib2.build_opener(httpHandler, httpsHandler)
            urllib2.install_opener(opener)
            request = urllib2.Request(uri, headers=loginHeaders)
            response = urllib2.urlopen(request, json.dumps(params))
            code = response.getcode()
            if code == 200:
                page = response.read()
                result = json.loads(page)
                self.easemobtoken = result['access_token']
                expin = result['expires_in']
                self.expire = time.mktime(datetime.datetime.now().timetuple()) + expin
                return self.easemobtoken
            else:
                self.funcoutput('getToken failed,response code:' + str(code))

        except urllib2.HTTPError, e:
            self.funcoutput('getToken failed,code:' + str(e.code) + ',message:' + e.msg)
            self.funcoutput(e.code)
            return ''

    #http://api-docs.easemob.com/#/发送消息
#POST /{org_name}/{app_name}/messages

    def sendMSG(self):
        try:
            if self.pause == 1:
                sleep(self.interval)
                return 'paused...'
            self.funcoutput(self.easemobtoken)
            uri = 'http://a1.easemob.com/oujia/offerplus/messages'
            if(self.isdev==1):
                uri = 'http://a1.easemob.com/oujia/offerplusdev/messages'
            self.funcoutput('getHistoryInfo start,url:' + uri)
            # opener = urllib2.build_opener()
            self.token_ = {'Content-Type': 'application/json', 'Authorization': "Bearer %s" % self.easemobtoken}
            loginHeaders = self.token_
            httpHandler = urllib2.HTTPHandler(debuglevel=1)
            httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
            opener = urllib2.build_opener(httpHandler, httpsHandler)
            urllib2.install_opener(opener)
            request = urllib2.Request(uri, headers=loginHeaders)
            nt = datetime.datetime.now()
            #str(nt.microsecond)
            msg = str(self.index)+'从:' + str(self.idcurrent) + "," + nt.strftime("%m%d %H:%M:%S.%f")
            if(self.idcurrent==self.target):
                self.idcurrent+=1


            params = {"target_type": "users","target": [""+ str(self.target) +""],"msg": {"type": "txt","msg": ""+ msg +""},"from": ""+ str(self.idcurrent)  +""}
            self.funcoutput(params)
            response = urllib2.urlopen(request, json.dumps(params))
            code = response.getcode()
            if code == 200:
                self.idcurrent += 1
                if(self.idcurrent>self.idend):
                    self.idcurrent = self.idstart
                page = response.read()
                self.index += 1

                #self.funcoutput(page)
            else:
                self.funcoutput("%s%s%s" % (uri, "无记录,返回码:", str(code)))
        except urllib2.HTTPError, e:
            self.funcoutput('failed,code:' + str(e.code) + ',message:' + e.msg)
            #if (e.code == 429):
            self.funcoutput(e.code)

        return ''

    def mainMethod(self):
        self.funcoutput('begain get token')
        token = self.getToken()
        if len(token) > 0:
            self.funcoutput('get token success,token:' + token)
            while(self.stop==0):
                try:
                    self.sendMSG()
                except Exception, e:
                    self.funcoutput('error:message:' + e.message)
                sleep(self.interval)



