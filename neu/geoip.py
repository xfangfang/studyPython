#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import requests
from bs4 import BeautifulSoup

def getIpInfor(ip='',v=''):
    print 'start'
    if(v != '6' and v != ''):
        print 'invalid',v
        return
    s = requests.Session()
    res = s.get('http://geoip.neu'+v+'.edu.cn/?ip='+ip).text
    data = BeautifulSoup(res,"lxml")
    div = data.find_all('div',attrs={"class":"row"})
    for i in range(2,len(div)):
        # print div[i]
        d = div[i].find_all('div')
        print d[0].text.replace('\n','').replace(' ',''),"----",d[1].text.encode('utf-8').replace('\n','').replace(' ','')
    print 'end'
if __name__ == '__main__':
    l = len(sys.argv[1:])
    if l == 0:
        getIpInfor()
    if l == 1:
        if(sys.argv[1] == '4'):
            getIpInfor()
        elif(sys.argv[1] == '6'):
            getIpInfor(v='6')
        else:
            getIpInfor(sys.argv[1])
    if l == 2:
        if(sys.argv[2] == '4'):
            getIpInfor(sys.argv[1],v='')
        if(sys.argv[2] == '6'):
            getIpInfor(sys.argv[1],v='6')
    # getIpInfor(ip = '202.118.31.226',v = '')
    # getIpInfor(v = '6')
