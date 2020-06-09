# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/31 14:55
filename(文件名): sort_dictionaries.py
function description(功能描述):
    一个列表由字典构成，需要对此列表进行排序，其中字典都有相同的键，通过该键的值进行排序
    用key=lambda x: x[键]可以达到该效果
    通过operator模块中的itemgetter函数速度更快, itemgetter还适用于min和max函数
...
"""
from operator import itemgetter

rows = [
    {"fname": "Brain", "lname": "Jones", "uid": 1003},
    {"fname": "David", "lname": "Beazley", "uid": 1002},
    {"fname": "John", "lname": "Cleese", "uid": 1001},
    {"fname": "Big", "lname": "Jones", "uid": 1004},
]

sort_by_fname = sorted(rows, key=itemgetter("fname"))
sort_by_lname = sorted(rows, key=itemgetter("lname"))
sort_by_uid = sorted(rows, key=itemgetter("uid"))

print(sort_by_fname)
print(sort_by_lname)
print(sort_by_uid)
