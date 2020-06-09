# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/1 16:55
filename(文件名): round_off.py
function description(功能描述):
    使用内置的round函数对数值进行四舍五入，包括取整。恰好为.5时，取偶数：如1.5，2.5均为2
    round(value, ndigits), ndigits是小数的位数
...
"""
print(round(1.23, 1))
print(round(1.27, 1))
print(round(1.5))
print(round(2.5))
