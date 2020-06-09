# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/1 17:00
filename(文件名): decimal.py
function description(功能描述):
    使用decimal模块中的Decimal类，避免浮点数产生的偏差
    使用math模块中的fsum模块，避免求和时大数吃掉小数
...
"""
from decimal import Decimal
from math import fsum

a = 4.2
b = 2.1
print(a + b)  # output 6.300000000000001
print(a + b == 6.3)  # output False

a = Decimal("4.2")
b = Decimal("2.1")
print(a + b)  # output 6.3
print(a + b == Decimal("6.3"))  # output True

nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))  # output 0
print(fsum(nums))  # output 1
