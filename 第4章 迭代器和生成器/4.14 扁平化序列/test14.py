# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/7 14:05
filename(文件名): test14.py
function description(功能描述):
    扁平化序列：[a, b, [c, d], [e, f, g]] => [a, b, c, d, e, f, g]
...
"""
from collections import Iterable


def flatten(Iter: Iterable, ignore_type=(str, bytes)):
    for item in Iter:
        if not isinstance(item, Iterable) or isinstance(item, ignore_type):
            yield item
        elif isinstance(item, Iterable):
            yield from flatten(item)


sequence = [1, 2, ["efl", "df0", "d", ["eff", "defe"]], [1, 2]]
print(flatten(sequence))
for i in flatten(sequence):
    print(i)
