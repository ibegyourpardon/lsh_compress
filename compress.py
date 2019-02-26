#!/usr/bin/python
#how to use
#python compress.py 图片目录的绝对路径
from PIL import Image
import os
import sys
import glob
import shutil

#设定目标输出路径文件夹
#desdir = "/lsh_des/"
#读取参数，输入文件夹路径
url = sys.argv[1]
#print(url)
#目标文件夹上级父目录
hjx = os.path.abspath(os.path.join(os.path.dirname(url),os.path.pardir))
#源目录最后一段
hw = os.path.basename(os.path.normpath(url))
#新目录
desdir = hjx + "/lsh_" + hw

#唔，先，复制个文件夹出来再说 2333
shutil.copytree(url,desdir)

#先不管了，复制一个原始的文件目录出来， 万一还要用呢，对吧

#创建文件夹
def mkdir(path):
    folder = os.path.exists(path + desdir)
    if not folder:
        os.makedirs(path +  desdir )
    else:
        print("-----")


#读取文件列表
def dirlist(path, allfile):  
    #filelist =  os.listdir(path)
    #下面这句用 glob 排除掉了 . 开头的隐藏文件
    filelist = glob.glob(os.path.join(path, '*'))
  
    for filename in filelist:  
        filepath = os.path.join(path, filename)
       
        if os.path.isdir(filepath):  
            dirlist(filepath, allfile)  
#            type=os.path.splitext(filename)[1]
#            if not type in image_types:
#                os.remove()
        else:  
            allfile.append(filepath)  
    return allfile 

#列出目标文件夹下所有文件
list = dirlist(desdir,[])
print(list)



# 默认压缩jpeg
def default_compress_jpeg(path,extname):
    lsh_png = Image.open(path)
    lsh_png.save(newpath,'JPEG',quality=50 )


# 默认压缩 png
def default_compress_png(path,newpath):
    lsh_png = Image.open(path)
    lsh_png.save(newpath,'PNG',quality=50 )


for x in list:
    image_types = [".jpg",".png",".jpeg"]
    fullpath = os.path.abspath(x)
    path = os.path.split(x)[0]
    filename = os.path.split(x)[1]
    extname = os.path.splitext(x)[1]
    if extname in image_types:

#在每个目录下创建对应的 des 目录用于存放压缩后的新图片
        #mkdir(path)
        newpath = desdir + filename
        if extname == ".png":
            default_compress_png(fullpath,newpath)
            print(fullpath + "压缩成功")
            print("========")
        elif extname == ".jpg":
            default_compress_jpeg(fullpath,newpath)
            print(fullpath + "压缩成功")
            print("========")
        elif extname ==".jpeg":
            default_compress_jpeg(fullpath,newpath)
            print(fullpath + "压缩成功")
            print("========")
        else:
            print(filename + "不是受支持的图片文件类型")

        #print(filename)
        # print(path)
        #print(extname)
    else:
        print("incorrect type")

