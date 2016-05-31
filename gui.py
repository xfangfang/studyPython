# -*- coding: utf-8 -*
import urllib2,json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from Tkinter import *
import tkMessageBox
def FangWen(url):
    req = urllib2.Request(url)
    req.add_header("apikey", "46be8c2ee42e728b2c76e60686993157")
    return urllib2.urlopen(req).read()
def FanYi(word):
    n1 = '&from=en&to=zh'
    n2 = '&from=zh&to=en'
    if word[0] > chr(127) :
        n = n2
    else :
        n = n1
    url = 'http://apis.baidu.com/apistore/tranlateservice/translate?query='+word+n
    res = FangWen(url)
    return json.loads(res)['retData']['trans_result'][0]['dst']

class Application(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.pack()
    self.createWidgets()

  def createWidgets(self):
    self.nameInput = Text(self,borderwidth = 1,width=40,height=20)
    self.nameInput.pack(side='right')
    self.alertButton = Button(self, text='立即翻译', command=self.fan)
    self.alertButton.pack(side='top')
    self.dictLabel = Label(self, text='...',width=44,height=22,fg='white',bg='black',wraplength=300)
    self.dictLabel.pack(side='left')

  def fan(self):
    name = self.nameInput.get('1.0',END)
    name = '%s' %name
    print "name:"+name
    print type(name)
    if name.strip()!='':
        name = FanYi(name)
        self.dictLabel['text']=name
        # print name
        #tkMessageBox.showinfo('翻译好啦', ' %s' % name)

dict = Application()
dict.master.title('小方的字典')
# dict.master.geometry('400x400')
dict.mainloop()
