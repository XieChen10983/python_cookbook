# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/31 8:23
filename(文件名): heapq_.py
function description(功能描述):
    探究heapq模块中的nlargest和nsmallest函数，找出某个集合中的最大n个或最小n个数据
...
"""
import heapq
import random

a = [random.randint(0, 100) for _ in range(20)]
print(a)
small = heapq.nsmallest(5, a)
print("small: ", small)
large = heapq.nlargest(5, a)
print("large: ", large)

names = "abcdefghijklmnopqrstuvwxyz"
price_name_dict = [{"name": name, "price": random.random()} for name in names]
print(price_name_dict)

print("***********************************************************")
print(min(s['price'] for s in price_name_dict))
print(min(price_name_dict, key=lambda s: s['price']))
print("***********************************************************")

small2 = heapq.nsmallest(5, price_name_dict, key=lambda dict1: dict1["price"])
print(small2)
large2 = heapq.nlargest(5, price_name_dict, key=lambda dict1: dict1["price"])
print(large2)
