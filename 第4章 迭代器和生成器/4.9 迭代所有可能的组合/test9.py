# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/7 11:26
filename(文件名): test9.py
function description(功能描述):
    使用itertools中的permutations(iterable, number)对iterable选取number个元素进行排列
    使用itertools中的combinations(iterable, number)对iterable选取number个元素进行组合，元素须不同
    使用itertools中的combinations_with_replacement(iterable, number)对iterable选取number个元素进行组合，元素可相同
...
"""
from itertools import permutations, combinations, combinations_with_replacement

print("--------------------permutation------------------------")
my_list = ["a", "b", "c"]
for p in permutations(my_list):
    print(p)
for p in permutations(my_list, 2):
    print(p)

print("--------------------combination------------------------")
for c in combinations(my_list, 2):
    print(c)

print("--------------------combination_with_replacement------------------------")
for c in combinations_with_replacement(my_list, 2):
    print(c)
