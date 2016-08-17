# -*- coding: utf-8 -*

import sys,re
from PIL import Image
# from PIL import ImageEnhance
# from PIL import ImageFilter
import logging
# logging.basicConfig(level=logging.DEBUG)

reload(sys)
sys.setdefaultencoding( "utf-8" )
import requests

headers={
'User-Agent': 'YouKnowWho',
}
s = requests.Session()
r = s.get('http://ipgw.neu.edu.cn:8800/',headers=headers)
r = r.text
_csrf = re.findall('name="_csrf" value="(.+?)">',r)[0]
imgUrl = "http://ipgw.neu.edu.cn:8800/"+re.findall('src="(.+?)" alt=""',r)[0]
pic = s.get(imgUrl)
ad = '/Users/FANGs/Desktop/Unknown.png'
f = open(ad,'wa')
f.write(pic.content)
f.close()
i = Image.open(ad)
i.show()


# verifyCode = raw_input('输入验证码')
#
# data = {
# '_csrf' : _csrf,
# 'LoginForm[username]' : '20154409',
# 'LoginForm[password]' : '606123',
# 'LoginForm[verifyCode]' : verifyCode,
# }
# r = s.post("http://ipgw.neu.edu.cn:8800/",data=data,headers=headers)
# print r.text
