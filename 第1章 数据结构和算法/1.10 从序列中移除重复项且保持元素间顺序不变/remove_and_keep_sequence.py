# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/31 14:08
filename(文件名): remove_and_keep_sequence.py
function description(功能描述):
    去除序列中出现的重复元素，但仍然保持剩下的元素顺序不变
    如果序列中的值是可哈希的(数字、元组等)，则可通过集合和生成器来解决。
    如果序列中的值是不可哈希的(字典、列表等)，则需要指定一个函数来将序列转换为可哈希的类型
    直接用集合则不能保证顺序不变
...
"""


def dedupe_hashable(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_unhashable(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [1, 5, 2, 1, 9, 1, 5, 10]
b = [{'x': 1, "y": 2}, {'x': 1, "y": 3}, {'x': 1, "y": 2}, {'x': 2, "y": 4}]
c = [[1, 2], [1, 3], [1, 2], [2, 4]]
print(list(dedupe_hashable(a)))
print(list(dedupe_unhashable(b, key=lambda d: (d['x'], d['y']))))
print(list(dedupe_unhashable(c, key=tuple)))
