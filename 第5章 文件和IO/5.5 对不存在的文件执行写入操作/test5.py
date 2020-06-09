# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/8 9:19
filename(文件名): test5.py
function description(功能描述):
    有时候我们想将数据写入到一个文件中，但不希望该文件已经存在于系统文件中，否则会将该系统文件修改了
    可以先判断是否存在同名文件，也可以直接用"xt"或"xb"模式
...
"""
import os
file_name = "exist.txt"
data = "Hello World!"

# method 1
if os.path.exists(file_name):
    raise FileExistsError
else:
    with open(file_name, 'wt') as file:
        file.write(data)

# method 2
with open(file_name, "xt") as file:
    print("xt方式写入文件")
    file.write(data)
