# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from bs4 import BeautifulSoup
import urllib2
import urllib
import re
import os
import json
import time

def get(url):
    res = urllib2.urlopen(url)
    return res.read()

urlReplies = 'http://baobab.wandoujia.com/api/v1/replies/video?lastId=0&id=7308&num=100'
urlDiscovery = 'http://baobab.wandoujia.com/api/v3/discovery'
urlFeed = 'http://baobab.wandoujia.com/api/v2/feed?num=2'
urlSearch = 'http://baobab.wandoujia.com/api/v1/search?query=vr'
def getFeed():
    urlFeed = 'http://baobab.wandoujia.com/api/v2/feed?num=2'
    res = get(urlFeed)
    res = json.loads(res)
    for i in res['issueList']:
        print time.ctime(i["date"]/1000)
        for j in i['itemList']:
            if j['type']=="video":
                print "《"+j['data']['title']+"》"
                print j['data']['description']
    return res

# getFeed()
res = get(urlSearch)
print res
# print res['count']
# print res['nextPageUrl']
# print res['total']
# for i in res['replyList']:
#     # print i
#     print "第",i['sequence'],"条",i['likeCount'],"人喜欢",time.ctime(i['createTime']/1000                               ),i['user']['nickname'],i['message'],i['user']['avatar']
