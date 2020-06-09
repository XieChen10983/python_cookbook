# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/7 10:50
filename(文件名): test3.py
function description(功能描述):
    希望用生成器函数来实现新的迭代模式，
    使用函数+yield
...
"""


def count(begin=0, end=None):
    assert isinstance(begin, (int, float))
    if end is None:
        while True:
            yield begin
            begin += 1
    else:
        assert isinstance(end, (int, float))
        while begin <= end:
            yield begin
            begin += 1


for n in count(begin=10, end=150):
    print(n)
