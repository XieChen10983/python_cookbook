# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/3/27 11:09
filename(文件名): deque.py
function description(功能描述):
...
"""
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# example use on a file
if __name__ == "__main__":
    with open("somefile.txt", "r", encoding="utf-8") as f:
        for line, prevlines in search(f, "python", 3):
            for pline in prevlines:
                print(pline, end="")
            print(line, end="")
            print("-"*20)
