# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/31 10:51
filename(文件名): multi_map.py
function description(功能描述):
    字典的键映射到多个值上==键的值为列表（有重合元素）或者集合（无重合元素）
    可以采用collections中的defaultdict方法，将值的类型提前设定为列表或集合
    如希望创建这样一个字典：
    d = {
        "a": [1, 2, 3],
        "b": [4, 5, 4]
    }
    e = {
        "a": {1, 2, 3},
        "b": {4, 5}
    }
...
"""
from collections import defaultdict

d = defaultdict(list)
e = defaultdict(set)
a_ = [1, 2, 3]
b_ = [4, 5, 4]
for a in a_:
    d["a"].append(a)
    e["a"].add(a)
for b in b_:
    d["b"].append(b)
    e["b"].add(b)
print(d)
print(e)
