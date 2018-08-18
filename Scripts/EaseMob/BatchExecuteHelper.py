# -*- coding: utf-8 -*-
import datetime
import gzip
import json
import urllib
import urllib2
import requests
from time import sleep
from BaseClass import *
import cookielib
import time
from json import *
import xlrd
import types
from PostFileHelper import *
import threading
import hashlib

class BatchExecuteHelper:

    def __init__(self,outputfnc,url,eparams,path,tnum,wnum,isrecall,inter):
        self.funcoutput = outputfnc
        self.expire = 0
        self.targetUrl = url
        self.essentialParams = eparams
        self.batchPatch = path
        self.interval = 1
        self.baseclass = BaseClass()
        self.stop = 0
        self.pause = 0
        self.isrd = isrecall

        if inter>0 and inter < 10001:
            self.interval = inter / 1000
        else:
            self.interval = 1

        if tnum>0 and tnum<101:
            self.THREAD_NUM = tnum  # 并发线程总数
        else:
            self.THREAD_NUM = 1
        if wnum>0 and wnum<101:
            self.ONE_WORKER_NUM = wnum
        else:
            self.ONE_WORKER_NUM = 1

    def analyseEssentialParams(self,params):
        params = '%s\r\n%s' % (self.essentialParams, params)
        list = params.replace('\r\n','\n').split('\n')
        list = filter(lambda x: len(x) > 0, list)
        result = ""
        for index in range(len(list)):
            str = list[index]
            item = str.split('=')
            if len(item) == 2:
                left = item[0].replace('"','\\"')
                right = item[1].replace('"','\\"')
                if index==len(list) - 1:
                    result = '%s"%s":"%s"' % (result,left,right)
                else:
                    result = '%s"%s":"%s",' % (result,left,right)
        return '%s%s%s' % ('{ ', result, ' }')

    def getFileName(self,filePath):
        filename = ""
        if os.path.exists(filePath):
            filename = os.path.basename(filePath)
        return filename,filePath

    def analyseAndSplitFile(self,dict):
        #﻿image(file)=/Users/liaoyilin/Desktop/timg.jpeg,/Users/liaoyilin/Desktop/timg2.jpeg
        #分析是不是文件文件的key以(file)结尾,内容以,分隔
        paramdic = {}
        filedic = {}
        for k in dict:
            #dict[image(file)] = /Users/liaoyilin/Desktop/timg.jpeg,/Users/liaoyilin/Desktop/timg2.jpeg
            #print "dict[%s] =" % k, dict[k]
            if "(file)" in str(k):
                kname = str(k).replace("(file)","")
                filelist = str(dict[k]).split(",")
                tmplist = []
                for filepath in filelist:
                    filename,filepath = self.getFileName(filepath)
                    #合法文件
                    if len(filename) > 0:
                        fileitem = (kname, (filename, open(filepath,'rb')))
                        tmplist.append(fileitem)
                filedic[k] = tmplist
            else:
                paramdic[k] = dict[k]
        return paramdic,filedic

    def calculateSign(self,datadic):
        #add timestamp
        if(not datadic.has_key("timestamp")):
            stamp = str(long(time.mktime(datetime.datetime.now().timetuple())))
            datadic["timestamp"]='%s%s' %(stamp,'000')

        result=''
        #appType=A&loginName=1000688&packageName=com.oujia.offerplus&password=96e79218965eb72c92a549dd5a330112&source=2&timestamp=1499751682123&version=1.0.0&

        for i, val in enumerate(sorted(datadic.items(), key=lambda d: d[0])):
            if(len(val)==2):
                if(val[0]=='sign'):
                    continue
                result = '%s%s=%s&' % (result, val[0], val[1])

        result = '%s%s' %(result,'99ca919b-4c6e-46d7-b25e-e0cbb9003436')
        sign = hashlib.md5(result.encode('utf-8')).hexdigest()
        datadic["sign"]=sign
        return datadic
    def executeOne(self,params):
        try:
            uri = self.targetUrl
            params = self.analyseEssentialParams(params)
            self.funcoutput(params)
            pdata = JSONDecoder().decode(params)
            datadic,filedic = self.analyseAndSplitFile(pdata)
            #todo...calculate sign
            datadic = self.calculateSign(datadic)
            largelist = []
            if len(filedic) > 0:
                for k in filedic:
                    currentlist = filedic[k]
                    for item in currentlist:
                        largelist.append(item)
            files = tuple(largelist)
            #files = (    ('offerImg', ('1.jpeg', open('/Users/liaoyilin/Desktop/timg.jpeg','rb'))),
            #    ('offerImg', ('2.jpeg', open('/Users/liaoyilin/Desktop/timg1.jpeg','rb'))) )
            response = requests.post(uri, data=datadic, files=files)
            code = response.status_code
            if code == 200:
                page = response.content
                self.funcoutput(page)
                return page
            else:
                self.funcoutput('failed,response code:' + str(code))
        except requests.HTTPError, e:
            self.funcoutput('failed,code:' + str(e.errno) + ',message:' + e.message)
            return ''

    '''
        filestr = '{    "name": "offerImg",    "files": [        {            "filePath": "/Users/liaoyilin/Desktop/timg.jpeg"        },        {            "filePath": "/Users/liaoyilin/Desktop/timg1.jpeg"        }    ]}'
        #filestr = ''
        phelper = PostFileHelper(uri, data, filestr)
        result = phelper.post_multipart()
        self.funcoutput(result)
    except Exception,e:
        self.funcoutput('error:message:' + e.message)
        return ''

        #httpHandler = urllib2.HTTPHandler(debuglevel=1)
        #httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
        #opener = urllib2.build_opener(httpHandler, httpsHandler)
        #urllib2.install_opener(opener)
        #dictionary = JSONDecoder().decode(params)
        #pdata = urllib.urlencode(dictionary)
        #request = urllib2.Request(uri, data=pdata)
        #response = urllib2.urlopen(request)
        #code = response.getcode()

        # https://stackoverflow.com/questions/15746558/how-to-send-a-multipart-related-with-requests-in-python

        #files = None
        #参考这里:http://blog.csdn.net/mgxcool/article/details/51742086
        '''

    def batchMethod(self):
        data = xlrd.open_workbook(self.batchPatch)
        table = data.sheets()[0]  # 通过索引顺序获取
        nrows = table.nrows
        ncols = table.ncols
        nameArray = []
        valueArray = []
        if nrows > 0 and ncols > 0:
            for i in range(nrows):
                if i == 0:
                    pname = ""
                    for j in range(ncols):
                        cell = table.cell(i, j).value
                        if j == ncols - 1:
                            pname = '%s%s' % (pname, cell)
                        else:
                            pname = '%s%s"' % (pname, cell)
                    print pname
                    nameArray = pname.split('"')
                else:
                    pdata = ""
                    for j in range(ncols):
                        cell = table.cell(i, j).value
                        if type(cell) == float:
                            if cell == int(cell):
                                cell = int(cell)
                        if j == ncols - 1:
                            pdata = '%s%s' % (pdata, cell)
                        else:
                            pdata = '%s%s"' % (pdata, cell)
                    print pdata
                    valueArray.append(pdata.split('"'))
        #数据
        for i in range(len(valueArray)):
            data = valueArray[i]
            if type(data) is types.ListType:
                if len(data) == len(nameArray):
                    param = ""
                    for j in range(len(data)):
                        pname = nameArray[j]
                        pval = data[j]
                        if j == len(data) - 1:
                            param = '%s%s=%s' % (param, pname, pval)
                        else:
                            param = '%s%s=%s\r\n' % (param, pname, pval)
                    self.executeOne(param)
                    sleep(self.interval)
                    while (self.pause == 1):
                        sleep(self.interval)
                        if self.stop == 1:
                            return
                    if self.stop == 1:
                        return

    def mainMethod(self):
        try:
            if len(self.batchPatch) > 0:
                self.funcoutput('begain batch execute')
                self.batchMethod()
            else:
                self.executeOne("")
        except Exception, e:
            self.funcoutput('error:message:' + e.message)

    def working(self):
        t = threading.currentThread()
        self.funcoutput( "[" + t.name + "] Sub Thread Begin")

        i = 0
        while i < self.ONE_WORKER_NUM and self.stop == 0:
            i += 1
            self.mainMethod()
            sleep(self.interval)
            self.funcoutput( "[" + t.name + "] Sub Thread End")
        #做完重新再来
        if self.isrd == 1 and self.stop == 0:
            self.working()
            sleep(self.interval)


    def multiThreadMethod(self):
        Threads = []
        # 创建线程
        for i in range(self.THREAD_NUM):
            t = threading.Thread(target=self.working, name="T" + str(i))
            t.setDaemon(True)
            Threads.append(t)

        for t in Threads:
            t.start()

        for t in Threads:
            t.join()