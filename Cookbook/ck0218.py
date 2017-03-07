"""字符串令牌解析"""
text = 'foo =  23 + 42 * 10'

tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
import re

"""
    ?P<TOKENNAME> 用于给一个模式命名
"""
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>)\s+'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

"""
    scanner() 创建一个scanner对象，在这个方法上不断的调用match方法会
    一步步扫描目标文本
"""
scanner = master_pat.scanner('foo = 42')
print(scanner.match())

"""
    生成器
"""


def generate_tokens(pat, text):
    from collections import namedtuple
    token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield token(m.lastgroup, m.group)


# eg
for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

"""
    过滤令牌流
"""

tokens = (tok for tok in generate_tokens(master_pat, text) if tok.type != 'WS')
for tok in tokens:
    print(tok)
