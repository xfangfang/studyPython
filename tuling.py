# -*- coding: utf-8 -*
import sys,json,urllib2,re
reload(sys)
sys.setdefaultencoding( "utf-8" )

import json
def Post(urls,data):
    import urllib2,json,urllib
    request = urllib2.Request(urls,urllib.urlencode(data))
    res=urllib2.urlopen(request,timeout=10)
    if res.getcode()!=200:
        return 'There is something Wrong'
    return res.read()

while(True):
    a = raw_input("你:")
    # a = "hi"
    p = {"key": "c50ffa4b516b6b79153b3b0c864991ea", "info": a}
    a = Post("http://www.tuling123.com/openapi/api",p)
    a = json.loads(a)
    print "小方:",a["text"]
