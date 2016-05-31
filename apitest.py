# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import urllib2,cookielib,json,urllib

def FangWen(url):
    req = urllib2.Request(url)
    req.add_header("apikey", "46be8c2ee42e728b2c76e60686993157")
    return urllib2.urlopen(req).read()
def FanYi(word):
    url = 'http://apis.baidu.com/apistore/tranlateservice/translate?query='+dict+'&from=en&to=zh'
    res = FangWen(url)
    return json.loads(res)['retData']['trans_result'][0]['dst']
def Weather(city):
    url = 'http://apis.baidu.com/apistore/weatherservice/citylist?cityname='+city
    res = FangWen(url)
    n=[]
    for i in json.loads(res)['retData']:
        print i['province_cn'],i['district_cn'],i['name_cn']
        n.append(i['area_id'])
    # for i in n :
    #     print i
    r= input("输入城市序号...")

    url = 'http://apis.baidu.com/apistore/weatherservice/recentweathers?cityid='+n[r-1]
    res = FangWen(url)
    j=json.loads(res)['retData']
    print j['city'],j['today']['type']
str = raw_input("输入城市名称...")
Weather(str)
