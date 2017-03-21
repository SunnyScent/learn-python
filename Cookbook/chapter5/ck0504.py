"""读写字节数据"""

with open('somefile.bin', 'rb') as f:
    data = f.read()

with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World')

t = 'Hello World'
print(t[0])
for c in t:
    print(c)

b = b'Hello World'
print(b[0])
for c in b:
    print(c)

with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('somefile.bin', 'wb') as f:
    text = 'Hello Wolrd'
    f.write(text.encode('utf-8'))

import array

a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    f.readinto(a)

print(a)
