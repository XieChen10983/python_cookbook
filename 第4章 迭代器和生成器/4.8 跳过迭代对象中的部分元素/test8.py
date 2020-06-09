# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/7 11:16
filename(文件名): test8.py
function description(功能描述):
    使用itertools模块中的dropwhile()，跳过前面部分元素
...
"""
from itertools import dropwhile

a = iter(range(10))
for ele in dropwhile(lambda y: y < 5, a):
    print(ele)
