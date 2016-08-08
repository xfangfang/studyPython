# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import re
import requests
import urllib
import io
from PIL import Image
from PIL import ImageEnhance
from bs4 import BeautifulSoup
import mdata
n = 20150000
while True:
    if n>20150000:
        break
    n+=1
    headers={
    'User-Agent': 'youGuessWhat',
    }
    url = "http://202.118.31.197/ACTIONLOGON.APPPROCESS?mode=4"
    s = requests.Session()
    res = s.get(url,headers=headers).text
    imageUrl = 'http://202.118.31.197/'+re.findall('<img src="(.+?)" width="55"',res)[0]
    im = Image.open(io.BytesIO(s.get(imageUrl,headers=headers).content))
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(7)
    x,y = im.size
    for i in range(y):
        for j in range(x):
            if (im.getpixel((j,i))!=(0,0,0)):
                im.putpixel((j,i),(255,255,255))
    num = [6,19,32,45]
    verifyCode = ""
    for i in range(4):
        a = im.crop((num[i],0,num[i]+13,20))
        l=[]
        x,y = a.size
        for i in range(y):
            for j in range(x):
                if (a.getpixel((j,i))==(0,0,0)):
                    l.append(1)
                else:
                    l.append(0)
        his=0
        chrr="";
        for i in mdata.data:
            r=0;
            for j in range(260):
                if(l[j]==mdata.data[i][j]):
                    r+=1
            if(r>his):
                his=r
                chrr=i
        verifyCode+=chrr
    # print "辅助输入验证码完毕:",verifyCode

    user = 20154409
    password = 606129
    data= {
    'WebUserNO':str(user),
    'Password':str(password),
    'Agnomen':verifyCode,
    }
    t = s.post(url,data=data,headers=headers).text
    if re.findall("images/Logout2",t)!=[]:
        print '登录成功',re.findall('!&nbsp;(.+?)&nbsp;',t)[0]
    else:
        print '登录失败',re.findall('alert((.+?));',t)[1][1][2:-2]
    # print s.get('http://202.118.31.197/ACTIONQUERYBASESTUDENTINFO.APPPROCESS?mode＝3').text #学籍信息
    score = s.get('http://202.118.31.197/ACTIONQUERYSTUDENTSCORE.APPPROCESS',headers=headers).text #成绩单
    score = BeautifulSoup(score, "lxml")
    table = score.html.body.table
    people = table.find_all(attrs={'height' : '36'})[0].string
    r = table.find_all('table',attrs={'align' : 'left'})[0].find_all('tr')
    subject = []
    lesson = []
    for i in r[0]:
        if type(r[0])==type(i):
            subject.append(i.string)
    for i in r:
        k=0
        temp = {}
        for j in i:
            if j.name=='td':
                temp[subject[k]] = j.string
                k+=1
        lesson.append(temp)
    lesson.pop()
    lesson.pop(0)
    for i in lesson:
        for j in i:
            print i[j],
        print
    s.get('http://202.118.31.197/ACTIONLOGOUT.APPPROCESS',headers=headers).text #注销
