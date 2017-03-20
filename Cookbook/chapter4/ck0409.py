""""排列组合的迭代"""

items = ['a', 'b', 'c']
from itertools import permutations

for p in permutations(items):
    print(p)

for p in permutations(items, 2):
    print(p)

from itertools import combinations

for p in combinations(items, 3):
    print(p)

for p in combinations(items, 2):
    print(p)

for p in combinations(items, 1):
    print(p)

# itertools.combinations with replacement() 允许同一个元素被选择多次

from itertools import combinations_with_replacement

for p in combinations_with_replacement(items, 3):
    print(p)
