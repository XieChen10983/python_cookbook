# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/8 8:52
filename(文件名): test3.py
function description(功能描述):
    print(value, sep=..., end=...)
    其中，sep设置分隔符，end设置行结尾符，同时end参数在输出中禁止打印换行符
...
"""
a = 1, 2, 3, 4, 5, 6
b = 2, 4, 8, 16, 32, 64
print(*a, sep=": ", end="")
print(*b, sep="- ", end="")
print("")
print(*b, end=" nihao")
