# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/7 10:59
filename(文件名): test5.py
function description(功能描述):
    通过实现__reverse__()方法来实现类的反向迭代功能
...
"""


class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


count = Countdown(4)
for i in reversed(count):
    print(i)

for i in count:
    print(i)
