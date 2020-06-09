# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/31 10:40
filename(文件名): list_with_priority.py
function description(功能描述):
    定义一个类：拥有pop和push方法，push时可以额外给定一个数作为优先级
    运用的是heapq模块中的heappop和heappush方法。其操作的复杂度为O(logN)，效率非常高。
...
"""
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority=0):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


pri = PriorityQueue()
pri.push("a")
pri.push("c", 5)
pri.push("sd", 2)
print(pri.pop())
