from PIL import Image
import glob

for imagePath in glob.glob('/Users/FANGs/Desktop/net/' + "/*"):
    print imagePath[-1:]
    for uri in glob.glob(imagePath+'/*.png'):
        pic = Image.open(uri)
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
        pic.save(uri)
