# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/31 11:04
filename(文件名): ordered_dictionary.py
function description(功能描述):
    采用collections中的OrderedDict类，使得字典中的内容有序。
    其可以帮助在进行JSON编码时精确控制各个字段的顺序
    其缺点是大小为普通的字典的两倍多
...
"""
from collections import OrderedDict
import json

d = OrderedDict()
d["foo"] = 1
d["bar"] = 2
d["spam"] = 3
d["grok"] = 4

for key in d:
    print(key, d[key])

print(json.dumps(d))
