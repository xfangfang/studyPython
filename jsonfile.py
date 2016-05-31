# -*- coding: utf-8 -*
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import json
filehandler = open('namelist.txt','r')
a = filehandler.read()
filehandler.close()
j =json.loads(a.replace('\n', ''))
# 2216
# print j['data'][0]['major']
s='任'
# s = input("seach:")
s2=''
#参数二
l= len(s)
if s2=='':
    s2='201'
l2= len(s2)


if  s[0] > chr(127):
    l=l/3
    emp='汉字'
    print emp
elif s[:3]=='201':
    emp='id'
    print emp
elif s[:2]=='19' or s[:2]=='20':
    emp='birth'
    print emp
else :
    emp = 'idcard'
    print emp

if  s2[0] > chr(127):
    l2=l2/3
    emp2='汉字'
    print emp2
elif s2[:3]=='201':
    emp2='id'
    print emp2
elif s2[:2]=='19' or s2[:2]=='20':
    emp2='birth'
    print emp2
else :
    emp2 = 'idcard'
    print emp2

for e in j['data']:
    if emp =='汉字':
        if e['sex'][:l] == s or e['name'][:l] == s or e['major'][:l] == s:
            if emp2 =='汉字':
                if e['sex'][:l2] == s2 or e['name'][:l2] == s2 or e['major'][:l2] == s2:
                    print e['id'],e['birth'],e['idcard'],e['major'],e['sex'],e['name']
            elif e[emp2][:l2] == s2:
                print e['id'],e['birth'],e['idcard'],e['major'],e['sex'],e['name']
    elif e[emp][:l] == s:
        if emp2 =='汉字':
            if e['sex'][:l2] == s2 or e['name'][:l2] == s2 or e['major'][:l2] == s2:
                print e['id'],e['birth'],e['idcard'],e['major'],e['sex'],e['name']
        elif e[emp2][:l2] == s2:
            print e['id'],e['birth'],e['idcard'],e['major'],e['sex'],e['name']
