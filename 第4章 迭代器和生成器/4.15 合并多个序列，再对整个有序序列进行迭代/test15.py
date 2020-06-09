# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/7 12:34
filename(文件名): test15.py
function description(功能描述):
    使用heapq模块中的merge()函数将有序序列合并
    和itertools中的chain相比，其合并之后是有序的
...
"""
from heapq import merge

a = [1, 4, 7, 10]
b = (2, 5, 6, 11)
c = merge(a, b)
for c in c:
    print(c)
