# 运行在树莓派上
# 扫描指定名称的Wi-Fi，当该Wi-Fi状态改变（距离上次运行脚本启动或关闭）时发送邮件
# 推荐搭配 crontab 定时使用

import os
import commands
import requests
import time
import pickle

ESSID = '9DA2'
cache_path = 'wlan.cache'
command = 'sudo iwlist wlan0 scanning | grep ESSID'
localtime = time.asctime( time.localtime(time.time()) )


def saveParm(p):
    with open(cache_path,'wb') as f:
        pickle.dump(p,f)

def readParm():
    with open(cache_path,'rb') as f:
        return pickle.load(f)

def send_simple_message(text):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox*****.mailgun.org/messages",
        auth=("api", "*****"),
        data={"from": "WIFI helper <postmaster@sandbox*****.mailgun.org>",
        "to": "***** <*****@*****.com>",
        "subject": text,
        "text": 'change your wifi now'})

if not os.path.exists(cache_path) : saveParm(False)
return_code, output = commands.getstatusoutput(command)
isEssidOnlineLastTime = readParm()

if output.rfind(ESSID) == -1: # essid offline now
    if isEssidOnlineLastTime:
        print(ESSID+' is offline. '+localtime+'\n')
        saveParm(False)
        send_simple_message('9DA2 is offline')
    else:
        print('nothing happend. (offline) '+localtime+'\n')
else: # essid online now
    if isEssidOnlineLastTime:
        print('nothing happend. (online) '+localtime+'\n')
    else:
        print(ESSID+' is online. '+localtime+'\n')
        saveParm(True)
        send_simple_message('9DA2 is online')
