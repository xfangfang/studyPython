from PIL import Image
import imagehash
import shelve
import glob
import numpy as np
from numpy import *

d = [[0 for j in range(1255)] for i in range(1255)]

def lcs(a,b,la=0,lb=0):
    if (d[la][lb]):
        return d[la][lb];
    if(la==len(a) or lb==len(b)):
        return 0
    if(a[la]==b[lb]):
        d[la][lb]=lcs(a,b,la+1,lb+1)+1
        return d[la][lb]
    d[la][lb]=max(lcs(a,b,la+1,lb),lcs(a,b,la,lb+1));
    return d[la][lb]

p1 = '/Users/FANGs/Desktop/net/9_3.png'
p2 = '/Users/FANGs/Desktop/net/28_3.png'
p1 = Image.open(p1)
p2 = Image.open(p2)
x=20
y=20
h1 = [[0 for j in range(x)] for i in range(y)]
for i in range(x):
    for j in range(y):
        if p1.getpixel((i,j))==(0,0,0):
            h1[j][i]=1
        else:
            h1[j][i]=0
a1 = np.mat(h1)
h2 = [[0 for j in range(x)] for i in range(y)]
for i in range(x):
    for j in range(y):
        if p2.getpixel((i,j))==(0,0,0):
            h2[j][i]=1
        else:
            h2[j][i]=0
a2 = np.mat(h2)
c = a1*a2
print c
print eye(4)*eye(4)
# print lcs(h1,h2)
# db = shelve.open('/Users/FANGs/Desktop/test.shelve', writeback = True)
# for imagePath in glob.glob('/Users/FANGs/Desktop/net/' + "/*.png"):
    # image = Image.open(imagePath)
    # h = str(imagehash.dhash(image))
    # filename = imagePath[imagePath.rfind("/") + 1:]
    # db[h] = db.get(h, []) + [filename]
# db.close()

# db = shelve.open('/Users/FANGs/Desktop/test.shelve')
# query = Image.open('/Users/FANGs/Desktop/net/a/44_2.png')
# h = str(imagehash.dhash(query))
# filenames = db[h]
# print "Found %d images" % (len(filenames))
# for filename in filenames:
#     image = Image.open('/Users/FANGs/Desktop/net/a/' + "/" + filename)
#     image.show()
# db.close()
