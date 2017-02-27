"""合并拼接字符串"""

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

a = 'Is Chicago'
b = 'Not Chicago'
print(a + ' ' + b)
print('hello' 'world')


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


print(' '.join(sample()))

with open("ck0214.txt", 'w') as f:
    for part in sample():
        f.write(part)
    f.close()


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
        yield ''.join(parts)


# 结合文件操作
with open('ck02142.txt', 'w') as f:
    for part in combine(sample(), 32768):
        f.write(part + '\n')
