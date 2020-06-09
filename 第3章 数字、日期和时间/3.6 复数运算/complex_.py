# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/1 17:28
filename(文件名): complex_.py
function description(功能描述):此代码探究python中的复数运算
    complex(real_part, imagine_part)或real_part + (imagine_part)j
    a.real, a.imag, a.conjugate分别获取实部、虚部和共轭
    复数的运算需要用到cmath库或np库，math库会抛出异常
...
"""
import cmath
import numpy as np

a = complex(2, 4)
b = 3 - 5j
print(a)
print(b)
print(a.real, a.imag, a.conjugate())
print(a + b)
print(cmath.sin(a))

a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(np.sin(a))
