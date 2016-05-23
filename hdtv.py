# -*- coding: utf-8 -*
import sys,re
reload(sys)
sys.setdefaultencoding( "utf-8" )
import re,time
from bs4 import BeautifulSoup
def Get(urls):
    import urllib2
    try:
        web=urllib2.urlopen(urls,timeout=10)
        return web.read()
    except urllib2.URLError,e:
        return e.reason

name = "cctv5hd"
url = "http://hdtv.neu6.edu.cn/time-select?p="+name
a = Get(url)
bt = BeautifulSoup(a,"lxml")
href = bt.find_all(attrs={'id' : "noon"})
name = bt.find_all(attrs={'id' : "afternoon"})
a = []
h = 0
n = 0
for t in range(0,8):
    # print "\n"+href[t].parent['id']
    a.append({'day':href[t].parent['id'],'video':[]})
    n = len(a)-1;
    # print href[t]['id']
    for i in href[t].find_all("div"):
        if i['id'] == 'list_status':
            for j in  i:
                a[n]['video'][len(a[n]['video'])-1]['href']=j['href']
                # print j['href']
        else:
            a[n]['video'].append({})
            for j in  i:
                a[n]['video'][len(a[n]['video'])-1]['name']=j
                a[n]['video'][len(a[n]['video'])-1]['href']=""
                # print j
    # print name[t]['id']
    for i in name[t].find_all("div"):
        if i['id'] == 'list_status':
            for j in  i:
                a[n]['video'][len(a[n]['video'])-1]['href']=j['href']
                # print j['href']
        else:
            a[n]['video'].append({})
            for j in  i:
                a[n]['video'][len(a[n]['video'])-1]['href']=""
                a[n]['video'][len(a[n]['video'])-1]['name']=j
                # print j

for i in a:
    print i['day']
    for j in i['video']:
        # print j
        print j['name'],
        print j['href']
# href = "%s" %href
# href = re.findall('<div id="list_item">(.+?)</a></div>',href)
# print href
