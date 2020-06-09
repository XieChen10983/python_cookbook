# coding=gbk
"""
author(作者): Channing Xie(谢琛)
time(时间): 2020/4/1 21:30
filename(文件名): np_matrix_.py
function description(功能描述):探究np.matrix在矩阵、线性代数方面的计算
    求逆: matrix.I
    求转置：numpy.linalg.inv(matrix)
    矩阵乘法：m*v
    计算行列式：numpy.linalg.det(matrix)
    计算特征值：numpy.linalg.eigvals(matrix)
    计算矩阵方程的解：numpy.linalg.solve(matrix, y)
...
"""
from numpy import matrix, linalg

m = matrix([
    [1, -2, 3],
    [0, 4, 5],
    [7, 8, -9],
])
print(m.T)
print(linalg.inv(m))

v = matrix([[2], [3], [4]])
print(m * v)

print(linalg.det(m))  # 计算行列式
print(linalg.eigvals(m))  # 计算特征值
print(linalg.solve(m, v))  # 计算矩阵方程
