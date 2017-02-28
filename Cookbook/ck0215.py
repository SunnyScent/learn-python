"""字符串中插入变量"""
s = '{name} has {n} message.'
print(s.format(name='Guido', n=37))

name = 'Fuido'
n = 237
print(s.format_map(vars()))
print(vars())


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('woc', 23)
print(s.format_map(vars(a)))
print(vars(a))


class safesub(dict):
    """防止 key 找不到"""

    def __missing__(self, key):
        return '{' + key + '}'


del n
print(vars())
print(s.format_map(safesub(vars())))

# def sub(text):
#     return text.format_map(safesub(sys._getframe(1).f_locals))

import string

n = 26
s = string.Template("$name has $n message.")
print(s.substitute(vars()))
