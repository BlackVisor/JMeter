# -*- coding: utf-8 -*-
import sys,re
import urllib,urllib2
import codecs
import MySQLdb
from pyquery import PyQuery as pq
import threading
from time import sleep


def dealFlagURL():
    #https: // en.wikipedia.org / wiki / Timeline_of_national_flags
    url = 'https://en.wikipedia.org/wiki/Timeline_of_national_flags'
    #print url
    req = urllib2.Request(url)
    f = urllib2.urlopen(req)
    c = f.read()
    d=pq(c)
    for starring in d("table[class='wikitable']"):
        html = pq(starring).html()
        adoc = pq(starring)
        #print html
        for da in adoc("a.image"):
            a = pq(da)
            href = a.attr("href")
            img = a("img.thumbborder[width='40']")
            if img:
                alt = img.attr("alt")
                alt = alt.replace('Flag of ','').replace('.svg','.png')
                multiThreadMethod(href,alt)


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
    url = 'https:'+imgurl
    print url
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
        'Cookie': 'AspxAutoDetectCookieSupport=1',
    }
    request = urllib2.Request(url, None, header)  # 刻意增加头部header，否则本行与下一行可以写为：response = urllib2.urlopen(imgurl)
    response = urllib2.urlopen(request)
    path = "/Users/liaoyilin/Desktop/tmp/flag/"+name
    #print path
    f = open(path, 'wb')
    f.write(response.read())
    f.close()

dealFlagURL()


