#!/usr/bin/python
#coding:utf-8
decode('gbk').encode('utf-8')

from PIL import Image
import os
import sys
import glob
import shutil

#读取参数
#第一个参数为输入文件夹路径
url = sys.argv[1]
#第二个参数为压缩质量
thequality = int(sys.argv[2])

print (thequality)
print ('参数列表:', str(sys.argv))

#print(url)
#目标文件夹上级父目录
hjx = os.path.abspath(os.path.join(os.path.dirname(url),os.path.pardir))
#源目录最后一段
hw = os.path.basename(os.path.normpath(url))
#新目录
desdir = hjx + "/lsh_" + hw

#唔，先，复制个文件夹出来再说 2333
shutil.copytree(url,desdir)

#读取文件列表
def dirlist(path, allfile):  
    #filelist =  os.listdir(path)
    #下面这句用 glob 排除掉了 . 开头的隐藏文件
    filelist = glob.glob(os.path.join(path, '*'))
  
    for filename in filelist:  
        filepath = os.path.join(path, filename)
       
        if os.path.isdir(filepath):  
            dirlist(filepath, allfile)  
        else:
            allfile.append(filepath)  
    return allfile 



# 默认压缩jpeg
def default_compress_jpeg(path,extname):
    lsh_jpeg = Image.open(path)
    lsh_jpeg.save(newpath,'JPEG',quality= thequality )

# 默认压缩 png
def default_compress_png(path,newpath):
    lsh_png = Image.open(path)
    lsh_png.save(newpath,'PNG',quality= thequality )


#列出目标文件夹下所有文件
list = dirlist(desdir,[])
print("待处理文件列表")
print(list)
print("开始压缩")
for x in list:
    image_types = [".jpg",".png",".jpeg"]
    fullpath = os.path.abspath(x)
    path = os.path.split(x)[0]
    filename = os.path.split(x)[1]
    extname = os.path.splitext(x)[1]
    if extname in image_types:
        print(fullpath)

        newpath = fullpath
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

