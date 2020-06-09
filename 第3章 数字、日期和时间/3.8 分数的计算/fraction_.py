# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/1 21:14
filename(文件名): fraction_.py
function description(功能描述):此代码探究小数的运算
    使用fraction模块来处理涉及分数的数学计算问题:
    Fraction类构造一个分数
    Fraction实例的加减乘除运算
    Fraction的分子和分母
    Fraction转为float
    float转为Fraction,需要设定一个最大分母
...
"""
from fractions import Fraction

a = Fraction(3, 5)
print(a.numerator, a.denominator)
b = Fraction(7, 9)
print(a + b)
print(a * b)
print(float(b))

c = 0.546875
print((a + b).limit_denominator(8))
