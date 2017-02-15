"""Mapping Names to Sequence Elements"""

from collections import namedtuple

Subscriber = namedtuple('Subcriber', ['addr', 'joined'])
sub = Subscriber('11111@163.com', '2012-10-12')
print(sub)
print(sub.count('11111@163.com'))
print(sub.addr)
print(sub.joined)

len(sub)
addr, joined = sub
print(addr)
print(joined)


def compute_cost(records):
    total = 0
    for rec in records:
        total += rec[1] * rec[2]
    return total


Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost2(records):
    total = 0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


s = Stock('ACME', '100', '123.45')
print(s)
# s.price = 567.7
s = s._replace(shares=75)
print(s)

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)


def dict_to_stock(s):
    return stock_prototype._replace(**s)
