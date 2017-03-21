"""顺序迭代合并后的排序迭代对象"""

# headq.merge
import heapq

a = [1, 4, 6, 5]
b = [2, 34, 5, 6]

for c in heapq.merge(a, b):
    print(c)

with open('sorted_file_1', 'rt') as file1, \
        open('sorted_file_2', 'rt') as file2, \
        open('merged_file', 'wt') as outf:
    for line in heapq.merge(file1, file2):
        outf.write(line)
