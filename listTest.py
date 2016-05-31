# -*- coding: utf-8 -*
import sys,re
reload(sys)
sys.setdefaultencoding( "utf-8" )
a = []
# a = [{'day':'2016-05-22','video':[{'name':"00:04 音乐电影欣赏",'href':'d'}]}]
a.append({'day':'2016-05-22','video':[]})
print len(a)
a[0]['video'].append({})
a[0]['video'][0]['name']='123'
a[0]['video'][0]['href']='456'
print a[0]['video']
for i in a[0]['video']:
    print i['name']
    print i['href']
