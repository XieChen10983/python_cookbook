# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/8 9:26
filename(文件名): test6.py
function description(功能描述):
    使用io库中的StringIO()和BytesIO()类可以创建类似于文件的对象，对象有write, read, getvalue等函数
    该对象只在运行时存在，是没有真正的文件描述符来对应的。
...
"""
from io import StringIO, BytesIO

string_io = StringIO()
bytes_io = BytesIO()

string = "Hello World!"
byte = b"Hello World!"
string_io.write(string)
print(string_io.getvalue())
#
print(" This is a test. ", file=string_io)
print(string_io.getvalue())
#
# a = string_io.read(4)
# print(a)

bytes_io.write(b"binary value")
print(bytes_io.getvalue())
