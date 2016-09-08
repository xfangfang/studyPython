# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import re
import requests
import io
import os
import json
from PIL import Image
from PIL import ImageEnhance
from bs4 import BeautifulSoup

import mdata

class Student:
    def __init__(self, user,password):
        self.user = str(user)
        self.password = str(password)
        self.s = requests.Session()

    def login(self):
        url = "http://202.118.31.197/ACTIONLOGON.APPPROCESS?mode=4"
        res = self.s.get(url).text
        imageUrl = 'http://202.118.31.197/'+re.findall('<img src="(.+?)" width="55"',res)[0]
        im = Image.open(io.BytesIO(self.s.get(imageUrl).content))
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
        data= {
        'WebUserNO':str(self.user),
        'Password':str(self.password),
        'Agnomen':verifyCode,
        }
        url = "http://202.118.31.197/ACTIONLOGON.APPPROCESS?mode=4"
        t = self.s.post(url,data=data).text
        if re.findall("images/Logout2",t)==[]:
            l = '[0,"'+re.findall('alert((.+?));',t)[1][1][2:-2]+'"]'+" "+self.user+" "+self.password+"\n"
            # print l
            # return '[0,"'+re.findall('alert((.+?));',t)[1][1][2:-2]+'"]'
            return [False,l]
        else:
            l = '登录成功 '+re.findall('!&nbsp;(.+?)&nbsp;',t)[0]+" "+self.user+" "+self.password+"\n"
            # print l
            return [True,l]

    def getInfo(self):
        imageUrl = 'http://202.118.31.197/ACTIONDSPUSERPHOTO.APPPROCESS'
        data = self.s.get('http://202.118.31.197/ACTIONQUERYBASESTUDENTINFO.APPPROCESS?mode＝3').text #学籍信息
        data = BeautifulSoup(data,"lxml")
        q = data.find_all("table",attrs={'align':"left"})
        a = []
        for i in q[0]:
            if type(i)==type(q[0]) :
                for j in i :
                    if type(j) ==type(i):
                        a.append(j.text)
        for i in q[1]:
            if type(i)==type(q[1]) :
                for j in i :
                    if type(j) ==type(i):
                        a.append(j.text)
        data = {}
        for i in range(1,len(a),2):
            data[a[i-1]]=a[i]
        # data['照片'] = io.BytesIO(self.s.get(imageUrl).content)
        return json.dumps(data)

    def getPic(self):
        imageUrl = 'http://202.118.31.197/ACTIONDSPUSERPHOTO.APPPROCESS'
        pic = Image.open(io.BytesIO(self.s.get(imageUrl).content))
        return pic

    def getScore(self):
            score = self.s.get('http://202.118.31.197/ACTIONQUERYSTUDENTSCORE.APPPROCESS').text #成绩单
            score = BeautifulSoup(score, "lxml")
            q = score.find_all(attrs={'height':"36"})[0]
            point = q.text
            print point[point.find('平均学分绩点'):]
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
                    if type(r[0])==type(j):
                        temp[subject[k]] = j.string
                        k+=1
                lesson.append(temp)
            lesson.pop()
            lesson.pop(0)
            return json.dumps(lesson)

    def logoff(self):
        return self.s.get('http://202.118.31.197/ACTIONLOGOUT.APPPROCESS').text

if __name__ == "__main__":
    # for i in range(20160000,20160010):
    #     a = Student(i,i)
    #     r = a.login()
    #     print r[1]
    #     if r[0]:
    #         q = json.loads(a.getInfo())
    #         for i in q:
    #             print q[i]


    a = Student(20154577,20154577)
    r = a.login()
    print r[1]
    if r[0]:
        r = json.loads(a.getScore())
        for i in r:
            for j in i:
                print i[j],
            print

        q = json.loads(a.getInfo())
        for i in q:
            print i,q[i]

        a.getPic().show()
    a.logoff()

# l = getScore(20154364,973149077)
