#/usr/bin/env python
#coding=utf8

import httplib
import md5
import urllib
import random
import json

appid = '20170813000072135'
secretKey = 's9AMqsxgupwtFyhgCO0f'

def singleTranslate(prs,q,fromLang,toLang):
    s = ''
    # dataarr不翻译
    ia = prs.find('DataArr')
    ib = q.find('%')

    if ia > -1 or ib > -1:
        s = prs + '="' + q + '";'
        print s
    else:
        httpClient = None
        myurl = '/api/trans/vip/translate'
        #q = 'apple'
        #fromLang = 'en'
        #toLang = 'zh'
        salt = random.randint(32768, 65536)

        sign = appid+q+str(salt)+secretKey
        m1 = md5.new()
        m1.update(sign)
        sign = m1.hexdigest()
        myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

        try:
            httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            #response是HTTPResponse对象
            response = httpClient.getresponse()
            result = response.read()
            data = json.loads(result)
            src = data['trans_result'][0]['src'];
            dst = data['trans_result'][0]['dst'];
            #print dst
            s = prs + '="' + dst + '";'
            print s
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()
if __name__ == "__main__":
    list = []
    file = open("/Users/liaoyilin/Desktop/RULES")
    for line in file:
        list.append(line)
    for s in list:

        #print(str)
        if len(s) == 0:
            continue
        lPos = s.find('="')
        if lPos > -1:
            ns = s[lPos+2:len(s)-3]
            prs = s[:lPos]
            #print(nstr)
            # jp日语 kor韩语
            singleTranslate(prs,ns,'zh','kor')
