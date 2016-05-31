#coding=utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        print x,
        print imgurl
        # urllib.urlretrieve(imgurl,'%s.png' % x)
        x+=1


html = getHtml("https://www.zhihu.com/question/33304970/answer/56383257")

getImg(html)
