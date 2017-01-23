"""Keeping the Last N Items """
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example of use a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, previous in search(f, 'python', 5):
            for pline in previous:
                print(pline, end=' ')
            print(line, end=' ')
            print('_' * 20)
