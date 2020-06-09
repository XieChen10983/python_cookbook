# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/7 9:08
filename(文件名): test12.py
function description(功能描述):
    对于不同类型的可迭代对象，希望进行相同的操作，而不嵌套使用for循环
    例如将[1, 2, 3]和(4, 5, 6)中的数字逐个打印出来

    解决方法：
        使用itertools中的chain类：chain(*iterables) => generator
...
"""
from itertools import chain
data = [1, 2, 3], (4, 5, 6)
for data_ in chain(*data):
    print(data_)
