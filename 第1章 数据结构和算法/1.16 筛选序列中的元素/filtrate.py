# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/31 21:06
filename(文件名): filtrate.py
function description(功能描述):
    通过列表推导式、生成器表达式或者filter函数对列表进行筛选
    通过itertools模块中的compress函数进行筛选,compress(需要筛选的数据, 布尔型的列表)
...
"""

# ################下面用列表推导式对序列进行筛选##################### #
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
plus_list = [n for n in mylist if n >= 0]
abs_list = [n if n >= 0 else -n for n in mylist]
print(plus_list)
print(abs_list)

# ##################下面用生成器表达式筛选################## #
generator = (n for n in mylist if n >= 0)
for x in generator:
    print(x)


# ##########################下面用filter函数对列表进行筛选################# #
def is_int(val):
    try:
        _ = int(val)
        return True
    except ValueError:
        return False


values = ["1", "2", "-3", "-", "4", "N/A", "5"]
new = list(filter(is_int, values))
print(new)

# ###################compress函数####################### #
a = ["a", "b", "C", "d", "e", "f", "g", "h", "i", "j"]
b = [0, 1, 1, 0, 1, 0, 1, 0, 0]
from itertools import compress
print(list(compress(a, b)))
