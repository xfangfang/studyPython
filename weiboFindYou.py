# -*- coding: utf-8 -*-
import sys,re
reload(sys)
sys.setdefaultencoding( "utf-8" )


def Get(urls):
    import urllib2
    try:
        web=urllib2.urlopen(urls,timeout=10)
        return web.read()
    except urllib2.URLError,e:
        return e.reason

url = "http://weibo.com/p/1005051975644165/follow?relate=fans&page=1#Pl_Official_HisRelation__64"

print Get(url)
