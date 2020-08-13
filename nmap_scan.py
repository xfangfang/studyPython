# 扫描内网设备数量，如果数量变化，发送邮件提醒
# 使用方式 python nmap_scan.py 192.168.1.0/24
# 建议搭配crontab 定时运行
# */5 * * * * /usr/bin/python /home/pi/nmap_scan.py 192.168.1.0/24 >> /home/pi/nmap.log 2>&1 &

import commands
import sys
import requests
import time
import os
import pickle
import re

IP = sys.argv[1]
COMMAND = 'nmap -sP '+IP
CACHE_PATH = 'nmap.cache'
LOCALTIME = time.asctime( time.localtime(time.time()) )

def saveParm(p):
    with open(CACHE_PATH,'wb') as f:
        pickle.dump(p,f)

def readParm():
    with open(CACHE_PATH,'rb') as f:
        return pickle.load(f)

def send_simple_message(text):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox*****.mailgun.org/messages",
		auth=("api", "*****"),
		data={"from": "NMAP helper <postmaster@sandbox*****.mailgun.org>",
			"to": "***** <*****@*****.com>",
			"subject": "network clients changed",
			"text": text})

if not os.path.exists(CACHE_PATH) : saveParm(0)
return_code, output = commands.getstatusoutput(COMMAND)
clientsNumLastTime = readParm()
n = re.search(r"(\d+)\shost", output)
num = int(n.group(1))


if num != clientsNumLastTime:
    print(output)
    saveParm(num)
    send_simple_message(output)
else:
    print('nothing happend. '+ LOCAL_TIME+'\n')
