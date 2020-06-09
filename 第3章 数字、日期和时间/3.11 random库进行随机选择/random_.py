# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/1 21:46
filename(文件名): random_.py
function description(功能描述):
    利用random库进行随机操作
    从序列中随机选取：random.choice(sequence)
    从序列中随机选取N个元素：random.sample(sequence, N)
    将序列随机打乱顺序：random.shuffle(sequence)
    随机产生整数：random.randint(min, max)包含min和max
    随机产生0-1之间均匀分布的浮点数：random.random()
...
"""
import random

values = [1, 2, 3, 4, 5, 6]
for _ in range(6):
    print(random.choice(values))

print(random.sample(values, 2))
b = random.sample(values, 2)
print(values)

random.shuffle(values)
print(values)

for _ in range(5):
    print(str(random.randint(0, 10))+"  ", end="")
print("")
for _ in range(3):
    print(str(random.random())+"  ", end="")
