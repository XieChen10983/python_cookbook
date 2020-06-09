# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/7 14:45
filename(文件名): test2.py
function description(功能描述):
...
"""
with open("1.txt", 'rt') as file:
    with open("2.txt", 'at') as f:
        print("\n", file=f, end='')
        for line in file:
            print(line, file=f, end='')
