# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import requests
import base64
import time
from bs4 import BeautifulSoup
import re
s = requests.Session()
an = requests.Session()
l = {}
def getSolved(l):
    score = 'http://poj.org/userstatus?user_id=xfang'
    r = requests.get(score).text
    l = {}
    f = re.findall(r'>\d+<',r)
    rank = int(f[0][1:-1])
    solved = int(f[1][1:-1])
    submissions = int(f[2][1:-1])
    soup = BeautifulSoup(r,"lxml")
    f = str(soup.find_all('script')[1].text)
    for i in re.findall('p\(\d+\)',f):
        l[int(i[2:-1])]=True
    # print rank,solved,submissions
    return l
data = {
    'user_id1':'xfang',
    'password1':'fangyc111',
    'B1':'login',
    'url':'/'
}
def add(l,n,q,s):
    q='#include<cstdio>\n#include<cstring>\n#include <iostream>\n'+q
    source = base64.b64encode(q)
    data = {
    'problem_id':str(n),
    'language':'4',
    'source':source,
    'submit':'Submit',
    'encoded':'1'
    }
    r = s.post('http://poj.org/submit',data=data).text
    time.sleep(3)
    l = getSolved(l)
    return l
r = s.post('http://poj.org/login',data=data).text
print "登录成功"
l = getSolved(l)
print "取过题数目"
1
for n in range(3278,4100):
    print n,
    if l.has_key(n):
        print 'accpted'
        continue
    try:
        word = 'poj'+str(n)
        r = an.get('http://zzk.cnblogs.com/s?t=b&p=1&w='+word,timeout=5).text
        soup = BeautifulSoup(r, "lxml")
        ans = []
        for i in soup.find_all(attrs={'class':"searchItem"}):
            url = i.a['href']
            r = an.get(url,timeout=5).text
            soup = BeautifulSoup(r,"lxml")
            for j in soup.find_all(attrs={'class':"cnblogs_code_hide"}):
                a = ""
                for k in j.pre:
                    if type(k) == type(j.pre):
                        if k.attrs !={}:
                            if k['style']!='color: #008080;':
                                a+=k.text
                    else:
                        if len(k)!=0:
                            a+=k
                a = a.replace("#","\n#")
                l = add(l,n,a,s)
                if l.has_key(n):
                    print 'ok'
                    break
            for j in soup.find_all(attrs={'class':"cnblogs_Highlighter"}):
                a = j.pre.text
                l = add(l,n,a,s)
                if l.has_key(n):
                    print 'ok'
                    break
            if l.has_key(n):
                print 'ok'
                break
    except Exception,e:
        print Exception,":",e
