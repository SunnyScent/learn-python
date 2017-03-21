"""读取文本数据"""

# Read the entire file as a single string
with open('test.txt', 'rt') as f:
    data = f.read()

with open('text.txt', 'rt') as f:
    for line in f:
        print(line)

with open('test.txt', 'rt', encoding='latin-1') as f:
    print()

f = open('test.txt', 'rt', encoding='ascii', errors='replace')
f = open('test.txt', 'rt', encoding='ascii', errors='ignore')
