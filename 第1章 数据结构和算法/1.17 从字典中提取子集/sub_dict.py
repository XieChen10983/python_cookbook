# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/31 21:22
filename(文件名): sub_dict.py
function description(功能描述):
    用字典推导式来进行字典子集的提取
...
"""

prices = {
    "ACME": 45.23,
    "AAPL": 612.78,
    "IBM": 205.55,
    "HPQ": 37.20,
    "FB": 10.75,
}

print(prices)

pl = {key: value for key, value in prices.items() if value > 200}
p3 = dict((key, value) for key, value in prices.items() if value > 200)
print(pl)
print(p3)

keys = ["AAPL", "FB"]
p2 = {key: value for key, value in prices.items() if key in keys}
print(p2)
