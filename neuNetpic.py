
import json,requests
import imagehash,os
from PIL import Image


s = requests.Session()
f = s.get("http://ipgw.neu.edu.cn:8800/site/captcha?refresh=1").text
f = json.loads(f)
url = "http://ipgw.neu.edu.cn:8800/"+f['url']

n =1
while n<=100:
    address = '/Users/FANGs/Desktop/net/'+str(n)+'.png'
    pic = s.get(url).content
    f = open(address,"wb")
    f.write(pic)
    f.close()
    # query = Image.open(address)
    # h = str(imagehash.dhash(query))
    # os.rename(address,'/Users/FANGs/Desktop/net/'+h+'.png')
    n+=1
