# -*- coding: utf-8 -*
import sys,re
reload(sys)
sys.setdefaultencoding( "utf-8" )

import urllib2

def get(u):
    r = urllib2.urlopen(u)
    return r.read()

print get("http://www.baidu.com")
