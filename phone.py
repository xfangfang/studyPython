# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import sys, urllib, urllib2, json

url = 'http://apis.baidu.com/apistore/mobilenumber/mobilenumber?phone=15210011578'

req = urllib2.Request(url)

req.add_header("apikey", "46be8c2ee42e728b2c76e60686993157")

resp = urllib2.urlopen(req)
content = resp.read()
# print content
content = json.loads(content)
content = content['retData']
print content ['phone'],content['city'],content['province'],content['supplier']
