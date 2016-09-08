# -*- coding: utf-8 -*
import sys,time,re,json,urllib,Image
reload(sys)
sys.setdefaultencoding( "utf-8" )
def Post(urls,data):
    import urllib2
    request = urllib2.Request(urls,data)
    res=urllib2.urlopen(request,timeout=10)
    if res.getcode()!=200:
        return 'There is something Wrong'
    return res.read()
def Get(urls):
    import urllib2
    web=urllib2.urlopen(urls)
    return web.read().decode('gbk').encode('utf-8')
l=[]
num = 1
while True:
    ff = Get('http://202.118.31.197/ACTIONLOGON.APPPROCESS?mode=3')
    ran = re.findall('<img src="(.+?)" width="55"',ff)[0]
    ImageUrl = 'http://202.118.31.197/'+ran
    # FileName = ran[42:]+'.jpg'
    FileName = str(num)+'.jpg'
    num+=1
    address = '/Users/FANGs/Desktop/pic/'+FileName
    print urllib.urlretrieve(ImageUrl,address)[0]
# jj = '8Eui'
# f = Post("http://202.118.31.197/ACTIONLOGON.APPPROCESS?mode=3","WebUserNO=20154409&Password=606129&Agnomen="+jj+"&submit.x=20&submit.y=11")
