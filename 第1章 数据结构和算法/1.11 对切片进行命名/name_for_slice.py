# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/31 14:30
filename(文件名): name_for_slice.py
function description(功能描述):
    如果序列中的一段是有某种意义的，我们除了用[start:stop]来获取外，还可以通过slice定义一个名称来获取
    slice函数的用法
...
"""
s = "I love you"
love = slice(2, 6)
print(s[2:6])
print(s[love])
