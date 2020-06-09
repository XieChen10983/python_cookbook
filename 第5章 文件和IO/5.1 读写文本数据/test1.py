# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/8 8:43
filename(文件名): test1.py
function description(功能描述):
    使用with open(...) as file: 的语句来读写文本
    如果没有用with来创建上下文环境，直接用file = open("file name", "rt")等时，需要注意关闭file.close()
    读写的方式包括：
        “rt”： read text 只读文本
        “rb”： read binary 只读二进制
        “wt”： write text 写文本（覆盖之前的文本）
        “wb”： write binary 写二进制数据（覆盖之前的数据）
        “at”： add text 写文本（在之前的文本上添加）
        “ab”： add binary 写二进制（在之前的数据上添加）
    编码的方式包括：
        "utf-8": 最常见
        "ascii":
        "latin-1":
        "utf-16":
...
"""
