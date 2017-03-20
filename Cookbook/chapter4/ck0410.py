"""序列上索引值迭代"""
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

print("-------------------")
# 从1开始输出序号
for idx, val in enumerate(my_list, 1):
    print(idx, val)

from collections import defaultdict

word_summary = defaultdict(list)
with open('myfile.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

print(word_summary)

data = [(1, 2), (3, 4), (5, 6), (7, 8)]
# Correct!
##for n ,(x,y) in enumerate(data):
