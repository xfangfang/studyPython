#encoding=utf-8
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
import sys
import re
import mdata
import os
reload(sys)
sys.setdefaultencoding( "utf-8" )

n=1
while n<=1:
    password = []
    ad = "/Users/FANGs/Desktop/pic/"
    im = Image.open(ad+str(n)+".jpg")
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(7)
    x,y = im.size
    for i in range(y):
        for j in range(x):
            if (im.getpixel((j,i))!=(0,0,0)):
                im.putpixel((j,i),(255,255,255))
    num = [6,19,32,45]
    for i in range(4):
        a = im.crop((num[i],0,num[i]+13,20))
        # a.save(ad+"a"+str(n)+"_"+str(i)+".jpg")
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
        password.append(chrr)
        p = password
    print password
    # os.rename(ad+str(n)+".png",ad+p[0]+p[1]+p[2]+p[3]+".png")
    n+=1
