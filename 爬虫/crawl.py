from bs4 import BeautifulSoup
import urllib2
import re
def Get(url):
    res = urllib2.urlopen(url)
    return res.read()

url = 'http://baike.baidu.com/subview/2482/6430317.htm'
a = Get(url)
# print a
s = BeautifulSoup(a,"lxml")
# s = s.find_all("a",target="_blank")
s = s.find_all("a",target="_blank",href="/view/"+"[0-9].+"+".htm" )
for i in s:
    print i

c = 'a*'
print c

#<a href="/view/159206.htm" target="_blank"></a>
