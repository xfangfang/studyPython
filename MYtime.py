# -*- coding: utf-8 -*-

import time

def Get(urls):
    import urllib2
    try:
        web=urllib2.urlopen(urls,timeout=10)
        return web.read()
    except urllib2.URLError,e:
        return e.reason

def reRun(t):
    while(True):
        a = Get("http://115.28.207.130/api/userip")
        filehandler = open('api','w')
        filehandler.write(a+"\n")
        filehandler.close()
        print a
        time.sleep(t)


reRun(1)
