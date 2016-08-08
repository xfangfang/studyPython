# -*- coding: utf-8 -*
import sys,re
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter

ad = '/Users/FANGs/Desktop/net/6.png'
im = Image.open(ad)
# im.show()
x,y = im.size
print x,y
# im = im.resize((x, y), Image.ANTIALIAS)
l = []
for i in range(x):
    n=0
    for j in range(y):
        if im.getpixel((i,j))==(0,0,0):
            n+=1
    l.append(n)
# im.show()
a=b=c=d=e=0

for i in range(len(l)):
    if l[i]!=0:
        a = i
        break
for j in range(len(l)-1,0,-1):
    if l[j]!=0:
        e = j+1
        break
for i in range(i+5,j-5):
    n=0
    for j in range(y):
        if im.getpixel((i,j))!=(0,0,0):
            n+=1
    if n==y:
        for j in range(y):
            im.putpixel((i,j),(0,0,0))
im.show()
l = []
for i in range(x):
    n=0
    for j in range(y):
        if im.getpixel((i,j))==(0,0,0):
            n+=1
    l.append(n)
r=51
for k in range(a+5,e-5):
    if r>l[k]:
        r=l[k]
        b = c
        c = d
        d = k
num = [a,b,c,d,e]
print num
for i in range(4):
    a = im.crop((num[i],0,num[i+1],50))
    a.show()
