# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/27 10:40
filename(文件名): variable_length_params.py
function description(功能描述):
...
"""

records = [
    ("foo", 1, 2),
    ("bar", "hello"),
    ("foo", 3, 4)
]


def foo(x, y):
    print("foo", x, y)


def bar(x):
    print("bar", x)


for tag, *params in records:
    if tag == "foo":
        foo(*params)
    elif tag == "bar":
        bar(*params)


path = 'B:\\python_cookbook\\第1章 数据结构和算法\\1.2 从任意长度的可迭代对象中分解元素'
print(path)
*upper_dir, sub_dir = path.split("\\")
upper_dir = "\\".join(upper_dir)
print(upper_dir)
