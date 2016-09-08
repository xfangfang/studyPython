# -*- coding: utf-8 -*
from PIL import Image

addr = '/Users/FANGs/Desktop/1.jpg'
q = '/Users/FANGs/Desktop/test.txt'
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(l):
    length = len(ascii_char)
    unit = (256.0 +1)/length
    return ascii_char[int(l/unit)]

im = Image.open(addr)
print im.mode
im = im.convert('L')
x,y = im.size
x/=1
y/=1
im = im.resize((x,y), Image.NEAREST)
a = ""
for i in range(y):
    for j in range(x):
        a += get_char(im.getpixel((j,i)))
    a += '\n'

print a
f = open(q,"w")
f.write(a)
f.close()
