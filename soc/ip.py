# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import sys, urllib, urllib2, json

url = 'http://apis.baidu.com/apistore/iplookupservice/iplookup?ip=123.245.8.135'

req = urllib2.Request(url)

req.add_header("apikey", "46be8c2ee42e728b2c76e60686993157")

resp = urllib2.urlopen(req)
content = resp.read()

j = json.loads(content)
print j
print type(j)
for i in j['retData'].iteritems():
    print i

# content = json.loads(content)
# content = content['retData']
# print content['ip'],content['country'],content['province'],content['city'],content['district'],content['carrier']
