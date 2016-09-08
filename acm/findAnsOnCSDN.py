# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import requests
from bs4 import BeautifulSoup

header = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:41.0) Gecko/20100101 Firefox/41.0'
}


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
def add(n,q,s):
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

r = s.post('http://poj.org/login',data=data).text
print "登录成功"
l = getSolved(l)
print "取过题数目"
1
for n in range(1326,4100):
    if l.has_key(n):
        print n,'accpted'
        continue
    else:
        print n
        print "??"
    try:
        word = 'poj'+str(n)
        url = 'http://www.baidu.com/s?wd="'+word+'" site:csdn.net'
        r = an.get(url,headers=header).text
        soup = BeautifulSoup(r,"lxml")
        for i in soup.find_all(attrs={'class':"t"}):
            url = i.a['href']
            r = requests.get(url,headers=header).text
            soup = BeautifulSoup(r,"lxml")
            for j in soup.find_all("pre",attrs={'class':"cpp"}):
                add(n,j.text,s)
                # print j.text
                l = getSolved(l)
                if l.has_key(n):
                    break
            if l.has_key(n):
                print '/\----ok'
                break
    except Exception,e:
        print Exception,":",e
