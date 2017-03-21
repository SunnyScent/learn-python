"""使用其他分割符或者终止符打印"""

print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',', end='!!\n')

for i in range(5):
    print(i)

for i in range(5):
    print(i, end=' ')

row = ('ACME', 50, 91.5)
print(*row, sep=',')
