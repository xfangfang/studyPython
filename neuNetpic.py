
import json,urllib
def Get(urls):
    import urllib2
    web=urllib2.urlopen(urls)
    return web.read().decode('gbk').encode('utf-8')
n =0
while n<=100:
    n+=1
    print n
    f = Get("http://ipgw.neu.edu.cn:8800/site/captcha?refresh=1")
    f = json.loads(f)
    url = "http://ipgw.neu.edu.cn:8800/"+f['url']
    address = '/Users/FANGs/Desktop/net/'+str(n)+'.png'
    print urllib.urlretrieve(url,address)[0]
