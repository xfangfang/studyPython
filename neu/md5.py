# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import json

def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

def ran():
    import random
    return str(random.randint(1000000000000000000, 2999999999999999999))

def tim():
    import time
    day = time.strftime("%Y%m%d")
    now = time.strftime("%H%M%S")
    return  day+now

def WebView(urls):
    import urllib2
    # request=urllib2.Request(urls)
    web=urllib2.urlopen(urls)
    return web.read().decode('gbk').encode('utf-8')

userName = '20152579'
passwd = md5('20152579')
token = tim()
url = "http://202.118.31.241:8080/api/v1/login?userName="+userName+"&passwd="+passwd+"&token"+tim()+ran()

Login = WebView(url)
print Login
JsonLogin = json.loads(Login)
token = JsonLogin['data']['token']
UrlKeBiao = "http://202.118.31.241:8080/api/v1/courseSchedule2?token="+token

KeBiao = WebView(UrlKeBiao)
JsonKeBiao = json.loads(KeBiao)
# print type(JsonKeBiao['data'])
# print type(JsonKeBiao['data'][0])
r=0
while r!=42:
    print JsonKeBiao['data'][r]['name']
    r=r+1
# k=0
# r=0
# while r!=6:
#     print "%-25.20s"%(JsonKeBiao['data'][k+r]['name']),
#     k+=6
#     if k==42:
#         k=0
#         r=r+1
#         print '\n'
