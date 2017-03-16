"""跳过可迭代部分的开始部分"""

with open('ck0405.py', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')

from itertools import dropwhile

with open('ck0405.py', 'r', encoding='utf-8') as f:
    for line in dropwhile(lambda line: line.startwith('#'), f):
        print(line, end='')

from itertools import islice

items = ['a', 'b', 'c', 1, 5, 3, 34]
for x in islice(items, 3, None):
    print(x)
