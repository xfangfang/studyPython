# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json

url = 'http://apis.baidu.com/apistore/idservice/id?id=210726199702216714'


req = urllib2.Request(url)

req.add_header("apikey", "46be8c2ee42e728b2c76e60686993157")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)
