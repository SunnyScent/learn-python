"""矩阵与线性代数运算"""

import numpy as np

m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)
print(m.T)

v = np.matrix([2], [3], [4])
print(v)

print(m * v)
