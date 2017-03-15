"""随机选择"""

import random

values = [1, 2, 3, 4, 5, 6]

print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))

print(random.sample(values, 2))
print(random.sample(values, 2))
print(random.sample(values, 3))
print(random.sample(values, 3))

print(random.shuffle(values))
print(random.shuffle(values))

print(random.randint(0, 10))

print(random.random())

print(random.getrandbits(200))
