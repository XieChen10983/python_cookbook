# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/7 11:37
filename(文件名): test11.py
function description(功能描述):
    使用zip函数同时迭代多个序列
    zip(a, b)的工作原理是创建出一个迭代器，该迭代器可以产生出元祖(x, y)，这里的x取自a， y取自b

    如果序列的长度不一样，可以用itertools中的zip_longest(fillvalue=value)来以最长的序列为基
...
"""
list1 = range(0, 5)
list2 = range(6, 20)
for i, j in zip(list1, list2):
    print(i, j)
print(zip(list1, list2))

from itertools import zip_longest
for i, j in zip_longest(list1, list2, fillvalue=0):
    print(i, j)
