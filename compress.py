#!/usr/bin/python
#coding:utf-8

from PIL import Image
import os
import sys
import glob
import shutil
import time
from colorama import Fore, Back, Style

print("""\
|
|lllllllllllllllllllll'.ldc,.,:lllllllllllllllllllll:'..:xOO0d.,l|
|lllllllllllllllllllll.';oOOkc..,clllllllllllllll:'..,dO0x,l00;.c|
|llllllllllllllllllllc c,.kOxdl,  ..'''''..'......,lO000k',;x0o ;|
|llllllllllllllllllll; o. .',:clodddddodxxxxxxxddOKK000O,';;o0O.,|
|lllllllllllllllllll:. ';okKKKKKKKKKKKKKKKKKKKKKKKKKKKK;.;;;lK0,.|
|lllllllllllllllll;..;d0KKKKKKKKKKKKKKKKKXXXKKKKKKKKKKKx:,',xKK:.|
|lllllllllllllll:..lO0000KXNNNXXKKKKKKXXXWWWWNKKKKKKKKKKKKOOKKK: |
|llllllllllllll:.,O00OkxxkKNWWWWNKKKKXWWWWXOdlc::clox0KKKKKKKKKd.|
|llllllllllllll,.kk:',;:.  .'oXWNKKKKKNXo,':od'      .:OKKKKKKKKo|
|llllllllllllll'.x.:XWNc      '0KKKKKKK;.0WWW0         'KKKKKKKKK|
|llllllllllllll'.x.,kXN;      ,0KKKKKKKl.o0XWN'       .oNXKKKKKKK|
|llllllllllllll'.KXxc;,,... .l0KKKKK0000xc::;:,''',;cxXWWWNXKKKKK|
|llllllllllllll.,NNNNNNNkccd00000000000KXNNNNNNWWWWWWWWWWWWWNXKKK|
|lllllllllllll: oNNNNNNc:Oc,'...';oKXXNNNNNNWWWWWWWWWWWWWWWWWNXKK|
|lllllllllllll, kNNNNNO'KK'       :XNNNWWWWWWWWWWWWWWWWWWWWWWWNKK|
|lllllllllllll' ONWWWWXdWWXd:. ;o0NWWWNXWWWWWWWWWWWWWWWWWWWWWWNKK|
|lllllllllllll, dNWWWWWkxKK0Xx.OXNNWXXWKNXkKWWWWWWWWWWWWWWWWWWN00|
|lllllllllllllc..KNWWWWk'cdkx, ,okOKXXKxx'.dWWWWWWWWWWWWWWWNNNX00|
|llllllllllllllc.'0WWWWNXkl:,......,,;;cokXWWWWWWWWWWWWWWNNNNX000|
|lllllllllllllllc..dNWNNNNXX0OOOOO0KXNWWWWWWWWWWWWWWWWNNNNNNK0000|
|lllllllllllllllll, .o0NNNNNNNNNNNNNWWWWWWWWWWWWWWNNNNNNNXK000000|
|llllllllllllllllc..cc,';lx0NNNWWWWWWWWWWWWWWWWWWWNNNNNXK000000OO|
|llllllllllllllll' dNNNX0koloxOXNNNNWWWWWWWWNNNNNNNNNXXKK000OOOOO|
|lllllllllllllllc..0XXXXNNNNNNNNNNNNNNNK0OOOO0XNNNNNNNNNNX00OOOOO|
|lllllllllllllll, :XXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNX000OO00|
|lllllllllllllc' '0XXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNK0000000|
|llllllllllll:. c0XXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXK000000000|
|lllllllllll:..o000OO0XNNNNNNNNNNNNNNNNNNNNNNXXXNNXKK000000000000|
|lllllllllll. l000Odl:::coOXNNNNNNNNNNN0xl:;;;co00000000000000000|
|llllllllll: '0000000000ko:,:kNNNNNXk:,;cdxO000000000000000000000|
|llllllllll; ;0000000000000O:.cXNNK;.cO00000000000000000000Oll000|
+----------------------------------------------------------------+'
                    """)


print("正在初始化")
time.sleep(1)

#记录程序开始执行的时间
start = time.clock()

#读取参数
#第一个参数为输入文件夹路径
source_dir = sys.argv[1]
#第二个参数为压缩质量
thequality = int(sys.argv[2])

print (thequality)
print ('参数列表:', str(sys.argv))

#print(source_dir)
#目标文件夹上级父目录
hjx = os.path.abspath(os.path.join(os.path.dirname(source_dir),os.path.pardir))
#源目录最后一段
hw = os.path.basename(os.path.normpath(source_dir))
#新目录
desdir = hjx + "/lsh_" + hw



#唔，先，复制个文件夹出来再说 2333
shutil.copytree(source_dir,desdir)

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


#计算压缩前的文件夹大小
folder_size = 0
for (path, dirs, files) in os.walk(source_dir):
    for file in files:
        filename = os.path.join(path, file)
        folder_size += os.path.getsize(filename)

pre_size = "%0.1f MB" % (folder_size/(1024*1024.0))



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
i = 0
for x in list:
    image_types = [".jpg",".png",".jpeg"]
    fullpath = os.path.abspath(x)
    path = os.path.split(x)[0]
    filename = os.path.split(x)[1]
    extname = os.path.splitext(x)[1]
    if extname in image_types:
        #print(fullpath)
        i = i+1
        newpath = fullpath
        if extname == ".png":
            default_compress_png(fullpath,newpath)
            print(Fore.GREEN + "正在压缩  " + fullpath)
        elif extname == ".jpg":
            default_compress_jpeg(fullpath,newpath)
            print(Fore.GREEN + "正在压缩  " + fullpath)
        elif extname ==".jpeg":
            default_compress_jpeg(fullpath,newpath)
            print(Fore.GREEN + "正在压缩  " + fullpath)
        else:
            print(filename + "不是受支持的图片文件类型")

        #print(filename)
        # print(path)
        #print(extname)
    else:
        print("incorrect type")

# 计算压缩后的文件夹大小
folder_size = 0
for (path, dirs, files) in os.walk(desdir):
    for file in files:
        filename = os.path.join(path, file)
        folder_size += os.path.getsize(filename)

post_size = "%0.1f MB" % (folder_size / (1024 * 1024.0))


#计算程序运行时间
elapsed = (time.clock() - start)
print(Fore.BLUE + "所有图片压缩完成,一共压缩了" + str(i) + "张图片")
print (Fore.RED +  "图片压缩完成,耗时:" + str(elapsed) + "秒")
print("所有图片已从" + pre_size + "压缩到了" + post_size)