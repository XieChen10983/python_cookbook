# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/7 10:31
filename(文件名): test1.py
function description(功能描述):
    使用a = iter(Iterable)获取迭代器，with open() as f: f也是一个迭代器
    使用next(a)来访问迭代器中的元素
    迭代结束时会抛出StopIteration的异常
...
"""
with open("C:/Users/Administrator/Desktop/1.txt", encoding="utf-8") as f:
    try:
        while True:
            line = next(f)
            print(line, end="")
    except StopIteration:
        pass

another_iter = iter([1, 2, 4, 5, 3])
try:
    while True:
        print(next(another_iter))
except StopIteration:
    pass
