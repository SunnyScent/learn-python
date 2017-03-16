"""迭代器切片
    得到一个由迭代器生成的切片
"""


def count(n):
    while True:
        yield n
        n += 1


c = count(0)

import itertools

"""迭代器和生成器不能使用标准的切片操作"""
for x in itertools.islice(c, 10, 20):
    print(x)
