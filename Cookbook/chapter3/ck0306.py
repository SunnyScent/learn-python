"""复数的数学运算"""

a = complex(2, 4)
print(a)
b = 3 - 5j
print(b)

print(a.real)
print(a.imag)
print(a.conjugate())

print(a + b)
print(a * b)
print(a / b)
print(abs(a))

"""如果要执行其他的复数函数，使用cmath"""

import cmath

print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

import numpy as np

a = np.array([2 + 3j, 4 + 5j, 6 - 7j, 8 + 9j])
print(a)
print(a + 2)
print(np.sin(a))

print(cmath.sqrt(-1))
