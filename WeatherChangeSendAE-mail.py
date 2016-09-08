# -*- coding: utf-8 -*-
import sys,re
reload(sys)
sys.setdefaultencoding( "utf-8" )

import time,json

def sendMail(contents="null",sendTo="2553041586@qq.com",subjects="不知道什么主题"):
    import smtplib
    from email.mime.text import MIMEText
    sender = "20154409@stu.neu.edu.cn"
    receivers = [sendTo]
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect("smtp.stu.neu.edu.cn", "25")
        state = smtpObj.login(sender, "606129")
        msg = MIMEText(contents)
        msg['Subject'] = subjects
        msg['From'] = sender
        msg['To'] = sendTo
        if state[0] == 235:
            smtpObj.sendmail(sender, receivers, msg.as_string())
            print "邮件发送成功"
            smtpObj.quit()
    except smtplib.SMTPException, e:
        print str(e)

def Get(urls):
    import urllib2
    try:
        web=urllib2.urlopen(urls,timeout=10)
        return web.read()
    except urllib2.URLError,e:
        return e.reason

def getWeather():
    import urllib2
    url = 'http://apis.baidu.com/apistore/weatherservice/weather?citypinyin=shenyang'
    req = urllib2.Request(url)
    req.add_header("apikey", "46be8c2ee42e728b2c76e60686993157")
    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        return (content)
def reRun(t,old):
    while(True):
        a = getWeather()
        a = json.loads(a)
        now = a['retData']['time']
        a = a['retData']['weather']
        print now,a
        if a != old:
            contents = str(now)+"更新：沈阳天气由"+str(old)+"变为"+str(a)+"."
            sendMail(contents,"2553041586@qq.com","天气有变化了")
            old = a
        time.sleep(t)


a = getWeather()
a = json.loads(a)
# print a
print '天气预报开始'
print a['retData']['time'],a['retData']['weather']

reRun(180,a['retData']['weather'])
#
