"""以指定列宽格式化字符串"""
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap

print(textwrap.fill(s, width=70))
print(textwrap.fill(s, width=40, initial_indent='    '))
print(textwrap.fill(s, width=40, subsequent_indent='    '))
