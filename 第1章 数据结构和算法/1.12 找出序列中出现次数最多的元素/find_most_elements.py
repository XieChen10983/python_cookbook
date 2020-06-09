# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/31 14:40
filename(文件名): find_most_elements.py
function description(功能描述):
    利用collections模块中的Counter类，可以对序列中的元素进行统计，利用其most_common方法可以找到最多的元素
    可以用Counter.update(Iterable)方法将Iterable更新到counter中
    可以对counter对象进行数学运算：a = Counter(words), b = Counter(more_words), a - b
...
"""
from collections import Counter

words = [
    "look", "into", "my", "eyes", "look", "into", "my", "eyes",
    "the", "eyes", "the", "eyes", "the", "eyes", "not", "around", "the",
    "eyes", "don't", "look", "around", "the", "eyes", "look", "into",
    "my", "eyes", "you're", "under"
]

more_words = [
    "why", "are", "you", "not", "looking", "in", "my", "eyes"
]

word_count = Counter(words)
print(word_count)
word_count.update(more_words)
print(word_count)

b = Counter(more_words)
print(word_count - b)
print(word_count + b)
print(word_count.most_common(3))
