# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/31 11:26
filename(文件名): find_same_keys_values.py
function description(功能描述):
    此代码探究如何获取两个字典中相同或不同的键和值
    用&获取相同值，用-获取不同值
...
"""
a = {
    "x": 1,
    "y": 2,
    "z": 3
}
b = {
    "w": 10,
    "x": 11,
    "y": 2
}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())
print(a.keys() - {'z', 'w'})  # 可以借助-方法来去掉字典中的某些键，从而生成子字典
