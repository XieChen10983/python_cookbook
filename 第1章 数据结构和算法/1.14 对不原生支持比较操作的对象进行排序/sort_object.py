# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/31 15:06
filename(文件名): sort_object.py
function description(功能描述):
    某一个对象不支持排序（比较大小），可以通过对象的某一属性对对象进行排序
    sorted函数 + operator.attrgetter方法可以解决此问题
    当然lambda函数也可以
...
"""
from operator import attrgetter


class User:
    def __init__(self, uid=0):
        self.id = uid

    def __repr__(self):
        return "User({})".format(self.id)


users = [User(23), User(3), User(99)]
sort_ = sorted(users, key=attrgetter("id"))
print(sort_)

sort__ = sorted(users, key=lambda x: x.id)
print(sort__)
