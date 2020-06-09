# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/31 21:30
filename(文件名): operate_on_sequence.py
function description(功能描述):
    同时对数据做转换和换算: sum()、min()、max()函数等
    通过生成器进行
...
"""
nums = [1, 2, 3, 4, 5]
s = sum(x*x for x in nums)  # 生成器表达式
print("s: ", s)

s = ("ACME", 50, 123.45)
print(",".join(str(x) for x in s))  # 生成器表达式

portfolio = [
    {"name": "GOOG", "shares": 50},
    {"name": "YHOO", "shares": 75},
    {"name": "AOL", "shares": 20},
    {"name": "SCOX", "shares": 65},
]
min_share = min(s['shares'] for s in portfolio)  # 生成器表达式
print("min_share: ", min_share)
