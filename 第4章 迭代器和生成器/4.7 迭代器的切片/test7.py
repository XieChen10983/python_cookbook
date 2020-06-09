# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/7 11:10
filename(文件名): test7.py
function description(功能描述):
    使用itertools模块中的islice()来实现对迭代器和生成器的切片
...
"""
from itertools import islice

iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
iterable = iter(iterable)
try:
    for a in iterable[5, 8]:
        print(a)
except TypeError:
    pass

for a in islice(iterable, 5, 8):
    print(a, " ", end="")
