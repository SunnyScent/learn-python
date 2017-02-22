"""将Unicode文本标准化"""
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)

print(s1 == s2)
print(len(s1))
print(len(s2))

import unicodedata

# NFC 表示字符应该是整体组成,比如可能的话就使用单一编码
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(ascii(t1))
# NFD 表示字符应该分解为多个组合字符表示
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
print(ascii(t3))

# python 支持扩展的标准化形式NFKC NFKD,他们在处理某些字符串的时候增加某些额外的兼容特性
s = '\ufb01'
print(s)
print(unicodedata.normalize('NFD', s))
print(unicodedata.normalize('NFKC', s))
print(unicodedata.normalize('NFKD', s))
