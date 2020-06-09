# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/31 11:11
filename(文件名): dict_oper.py
function description(功能描述):
    探究字典的键值翻转、排序、最大值、最小值问题
    键值翻转：zip函数
    排序：sorted函数
    最大，最小：max、min，最好先用zip函数转为列表之后再弄，否则max(dict)只能得到键，不能得到完整的item
...
"""
# from operator import attrgetter, itemgetter

prices = {
    "ACME": 45.23,
    "AAPL": 612.78,
    "IBM": 205.55,
    "HPQ": 37.20,
    "FB": 10.75
}

# 找出最大最小值用min、max
min_ = min(zip(prices.values(), prices.keys()))
max_ = max(zip(prices.values(), prices.keys()))
print(min_, max_)

# 按值的大小排序
sorted_ = sorted(zip(prices.values(), prices.keys()), key=lambda x: -x[0])  # 从大到小排序，没有负号为从小到大
print(sorted_)
