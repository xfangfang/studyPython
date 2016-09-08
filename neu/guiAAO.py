# -*- coding: utf-8 -*
from __future__ import print_function

import urllib2,json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from Tkinter import *
from PIL import Image, ImageTk
import tkMessageBox
import requests
from autoAAO import *
import time
import io

MENU_ITEMS = ['Windows', 'Edit', 'Format', 'Run', 'Options', 'Windows', 'Help']
class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.createWidgets()
        self.initMenu()

    def createWidgets(self):
        self.L1 = LabelFrame(self,bg = "black")
        self.L1.pack(side = TOP,fill = X,expand = 1,ipadx = 10)

        self.user = Text(self.L1,height=1,width=8)
        self.user.pack(fill = BOTH,expand = 1,side = LEFT,padx = 4)
        self.password = Text(self.L1,height=1,width=8)
        self.password.pack(fill = BOTH,expand = 1,side = LEFT,padx = 0)
        self.sign = Button(self.L1, text='登录', command=self.login)
        self.sign.pack(side=LEFT,padx = 10)

        self.mesg = Label(self, text='...',width=44,height=40,fg='white',bg='black',wraplength=300)
        self.mesg.pack(side='bottom',fill = Y,expand = 1)
    def initMenu(self):
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="退出",command = self.quit )
        filemenu.add_separator()
        filemenu.add_command(label="123",command = lambda:print(123) )
        menubar.add_cascade(label=MENU_ITEMS[0], menu=filemenu)
        self.config(menu=menubar)

    def login(self):
        name = self.user.get('1.0',END)[:-1]
        pa = self.password.get('1.0',END)[:-1]
        stu = Student(name,pa)
        res = stu.login()
        self.mesg['text'] = res[1]
        print(res[1]) #显示登录是否成功
        data = ""
        if res[0]:
            #如果登录成功
            score = json.loads(stu.getScore())
            for i in score:
                for j in i:
                    data+=(str(i[j])+" ")
                    print(i[j],)
                print
                data+= "\n"
            info = json.loads(stu.getInfo())
            for i in info:
                print(i,info[i])
            pic = stu.getPic()
            img = ImageTk.PhotoImage(pic)
            self.pic = Label(self, bg = 'red',image = img)
            self.pic.image = img
            self.pic.pack(side = 'bottom')
            stu.logoff()
            self.mesg['text'] += data
g = lambda x:print(x)
dict = Application()
dict.title('NEU教务处')
dict.geometry('400x800')
dict.mainloop()
