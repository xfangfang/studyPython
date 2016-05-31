# -*- coding: utf-8 -*
# import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )
def XiaoHuang(chat):
    import urllib2
    url ='http://www.xiaodoubi.com/bot/chat.php'
    req = urllib2.Request(url,'chat='+chat)
    print type(req)
    res=urllib2.urlopen(req,timeout=3)
    if res.getcode()!=200:
        return 'There is something Wrong'
    return res.read()
print "小贱鸡: 哼！\n二傻子:",
while True:
    # r = raw_input()
    # if r=="exit":
    #     break
    r='hi'
    print "小贱鸡:",
    print XiaoHuang(r),"\n二傻子:",
