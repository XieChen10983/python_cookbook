# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/1 17:20
filename(文件名): test.py
function description(功能描述):
    探究不同的进制之间的转换
        format函数 + “o”、“b”、“x”，如format(value, "o")
        bin()、oct()、hex()函数
        转为十进制: int(str_of_value, 进制数)，如int("4d2", 16)
...
"""

x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

print(format(x, "o"))
print(format(x, "b"))
print(format(x, "x"))

print(int("4d2", 16))
