# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/27 10:02
filename(文件名): test.py
function description(功能描述):
...
"""
import os
import sys
from functools import reduce
sys.path.append(os.getcwd())

##############################################################################
*upper_path, sub_path = os.getcwd().split("\\")
# upper_path = reduce(os.path.join, *upper_path)
path = os.path.join("\\".join(upper_path))
print(os.path.join("\\".join(upper_path)))
print(os.listdir(path))

##############################################################################

sys.path.remove(os.getcwd())
