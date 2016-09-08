#encoding=utf-8
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
import sys

f = file("/Users/FANGs/Desktop/a.txt","w")
n=0
while n<=0:
    ad = "/Users/FANGs/Desktop/Up_chr/"
    im = Image.open(ad+"24.jpg")
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(7)
    l=[]
    x,y = im.size
    for i in range(y):
        for j in range(x):
            if (im.getpixel((j,i))==(0,0,0)):
                l.append(1)
            else:
                l.append(0)
    g = 1
    f.write("num_"+str(n)+"=[\n")
    for i in l:
        f.write(str(i)+",")
        if(g%x==0):
            f.write("\n")
        g+=1
    f.write("]\n")
    n+=1
