# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/7 10:39
filename(文件名): test2.py
function description(功能描述):
    通过实现__iter__()方法来构造一个可迭代的类
...
"""


class A:
    def __init__(self):
        self.list_ = []

    def __repr__(self):
        return "("+"".join([str(i) + ", " for i in self.list_[:-1]]) + str(self.list_[-1]) + ")"

    def append(self, item):
        self.list_.append(item)

    def __iter__(self):  # 因为添加了__iter__()方法，所以A变成可迭代的对象了
        return iter(self.list_)


a = A()
a.append(1)
a.append(2)
a.append(3)
for i in a:
    print(i)
print(a)
