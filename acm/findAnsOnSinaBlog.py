# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import requests

url = 'http://blog.sina.com.cn/u/c0d5430b0101b3ke'
r = requests.get(url).text
st = r.find("#in")
en = r.rfind("}")
print r[st:en]
