"""在正则表达式中使用Unicode"""

import re

num = re.compile('\d+')
# Ascii digits
print(num.match('123'))
# Arabic digits
print(num.match('\u0661\u0662\u0663'))
