# -*- coding: utf-8 -*-
import sys,re
import urllib,urllib2
import codecs
import MySQLdb
from pyquery import PyQuery as pq
import threading
from time import sleep
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

def dealFlagURL():
    #https: // en.wikipedia.org / wiki / Timeline_of_national_flags
    url = 'https://www.xe.com/currency'
    #print url
    req = urllib2.Request(url)
    f = urllib2.urlopen(req)
    c = f.read()
    d=pq(c)
    print sys.argv[0]
    print(d)
    # for starring in d("table[class='wikitable']"):
    #     html = pq(starring).html()
    #     adoc = pq(starring)
    #     #print html
    #     for da in adoc("a.image"):
    #         a = pq(da)
    #         href = a.attr("href")
    #         img = a("img.thumbborder[width='40']")
    #         if img:
    #             alt = img.attr("alt")
    #             alt = alt.replace('Flag of ','').replace('.svg','.png')
    #             multiThreadMethod(href,alt)


def working(imgurl,name):
    t = threading.currentThread()
    print ("[" + t.name + "] Sub Thread Begin")
    sleep(1)
    analySVG(imgurl,name)
    print ("[" + t.name + "] Sub Thread End")

Threads = []
TIndex = 0
def multiThreadMethod(imgurl,name):
    # 创建线程
    global TIndex
    TIndex = TIndex + 1
    t = threading.Thread(target=working, name="T" + str(TIndex),args=(imgurl,name,))
    t.setDaemon(True)
    Threads.append(t)
    t.start()
    t.join()

def analySVG(imgurl,name):
    #mw-mmv-final-image svg
    url = 'https://en.wikipedia.org'+imgurl
    #print url
    req = urllib2.Request(url)
    f = urllib2.urlopen(req)
    c = f.read()
    d = pq(c)
    for starring in d("div[class='fullImageLink']"):
        img = pq(starring)('img')
        src = img.attr("src")
        downImage(src,name)


def downImage(imgurl,name):
    fpath = os.getcwd() + "/flag/" + name
    if (os.path.exists(fpath)):
        return

    url = ''+imgurl
    print(url,name)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
        'Cookie': 'AspxAutoDetectCookieSupport=1',
    }
    try:
        request = urllib2.Request(url, None, header)  # 刻意增加头部header，否则本行与下一行可以写为：response = urllib2.urlopen(imgurl)
        response = urllib2.urlopen(request)
        # print path
        f = open(fpath, 'wb')
        f.write(response.read())
        f.close()
    except urllib2.HTTPError, e:
        print e.fp.read()


def analyseHtml():
    path = os.getcwd() + "/currency.html"
    f = open(path)
    d = pq(f.read())
    # print d
    all = []
    for strli in d("li[class='currencyListItem']"):
        ahtml = pq(strli).html()
        # print ahtml
        hrefImg = pq(ahtml)("img").attr("src")
        spanName = pq(ahtml)("span").html()
        # print spanName
        all.append(spanName)
        # print hrefImg
        index = hrefImg.rfind("/")
        filename = hrefImg[index+1:]
        print filename
        # downImage(hrefImg,filename)
        # break;
    all.sort()
    for astr in all:
        print astr

def isMatch():
    all1 = ["FJD","MXN","STD","LVL","SCR","CDF","BBD","GTQ","CLP","HNL","UGX","ZAR","TND","CUC","BSD","SLL","SDG","IQD","CUP","GMD","TWD","RSD","DOP","KMF","MYR","FKP","XOF","GEL","BTC","UYU","MAD","CVE","TOP","AZN","OMR","PGK","KES","SEK","BTN","UAH","GNF","ERN","MZN","SVC","ARS","QAR","IRR","MRO","CNY","THB","UZS","XPF","BDT","LYD","BMD","KWD","PHP","RUB","PYG","ISK","JMD","COP","MKD","USD","DZD","PAB","GGP","SGD","ETB","JEP","KGS","SOS","VEF","VUV","LAK","BND","ZMK","XAF","LRD","XAG","CHF","HRK","ALL","DJF","ZMW","TZS","VND","XAU","AUD","ILS","GHS","GYD","KPW","BOB","KHR","MDL","IDR","KYD","AMD","BWP","SHP","TRY","LBP","TJS","JOD","AED","HKD","RWF","EUR","LSL","DKK","CAD","BGN","MMK","MUR","NOK","SYP","IMP","ZWL","GIP","RON","LKR","NGN","CRC","CZK","PKR","XCD","ANG","HTG","BHD","KZT","SRD","SZL","LTL","SAR","TTD","YER","MVR","AFN","INR","AWG","KRW","NPR","JPY","MNT","AOA","PLN","GBP","SBD","BYN","HUF","BYR","BIF","MWK","MGA","XDR","BZD","BAM","EGP","MOP","NAD","NIO","PEN","NZD","WST","TMT","CLF","BRL"]
    all2 = ["AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTN","BWP","BYN","BZD","CAD","CDF","CHF","CLP","CNY","COP","CRC","CUC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","EUR","FJD","FKP","GBP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF","IDR","ILS","IMP","INR","IQD","IRR","ISK","JEP","JMD","JOD","JPY","KES","KGS","KHR","KMF","KPW","KRW","KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRO","MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLL","SOS","SPL","SRD","STD","SVC","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD","TVD","TWD","TZS","UAH","UGX","USD","UYU","UZS","VEF","VND","VUV","WST","XAF","XAG","XAU","XCD","XDR","XOF","XPD","XPF","XPT","YER","ZAR","ZMW","ZWD"]
    for a2 in all2:
        isfind=0
        for a1 in all1:
            if a2==a1:
                isfind = 1
                break;
        if(isfind==0):
            print a2

isMatch()
# analyseHtml()


