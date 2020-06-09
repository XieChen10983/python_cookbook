# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/1 21:04
filename(文件名): inf_nan.py
function description(功能描述):
    NaN会通过所有的操作进行传播，而且不会发生任何异常。如：nan + 2 = nan
    NaN == NaN  ==> False
    唯一安全检测NaN的方法是使用math.isnan(value)
...
"""
import math

a = float("inf")
b = float("-inf")
c = float("nan")
print(a, b, c)

print(math.isinf(a))
print(math.isnan(c))
