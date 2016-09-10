#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import re
import io
from PIL import Image
import requests
import json
from bs4 import BeautifulSoup

class IPGW:
    def __init__(self):
        self.s = requests.Session()
    def setPwdandUser(self,u,p):
        self.user = str(u)
        self.password = str(p)
    def getVerifyCodePic(self):
        r = self.s.get('http://ipgw.neu.edu.cn:8800/').text
        self._csrf = re.findall('name="_csrf" value="(.+?)">',r)[0]
        imgUrl = "http://ipgw.neu.edu.cn:8800/"+re.findall('src="(.+?)" alt=""',r)[0]
        verifyCodePic = Image.open(io.BytesIO(self.s.get(imgUrl).content))
        return verifyCodePic
    def getNewVerifyCodePic(self):
        self.s = requests.Session()
        return self.getVerifyCodePic()
    def login(self,verifyCode):
        data = {
        '_csrf' : self._csrf,
        'LoginForm[username]' : self.user,
        'LoginForm[password]' : self.password,
        'LoginForm[verifyCode]' : verifyCode,
        }
        r = self.s.post("http://ipgw.neu.edu.cn:8800/",data=data).text
        l = r.find('请修复以下错误')
        if l!=-1:
            if r[l+19:l+27]=='用户名或密码错误':
                res = [3,'用户名或密码错误']
            else:
                res = [2,'验证码不正确']
            return json.dumps(res)
        else:
            res = [1,r]
            return json.dumps(res)
    def drop(self,code):
        url = 'http://ipgw.neu.edu.cn:8800/home/base/drop'
        data = {
        'id' : code
        }
        r = self.s.post(url,data=data).text
        return r
    def changePassword(self,pwd):
        url = 'http://ipgw.neu.edu.cn:8800/user/chgpwd/index'
        data = {
        '_csrf' : self._csrf,
        'ModifyPasswordForm[old_password]':self.password,
        'ModifyPasswordForm[user_password]':str(pwd),
        'ModifyPasswordForm[user_password2]':str(pwd),
        }
        r = self.s.post(url,data=data).text
        return r
    def detail(self):
        url = 'http://ipgw.neu.edu.cn:8800/log/detail/index?page=12&per-page=10'
        res = self.s.get(url).text
        return res

if __name__ == "__main__":
    username = 20154409
    password = 606123
    if len(sys.argv)==3:
        username = sys.argv[1]
        password = sys.argv[2]
    aa = IPGW()
    aa.getVerifyCodePic().show()
    aa.setPwdandUser(username,password)
    v = raw_input('>输入验证码\n>')
    res = json.loads(aa.login(v))
    de = []
    if res[0]==1:
        data = BeautifulSoup(res[1],"lxml")
        l = data.find_all('div' ,attrs={'class':"panel-body"})
        print '------用户信息---------'

        baseInfo = l[0].find_all('li')
        for i in baseInfo:
            print str(i.text).replace("	","").replace(" ","").replace("\n","")[6:]

        print '------产品信息---------'
        a = l[2].table
        a = a.find_all('tr')
        for i in range(1,len(a)):
            d = BeautifulSoup(str(a[i]),"lxml")
            f = d.find_all('td')
            for j in f:
                print j.text.replace("	","").replace(" ","").replace("\n","")
        print '------在线信息---------'

        devices = l[1].table
        devices = devices.find_all('tr')
        for i in range(1,len(devices)):
            d = BeautifulSoup(str(devices[i]),"lxml")
            f = d.find_all('td')
            de.append(f[len(f)-1].a['id'])
            print '\n设备编号',len(de)," ",
            # print f[len(f)-1].a['id']
            for j in range(len(f)-1):
                print f[j].text.replace("	","").replace("\n","")," ",
        f = raw_input("\n输入在线设备代号，退出设备，输入0退出程序\n")
        if(f=='0'):
            exit()
        if(int(f)>len(de)):
            print "设备代号输入错误\n"
        else:
            print de[int(f)-1]
            print aa.drop(de[int(f)-1])
        print aa.detail()
    else:
        print res[1]

    # aa.changePassword(606123)
