"""字节字符串上的字符串操作"""
data = b'Hello World'
print(data[0:5])

print(data.startswith(b'Hello'))

print(data.split())

print(data.replace(b'Hello', b'Hello Crule'))

data = bytearray(b'Hello World')
print(data[0:5])

print(data.startswith(b'Hello'))

print(data.split())

data = b'FOO:BAR,SPAM'
import re

print(re.split(b'[:,]', data))

a = 'Hello World'  # Text String
print(a[0])
print(a[1])

b = b'Hello World'
print(b[0])
print(b[1])
