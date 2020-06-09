# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/1 21:23
filename(文件名): numpy_.py
function description(功能描述):
    numpy可以处理大型的数据，ndarray类型的数据，将一个函数作用在其上时，会同时施加于所有的元素之上
    ndarray和一行列表相加：每一列加上该行对应的数
    ndarray用条件假定来进行筛选
...
"""
import numpy as np

a = np.array([[1, 2, 3, 4], [5, 16, 17, 8], [9, 20, 21, 12]])
print(a + [100, 101, 102, 103])

b = np.where(a < 10, a, 10)
print(b)
