# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/6/9 21:07
filename(文件名): test7.py
function description(功能描述):
...
    以下程序展示了如何读取和写入压缩的数据文件。
    1. 需要用到 gzip模块 或 bz2模块
    2. 选择正确的文件模式是至关重要的，如果没有指定模式，默认的模式是二进制。
    3. 写入压缩数据时，可以用compresslevel关键字指定压缩级别，默认级别是9，代表着最高的压缩等级。
        with gzip.open("somefile.gz", 'wt', compresslevel=5) as file:
"""
import gzip
import bz2
text = '我爱你'

# 下面是写入压缩的数据文件
with gzip.open("testfile.gz", 'wt') as f:
    f.write(text)

with bz2.open("testfile.bz2", 'wt') as f:
    f.write(text)

# 下面是读取压缩的数据文件
import os
if os.path.exists("testfile.gz"):
    with gzip.open("testfile.gz", 'rt') as file:
        text = file.read()
        print("gzip读取：", text)

# if os.path.exists("testfile.bz2"):
#     # print("hi")
#     with bz2.open("testfile.gz", 'rt') as file:
#         text = file.read()
#         print("bz2读取：", text)
