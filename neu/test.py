# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import json
from bs4 import BeautifulSoup

f = open("/Users/FANGs/Downloads/上网明细.html")
d = f.read()
f.close()

data = BeautifulSoup(d,"lxml")
summary = data.find_all(name='div', attrs={'class':'summary'})
print summary[0].text

summaryNum = int(summary[0].find_all('b')[1].text)
print summaryNum

table = data.find_all(name='table', attrs={'class':'table table-bordered detail-view'})[0]
print table.thead
for i in table:
    if type(i)==type(table):
        tr = i.find_all('tr')
        for j in tr:
            print j.text
