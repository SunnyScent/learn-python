"""数字的四舍五入"""

##不要试图用舍入浮点值来“修正” 表面上看起来正确的问题
a = 2.1
b = 4.2
c = a + b
print(c)
print(round(c, 2))

# 精确使用decimal
