# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/1 22:08
filename(文件名): datetime_.py
function description(功能描述):
    使用datetime.datetime(year, month, day, ...)来创建日期
    使用datetime.timedelta(days)来获取时间间隔，此时间间隔可以用于加减
    datetime.datetime之间可以相加减，从而获取时间间隔
    datetime.datetime.today()获取当前的时间
    datetime实例a可以用a.weekday()来获取a为星期几
...
"""
import datetime

a = datetime.datetime.today()
print(a.weekday())
print(a)
print(a + datetime.timedelta(days=30))

b = datetime.datetime(2012, 12, 21)
print(b.weekday())
print(b)
print(a - b)
