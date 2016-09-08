#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def getdata(s):
    a = 'data = {\n'
    s = s.split('&')
    for i in s:
        i = i.split('=')
        a = a+"'"+i[0]+"'"+':'+"'"+i[1]+"',"+'\n'
    a = a+"}"
    print a

if __name__ == '__main__':
    l = len(sys.argv[1:])
    getdata('action=get_online_info&key=')
    # if(l!=1):
    #     print "paramToJsonData <param>"
    # else:
    #     getdata(sys.argv[1])
