# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/31 8:11
filename(文件名): deque2.py
function description(功能描述):
    此代码探究collections模块中deque函数的用法，它可以保留任意长度（包括无限长度）的队列，和列表之间可以相互转换。
    其有append、appendleft、pop、popleft方法，运行速度很快地执行添加和弹出的操作，复杂度为O(1).

...
"""
from collections import deque

queue = deque(range(10), maxlen=5)
print(list(queue))
queue.popleft()
print(queue)
queue.appendleft(45)
print(queue)
queue.pop()
print(queue)
