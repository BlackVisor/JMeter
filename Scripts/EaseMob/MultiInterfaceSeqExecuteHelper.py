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
import xlwt
from xlutils.copy import copy
import types
from PostFileHelper import *
import threading
import hashlib

class MultiInterfaceSeqExecuteHelper:

    def __init__(self,outputfnc,url,eparams,path,inter):
        self.funcoutput = outputfnc
        self.expire = 0
        self.targetUrl = url
        self.essentialParams = eparams
        self.batchPatch = path
        self.interval = 1
        self.baseclass = BaseClass()
        self.stop = 0
        self.pause = 0

        if inter>0 and inter < 10001:
            self.interval = inter / 1000
        else:
            self.interval = 1

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

    def executeOne(self,table,row,dataNameArr,method,params,output,output_mapping):
        try:
            if self.targetUrl.endswith('/'):
                self.targetUrl = self.targetUrl[:(len(self.targetUrl)-1)]
            uri = '%s/%s' %(self.targetUrl,method)
            self.funcoutput(uri)
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
                s = json.loads(page)
                if s.has_key('status') and s.has_key('msg'):
                    for i in range(len(output_mapping)):
                        p = output_mapping[i]
                        propname = output[i]
                        propArr = propname.split('.')
                        datacol = dataNameArr.index(p)
                        if datacol > -1:
                            #analyse json and write data to target
                            val = self.calculateJsonVale(s,propArr,0)
                            self.writeSheet2StringDatas(table,row,datacol,val)
                return page
            else:
                self.funcoutput('failed,response code:' + str(code))
        except requests.HTTPError, e:
            self.funcoutput('failed,code:' + str(e.errno) + ',message:' + e.message)
            return ''

    def calculateJsonVale(self,s,propArr,index):
        if index < len(propArr):
            #data.tokenId,data.userName,data.list[0].offerTagId
            prop = propArr[index]
            left = prop.find('[')
            right = prop.find(']')
            if left > -1 and right > -1:
                propname = prop[:left]
                s = s[propname]
                i = int(prop[left+1:left+2])
                if type(s) is types.ListType and i < len(s):
                    s = s[i]
                    index += 1
                    if index == len(propArr):
                        return s
                    else:
                        return self.calculateJsonVale(s, propArr, index)
            elif s.has_key(prop):
                s = s[prop]
                index += 1
                if index == len(propArr):
                    return s
                else:
                    return self.calculateJsonVale(s, propArr, index)
        return ''
    def analyseRules(self,table):
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
        if len(nameArray) == 5:
            return nameArray,valueArray

    def analyseSheet2Names(self, table):
        nrows = table.nrows
        ncols = table.ncols
        nameArray = []
        if nrows > 0 and ncols > 0:
            if range(nrows) > 0:
                pname = ""
                for j in range(ncols):
                    cell = table.cell(0, j).value
                    if j == ncols - 1:
                        pname = '%s%s' % (pname, cell)
                    else:
                        pname = '%s%s"' % (pname, cell)
                print pname
                nameArray = pname.split('"')
        return nameArray


    def writeSheet2StringDatas(self, table, i, j, val):
        # 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
        # xf = 0  # 扩展的格式化
        # table.put_cell(row, col, ctype, value, xf)
        nrows = table.nrows
        ncols = table.ncols
        valueArray = []
        if nrows > 0 and ncols > 0:
            if i < range(nrows) and i > 0 and j > -1 and j < range(ncols):
                ws,wb = self.getWritableSheet(1)
                ws.write(i,j,val)
                wb.save(self.batchPatch)



    def analyseSheet2Datas(self, table,i):
        nrows = table.nrows
        ncols = table.ncols
        valueArray = []
        if nrows > 0 and ncols > 0:
            if i < range(nrows) and i > 0:
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
        return valueArray

    #按照sheet1定义的输入,输出参数,执行顺序依次执行所有方法算是一个方法组
    def calcParamsThenexecute(self,dataNameArr,row,method,params,param_mapping,output,output_mapping):
        datatable = self.getReadonlySheet(1)
        param = ""
        for i in range(len(param_mapping)):
            p = param_mapping[i]
            datacol = dataNameArr.index(p)
            if datacol > -1:
                cell = datatable.cell(row,datacol).value
                if type(cell) == float:
                    if cell == int(cell):
                        cell = int(cell)
                param = '%s%s=%s\r\n' % (param, params[i],cell )

        self.executeOne(datatable,row,dataNameArr,method,param,output,output_mapping)
        sleep(self.interval)


    def getReadonlySheet(self,index):
        data = xlrd.open_workbook(filename=self.batchPatch)
        table = data.sheets()[index]  # 规则sheet
        return table

    def getWritableSheet(self,index):
        rb = xlrd.open_workbook(filename=self.batchPatch, encoding_override='utf-8')
        # 通过sheet_by_index()获取的sheet没有write()方法
        #rs = rb.sheet_by_index(0)
        wb = copy(rb)
        # 通过get_sheet()获取的sheet有write()方法
        ws = wb.get_sheet(index)
        #ws.write(0, 0, 'changed!')
        #wb.save('m:\\1.xls')
        return ws,wb

    def batchMethod(self):
        ruletable = self.getReadonlySheet(0) #规则sheet
        nArr,ruleArr = self.analyseRules(ruletable)

        datatable = self.getReadonlySheet(1)
        dataNameArr = self.analyseSheet2Names(datatable)
        #每条数据,需要跑一组方法
        for j in range(datatable.nrows):
            if j == 0:
                continue
            # 按照sheet1定义的输入,输出参数,执行顺序依次执行所有方法算是一个方法组
            for i in range(len(ruleArr)):
                rdata = ruleArr[i]
                if type(rdata) is types.ListType:
                    if len(rdata) == 5:
                        method = rdata[0]
                        params = rdata[1].split(',')
                        param_mapping = rdata[2].split(',')
                        output = rdata[3].split(',')
                        output_mapping = rdata[4].split(',')
                        if len(params) != len(param_mapping) or len(output) != len(output_mapping):
                            continue
                        self.calcParamsThenexecute(dataNameArr,j,method,params,param_mapping,output,output_mapping)
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
                self.funcoutput('needs batch params.')
        except Exception, e:
            self.funcoutput('error:message:' + e.message)

    def working(self):
        t = threading.currentThread()
        self.funcoutput( "[" + t.name + "] Sub Thread Begin")

        i = 0
        while i < 1 and self.stop == 0:
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
        for i in range(1):
            t = threading.Thread(target=self.working, name="T" + str(i))
            t.setDaemon(True)
            Threads.append(t)

        for t in Threads:
            t.start()

        for t in Threads:
            t.join()