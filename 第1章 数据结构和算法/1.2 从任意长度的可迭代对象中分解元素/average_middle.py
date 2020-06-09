# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/27 10:28
filename(文件名): average_middle.py
function description(功能描述):实现对未知长度的序列的中间个数求平均值。使用“*”表达式可以解决这个问题
...
"""


def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)
