# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/8 8:58
filename(文件名): test4.py
function description(功能描述):
    我们需要读写二进制数据，比如图像，声音文件等。使用open()函数的rb和wb模式就可以实现对二进制数据的读写
    将文本写入二进制文件：binary_file.write(text.encode("utf-8"))
    从二进制文件中读取数据并转化为文本：binary_file.read().decode("utf-8")
...
"""
with open("binary.bin", 'ab') as file:
    file.write(b'Hello World!\n')
    file.write("Hello World!\n".encode("utf-8"))
with open("binary.bin", 'rb') as file:
    data = file.read()
    for d in data:
        print(d)
