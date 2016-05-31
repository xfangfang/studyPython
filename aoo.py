# -*- coding: utf-8 -*
import sys,time,re,json,urllib,Image
reload(sys)
sys.setdefaultencoding( "utf-8" )

def WebView(urls):
    import urllib2
    # request=urllib2.Request(urls)
    web=urllib2.urlopen(urls)
    return web.read().decode('gbk').encode('utf-8')
l=['123']
def see(dirs):
    im = Image.open(dirs)
    imgry = im.convert('L')
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    out = imgry.point(table,'1')
    print type(out)
    print out
while True:
    ff = WebView('http://202.118.31.197/ACTIONLOGON.APPPROCESS?mode=1&applicant=ACTIONQUERYBASESTUDENTINFO')
    ran = re.findall('<img src="(.+?)" width="55"',ff)[0]
    ImageUrl = 'http://202.118.31.197/'+ran
    FileName = ran[42:]+'.jpg'
    # FileName = '1'
    # for i in l:
    #     if i==FileName:
    #         print i
    #         print l
    #         exit()
    # l.append(FileName)
    lj = '/Users/FANGs/Desktop/python/image/'+FileName
    print urllib.urlretrieve(ImageUrl,lj)[0]
    see(lj)
