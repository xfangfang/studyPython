# -*- coding: utf-8 -*
import sys,re,json,requests,os,io
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
from svmPic import *

s = requests.Session()
f = s.get("http://ipgw.neu.edu.cn:8800/site/captcha?refresh=1").text
f = json.loads(f)
url = "http://ipgw.neu.edu.cn:8800/"+f['url']

def convent (pic):
    x,y = pic.size

    l = [[0 for j in range(y+5)] for i in range(x+5)]
    for i in range(x):
        for j in range(y):
            if pic.getpixel((i,j))!=(255,255,255):
                l[i+1][j+1]=1
    time = 2
    new = [-1,0,1]
    while time!=0:
        time-=1
        d = [[-1 for j in range(y+5)] for i in range(x+5)]
        for i in range(x):
            for j in range(y):
                if d[i+1][j+1]==-1:
                    if l[i+1][j+1]==0:
                        for q in range(3):
                            for w in range(3):
                                if l[i+1+new[q]][j+1+new[w]]==1:
                                    l[i+1+new[q]][j+1+new[w]]=0
                                    d[i+1+new[q]][j+1+new[w]]=0
    for i in range(x):
        for j in range(y):
            pic.putpixel((i,j),(255,255,255))
    for i in range(x):
        for j in range(y):
            if l[i+1][j+1]==1:
                pic.putpixel((i,j),(0,0,0))
    return pic


for svd in range(1):
    print svd
    address = '/Users/FANGs/Desktop/net/'+str(svd)+'.png'
    im = Image.open(io.BytesIO(s.get(url).content))
    # im = convent(im)
    x,y = im.size
    l = []
    for i in range(x):
        n=0
        for j in range(y):
            if im.getpixel((i,j))==(0,0,0):
                n+=1
        l.append(n)

    a=b=0
    for i in range(len(l)):
        if l[i]!=0:
            a = i
            break
    for j in range(len(l)-1,0,-1):
        if l[j]!=0:
            b = j+1
            break
    for i in range(a,b):
        if l[i]==0:
            for j in range(i,b):
                if l[j]!=0:
                    temp = im.crop((j-1,0,x,y))
                    im.paste(temp,((i-1,0,i+x-j,y)))
                    l = []
                    for k in range(x):
                        n=0
                        for m in range(y):
                            if im.getpixel((k,m))==(0,0,0):
                                n+=1
                        l.append(n)
                    x -= (j-i)
                    b -= (j-i)
                    break

    t = (b-a)/4
    left = [a,a+t,a+2*t,a+3*t]
    right = [b-3*t,b-2*t,b-t,b]
    x = t/2+1
    for i in range(4):
        temp = 0
        p = left[i]
        for j in range(left[i],left[i]+x):
            if temp > l[j]:
                temp = l[j]
                p = j
        left[i] = p
        temp = 0
        p = right[i]
        for j in range(right[i],left[i]-x,-1):
            if temp > l[j]:
                temp = l[j]
                p = j
        right[i] = p
        p = im.crop((left[i]-2,0,right[i]+2,50))
        p = p.resize((25, 50), Image.ANTIALIAS)
        p.save('/Users/FANGs/Desktop/test/'+str(i)+'.png')

p = svm_model_test('/Users/FANGs/Desktop/test/')
print p
