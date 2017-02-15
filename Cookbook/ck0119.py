"""Transforming and Reducing Data at the Same Time"""

num = [1, 2, 3, 4, 5]
s = sum(x * x for x in num)
print(s)

# Determine if any .py files exist in a directory
import os

files = os.listdir("E:\python\learn-python\Cookbook")
if any(name.endswith('.py') for name in files):
    print('There be python')
else:
    print('Sorry, no python')

# output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fileds of a data structure
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
