"""展开嵌套序列"""

from collections import Iterable


def flatten(items, ignore_type=(str, bytes)):
    for item in items:
        if isinstance(item, Iterable) and not isinstance(item, ignore_type):
            # 检查每一个元素是够可以迭代，将字符串和字节排除在外
            yield from flatten(item)
        else:
            yield item


items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)

names = ['zhangsan', 'lisi', ['wangwu', 'zhangsi']]

for x in flatten(names):
    print(x)
