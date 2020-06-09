# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/31 21:40
filename(文件名): map_dict.py
function description(功能描述):
    利用collections模块中的ChainMap类来将两个字典合并为逻辑上的一个字典
...
"""

from collections import ChainMap

a = {"x": 1, "z": 3}
b = {"y": 2, "z": 4}

# 用ChainMap来合并的c，如果a或b发生改变，c也会发生改变
c = ChainMap(a, b)
print(c)
print(c['x'])
print(c['y'])
print(c['z'])

# 用dict.update(dict)方法也可以将两个字典合并，但是其单独构建了一个完整的对象，若b发生了变化，d并不改变
d = a
d.update(b)
print(d)
