# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import urllib
import re
import os
ImagePath = os.path.join(os.getcwd(), 'captcha.png')
def get(url):
    res = urllib2.urlopen(url)
    return res.read()

def post(urls,data):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/601.5.17 (KHTML, like Gecko) Version/9.1 Safari/601.5.17",
    "Cookie": "PHPSESSID=6ra23o43d5i02sec0ggltnocd1; _csrf=6a4dd2046b87bb0f73572a94b2f1adb5757ce70e1fab625707dd8ab1fe81c17ca%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22eNtpgndYws3k3XFx2-iu2M2OqliNB4fw%22%3B%7D; _pk_id.10.b8a4=3d9dcd9fdaff9aba.1444971604.59.1460804574.1460804561.; _pk_ref.10.b8a4=%5B%22%22%2C%22%22%2C1460804561%2C%22http%3A%2F%2Fwww.neu.edu.cn%2F%22%5D; login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcrh7N4TPxBh44GCoNqvO0bJOCwrmDTc4yzZSpM%252BA6XiOpN5hvc3ZG6TeQDnwmYMqeUbk0z4wCMQungu8gQCdf1LIssLfCgo3d6YECj8JWgf9jR25BlWQOwGhStG6TCPbXYn%252FioI5iPZUf7i8CRp0%252BZj",
    "Connection":"keep-alive"}
    req = urllib2.Request(urls,data,headers)
    res=urllib2.urlopen(req,timeout=3)
    if res.getcode()!=200:
        return 'There is something Wrong'
    return res.read()

def show():
    pic = get(img)
    f = open(ImagePath, 'wb')
    f.write(pic)
    f.close()
    if os.name=='posix':
        os.system("open "+ImagePath)
    else :
        os.startfile(ImagePath)


url = 'http://ipgw.neu.edu.cn:8800/'
res = get(url)
soup = BeautifulSoup(res, "lxml")

csrf = soup.find_all("input")
print csrf[0]['value']
print csrf[0]['value'][:-2]

img = soup.find_all(src=re.compile("/site*"))[0]
img = img['src']
img = 'http://ipgw.neu.edu.cn:8800'+img

print img

# show()
# os.remove(ImagePath)

# cap = raw_input("测试")
cap = 'aaaa'

p =' _csrf='+csrf[0]['value'][:-2]+'%3D%3D&LoginForm%5Busername%5D=20154409&LoginForm%5Bpassword%5D=606123&LoginForm%5BverifyCode%5D='+cap+'&login-button='
print p
# t = post("http://ipgw.neu.edu.cn:8800/",p)
t = get('http://202.118.1.88:8800/home/base/index')
print t
