from svm import *
from svmutil import *
from PIL import Image
import glob


def get_feature(img):
    width, height = img.size
    pixel_cnt_list = []
    for y in range(height):
        for x in range(width):
            if img.getpixel((x, y)) == (0,0,0):
                pixel_cnt_list.append(1)
            else:
                pixel_cnt_list.append(0)
    return pixel_cnt_list
def test(ad):
    f = open(ad+"data.txt",'w')
    n=0
    for imd in glob.glob(ad+ "*.png"):
        im = Image.open(imd)
        l = get_feature(im)
        f.write(str(n)+" ")
        for i in range(len(l)):
            f.write(str((i+1))+":"+str(l[i])+" ")
        f.write("\n")
        n+=1
    f.close()
    return ad+"data.txt"
def train(ad):
    f = open(ad+"../data.txt",'w')
    n=0
    for d in glob.glob(ad+"*"):
        for imd in glob.glob(d+ "/*.png"):
            im = Image.open(imd)
            l = get_feature(im)
            print n
            f.write(str(n)+" ")
            for i in range(len(l)):
                f.write(str((i+1))+":"+str(l[i])+" ")
            f.write("\n")
        n+=1
    f.close()
    return ad+"../data.txt"
def train_svm_model(ad):
    y, x = svm_read_problem(train(ad))
    model = svm_train(y, x)
    svm_save_model("/Users/FANGs/Desktop/svm_model_file", model)
    return "/Users/FANGs/Desktop/svm_model_file"
def svm_model_test(ad):
    a = "abcdefghijklmnopqrstuvwxyz"
    yt, xt = svm_read_problem(test(ad))
    model = svm_load_model("/Users/FANGs/Desktop/svm_model_file")
    p_label, p_acc, p_val = svm_predict(yt, xt, model)
    cnt = 0
    p = ""
    for item in p_label:
        p+=a[int(item)]
    return p


# train_svm_model('/Users/FANGs/Desktop/net/')
# print svm_model_test('/Users/FANGs/Desktop/net/a/')
