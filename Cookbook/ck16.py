"""Mapping keys to Multiple Values in Dictionary"""

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

a = {}
a.setdefault('a', []).append(1)
a.setdefault('a', []).append(2)
a.setdefault('b', []).append(4)

d = defaultdict(list)
pairs = [[1, 2], [3, 4]]
for key, value in pairs:
    d[key].append(value)

print(d)
