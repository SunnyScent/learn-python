"""Splitting Strings on any of Multiple Delimiters"""

line = 'asdf fjdk; afed, fjek,asdf,      foo'
import re

print(re.split(r'[;,\s]\s*', line))

fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)
# Reform the line using the same delimiters
print(''.join(v + d for v, d in zip(values, delimiters)))
# ?:...   标识一个匹配不保存的分组
print(re.split(r'(?:,|;|\s)\s*', line))
