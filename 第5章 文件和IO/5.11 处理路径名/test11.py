# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/6/9 21:36
filename(文件名): test11.py
function description(功能描述):
...
    此代码演示如何处理路径名，找到基文件名、目录名、绝对路径等
    1. 需要用到os模块
    2. os.path.basename(path): 获取基文件名
    3. os.path.dirname(path): 获取文件夹名
    4. os.path.join(component_1, ..., component_n): 融合文件名
    5. os.path.splitext(path): 将path分为类型之前和类型两部分，
        如os.path.splitext("~/Data/data.csv") => ("~/Data/data", ".csv")
"""
import os
path = '/Users/hi/Data/data.csv'

# 获取基文件名
print(os.path.basename(path))

# 获取目录名
print(os.path.dirname(path))

# 根据各部分融合文件名
parts = ['tmp', 'Data', os.path.basename(path)]
print(os.path.join(*parts))

# 分离出文件的扩展名
print(os.path.splitext(os.path.join(*parts)))
