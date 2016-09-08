#!/usr/bin/env python
# -*- coding: utf-8 -*
# from __future__ import print_function

import urllib2,json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from Tkinter import *
from PIL import Image, ImageTk
import tkMessageBox
import requests
from autoIPGW import *
import time
import io


class Application(Tk):
    def __init__(self,n='login'):
        Tk.__init__(self)
        if n=='login':
            self.a = IPGW()
            pic = self.a.getVerifyCodePic()
            img = ImageTk.PhotoImage(pic)
            self.pic = Label(self, bg = 'red',image = img)
            self.pic.image = img
            self.pic.pack(side = 'bottom')

            self.loginWidgets()
            self.initMenu()
        else:

            self.Widgets()



    def loginWidgets(self):
        self.mesg = Label(self, text='登录校园网',fg="white",bg = "black")
        self.mesg.pack(side=TOP,fill = X,expand = 1)

        self.sign = Button(self, text='登录', command=self.login)
        self.sign.pack(side=BOTTOM,padx = 10)

        self.L1 = LabelFrame(self,bg = "black")
        self.L1.pack(side = BOTTOM,fill = X,expand = 1)
        self.user = Text(self.L1,height=1,width=16)
        self.user.pack(fill = Y,expand = 1,side = TOP)
        self.password = Text(self.L1,height=1,width=16)
        self.password.pack(fill = Y,expand = 1,side = BOTTOM)
        self.verifyCode = Text(self.L1,height=1,width=16)
        self.verifyCode.pack(fill = Y,expand = 1,side = BOTTOM)

    def Widgets(self):
        self.L1 = LabelFrame(self,bg = "black")
        self.L1.pack(side = TOP,fill = X,expand = 1,ipadx = 10)
        self.user = Text(self.L1,height=1,width=8)
        self.user.pack(fill = BOTH,expand = 1,side = LEFT,padx = 4)
        self.password = Text(self.L1,height=1,width=8)
        self.password.pack(fill = BOTH,expand = 1,side = LEFT,padx = 0)
        self.sign = Button(self.L1, text='啦啦', command=self.login)
        self.sign.pack(side=LEFT,padx = 10)


        self.mesg = Label(self, text='...',width=44,height=40,fg='white',bg='black',wraplength=300)
        self.mesg.pack(side='bottom',fill = Y,expand = 1)
    def initMenu(self):
        menubar = Menu(self)
        self.config(menu=menubar)
    def login(self):
        name = self.user.get('1.0',END)[:-1]
        pa = self.password.get('1.0',END)[:-1]
        v = self.verifyCode.get('1.0',END)[:-1]
        print name,pa,v
        a = self.a
        a.setPwdandUser(name,pa)
        res = json.loads(a.login(v))
        if res[0]==1:
            data = BeautifulSoup(res[1],"lxml")
            l = data.find_all('div' ,attrs={'class':"panel-body"})
            print '---------------'

            baseInfo = l[0].find_all('li')
            for i in baseInfo:
                print str(i.text).replace("	","").replace(" ","").replace("\n","")[6:]
            print '---------------'

            devices = l[1].table
            devices = devices.find_all('tr')
            for i in range(1,len(devices)):
                d = BeautifulSoup(str(devices[i]),"lxml")
                f = d.find_all('td')
                print f[len(f)-1].a['id']
                for j in range(len(f)-1):
                    print f[j].text.replace("	","").replace("\n","")

            print '---------------'
            a = l[2].table
            a = a.find_all('tr')
            for i in range(1,len(a)):
                d = BeautifulSoup(str(a[i]),"lxml")
                f = d.find_all('td')
                for j in f:
                    print j.text.replace("	","").replace(" ","").replace("\n","")
        else:
            print res[1]


loginWin = Application("login")
loginWin.title('NEU IPGW')
loginWin.geometry('300x300')
loginWin.mainloop()
