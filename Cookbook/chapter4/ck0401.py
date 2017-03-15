"""手动遍历迭代器"""


def manual_iter():
    with open('ck0402.py') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass


items = [1, 2, 3]
# Get the iterator
it = iter(items)
# Run the iterator
print(next(it))
print(next(it))
print(next(it))
