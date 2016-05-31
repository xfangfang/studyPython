# -*- coding: utf-8 -*
import sys,re,json,urllib
reload(sys)
sys.setdefaultencoding( "utf-8" )


def WebView(urls):
    import urllib2
    web=urllib2.urlopen(urls)
    return web.read().decode('gbk').encode('utf-8')
o=2;
while True:
    global o
    s = str(o)
    url='http://yxpjw.net/luyilu/2015/0626/1705_'+s+'.html'
    o=o+1;
    print url
    aa = WebView(url)
    ran = re.findall('src="(.+?)" /></p>',aa)
    for i in ran:
        FileName = i[43:]
        print FileName
        lj = '/Users/FANGs/Desktop/python/picture/'+FileName
        print urllib.urlretrieve(i,lj)
