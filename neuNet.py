# -*- coding: utf-8 -*
import sys,json,urllib2,re
reload(sys)
sys.setdefaultencoding( "utf-8" )

def ran():
    import random
    return str(random.randint(1000, 99999))

def Get(urls):
    import urllib2
    web=urllib2.urlopen(urls)
    return web.read()

def Post(urls,data):
    import urllib2
    request = urllib2.Request(urls,data)
    res=urllib2.urlopen(request,timeout=3)
    if res.getcode()!=200:
        return 'There is something Wrong'
    return res.read()

username = "20154409"
password = "606129"
b=Post("http://ipgw.neu.edu.cn:804/srun_portal_pc.php?ac_id=1&","action=login&ac_id=1&user_ip=&nas_ip=&user_mac=&url=&username="+username+"&password="+password+"&save_me=0")
#print b
k = ran()
c=Post("http://ipgw.neu.edu.cn:804/include/auth_action.php?k="+k,"action=get_online_info&key="+k)
print c
data = c.split(",")
flow = data[0]
time = data[1]
money = data[2]
ip = data[5]

print "已用流量："+ str(float(flow)/1e6)+" M"
print "使用时间："+ str(int(time)/60)+"分钟"
print "余额："+data[2]+"元"
print "ip地址："+data[5]
ip = "219.216.86.78"
#c = Post("http://ipgw.neu.edu.cn:804/srun_portal_pc.php","action=auto_logout&info=&user_ip="+ip)
print c
