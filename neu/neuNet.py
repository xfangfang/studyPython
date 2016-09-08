# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import requests
import json
import random

s = requests.Session()
def loginoff(ip):
    data = {
    'action':'auto_logout',
    'user_ip':ip,
    }
    c = s.post("http://ipgw.neu.edu.cn:804/srun_portal_pc.php",data = data).text
    if c.find('网络已断开')!=-1:
        print '网络已断开'
        return '网络已断开'
    elif c.find('您似乎未曾连接到网络')!=-1:
        print '您似乎未曾连接到网络'
        return '您似乎未曾连接到网络'

    # print c
def login(username,password):
    data = {
    'action':'login',
    'ac_id':'1',
    'username':str(username),
    'password':str(password),
    'save_me':'0',
    }
    b=s.post("http://ipgw.neu.edu.cn:804/srun_portal_pc.php",data = data)
    res = b.text

    if(res.find('E2620')!=-1):
        print '已经在线了'
        return '已经在线了'
    if(res.find('E2616')!=-1):
        print '已欠费'
        return '已欠费'
    if(res.find('E2531')!=-1):
        print '用户不存在'
        return '用户不存在'
    if(res.find('E2553')!=-1):
        print '密码错误'
        return '密码错误'
    if(res.find('网络已连接 ')!=-1):
        print '网络已连接'
        return '网络已连接'
    else:
        print "未知问题",res
def getInfor():
    k = str(random.randint(1000, 99999))
    data = {
    'k':k,
    'action':'get_online_info',
    'key':k,
    }
    c=s.post("http://ipgw.neu.edu.cn:804/include/auth_action.php?k="+k,\
    data=data).text
    data = c.split(",")
    flow = data[0]
    time = data[1]
    money = data[2]
    ip = data[5]
    print "已用流量："+ str(float(flow)/1e6)+" M"
    print "使用时间："+ str(int(time)/60)+"分钟"
    print "余额："+data[2]+"元"
    print "ip地址："+data[5]

if __name__ == '__main__':
    a = login('20154316','000000')
    if a == '网络已连接':
        getInfor()
    loginoff('118.202.41.48')
    # print help(random)
    # l = len(sys.argv[1:])
    # if(l!=2):
    #     print "neunet <username> <password>"
    # else:
    #     res = login(sys.argv[1],sys.argv[2])
    #     if res == "网络已连接":
    #         getInfor()
