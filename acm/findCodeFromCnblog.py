# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import re
import requests
from bs4 import BeautifulSoup

def ans(n):
    try:
        word = 'poj'+str(n)
        r = requests.get('http://zzk.cnblogs.com/s?t=b&p=1&w='+word,timeout=5).text
        soup = BeautifulSoup(r, "lxml")
        ans = []
        for i in soup.find_all(attrs={'class':"searchItem"}):
            url = i.a['href']
            r = requests.get(url,timeout=5).text
            soup = BeautifulSoup(r,"lxml")
            for j in soup.find_all(attrs={'class':"cnblogs_code_hide"}):
                a = ""
                for k in j.pre:
                    if type(k) == type(j.pre):
                        if k.attrs !={}:
                            if k['style']!='color: #008080;':
                                a+=k.text
                    else:
                        a+=k
                ans.append(a)
                break
            for j in soup.find_all(attrs={'class':"cnblogs_Highlighter"}):
                ans.append(j.pre.text)
                break
            if len(ans)>=1:
                break
        if len(ans)==1:
            return ans[0]
        else:
            return '0'
    except:
        return '0'
def getSolved():
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
    print rank,solved,submissions
    return l


l = [1,2]
print l.pop()
print l
