"""删除字符串中不需要的字符"""

# strip() 方法能用于删除开始或结尾的字符。lstrip()和rstrip()分别从左和右执行删除操作
# 默认情况下会删除空白字符
s = ' hello world \n'
print(s.strip())

print(s.lstrip())
print(s.rstrip())
t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))

# 去除操作不会对字符串的中间的文本产生任何影响
s = ' hello         world \n'
print(s.strip())
print(s.replace(' ', ''))
import re

print(re.sub('\s+', ' ', s))

with open('note.md') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)
