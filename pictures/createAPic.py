#!/usr/bin/env python
# coding=utf-8

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

s = 20

pic = Image.new('L', (2000,1000), color=255)
pic2 = pic

x,y = pic.size
o = (x/2,y/2)
print o

for i in range(x):
    pic.putpixel((i,o[1]), 0)
for i in range(y):
    pic.putpixel((o[0],i), 0)

#以o为原点，打印 x，y
def put(pic,o,x,y):
    pic.putpixel((o[0]+x, o[1]-y),0)

#打印坐标尺
def putX(pic,o,s):
    for i in range(0,o[0],s):
        put(pic, o, i, 0)
        put(pic, o, i, 1)
        put(pic, o, i, -1)
    for i in range(0,-o[0],-s):
        put(pic, o, i, 0)
        put(pic, o, i, 1)
        put(pic, o, i, -1)
def putY(pic,o,s):
    for i in range(0,o[1],s):
        put(pic, o,  0,i)
        put(pic, o,  1,i)
        put(pic, o,  -1,i)
    for i in range(0,-o[1],-s):
        put(pic, o,  0,i)
        put(pic, o,  1,i)
        put(pic, o,  -1,i)


# y = a*x + b
def plot2(pic,a,b):
    for i in range(x):
        tx = i-o[0]
        ty = a*tx+b
        if abs(ty)<y/2:
            put(pic, o, tx, ty)


# plot2(pic, 3, 100)
# putX(pic, o, 100)
# putY(pic, o, 100)

put(pic, (10,10), 1, 1)

pic.show()
