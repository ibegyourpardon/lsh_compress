# lsh_compress
Python压缩图片


使用方法：
python compress.py [URL] [quality]

[URL] 为图片文件夹所在路径
[quality] 为压缩质量 ，输入80则为压缩质量80%

例:
图片在
~/Downloads/source/
目录下的话

python compress.py ~/Downloads/source/ 90
暂时有点坑，路径最后需要带 / 才行
如果是
python compress.py ~/Downloads/source 90 则会出现结果目录错误的情况...
