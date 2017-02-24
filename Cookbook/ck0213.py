"""字符串对齐"""
##ljust() ,rjust(), cneter()

text = 'hello wolrd'
print(text.ljust(20))

print(text.rjust(20))
print(text.ljust(20))
print(text.center(20))

print(text.rjust(20, '-'))
print(text.center(20, '*'))

# format
format(text, '>20')
format(text, '<20')
format(text, '^20')

print(format(text, '=>20s'))
print(format(text, '*^20s'))
print('\n')
print('{:>10s}  {:>10s}'.format('Hello', 'World'))

# format可以用来格式化任何值
x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))
