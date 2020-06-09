# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/1 17:08
filename(文件名): format_.py
function description(功能描述):
    使用format函数或者 “%” 进行格式化输出。
    format(value, "*n.m*"):
        第一个*可取“^”、“<”、“>”，分别表示居中，左对齐，右对齐
        n表示输出的位数，不够补空格
        m表示输出的小数位数
        第二个*可取f、e等，f表示浮点数，e表示科学计数法
...
"""
x = 1234.56789
print(format(x, ".2f"))  # output 1234.57

print(format(x, ">10.1f"))  # output "    1234.6"
print(format(x, "<10.1f"))  # output "1234.6    "
print(format(x, "^10.1f"))  # output "  1234.6  "

print(format(x, "^10.2e"))  # output " 1.23e+03 "

print("% 10.2f" % x)
