"""无穷大与NaN"""

a = float('inf')
b = float('-inf')
c = float('nan')
print(a)
print(b)
print(c)

import math

print(math.isinf(a))
print(math.isnan(c))

print(a + 45)
print(a * 10)
print(10 / a)

print(a / a)
print(a + b)
##nan可以传播
