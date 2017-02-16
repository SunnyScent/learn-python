"""字符串开头或者结尾匹配"""
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))

import os

filenames = os.listdir('.')
print(filenames)
print([name for name in filenames if name.endswith(('.c', '.h'))])
print(any(name.endswith('.py') for name in filenames))

import urllib.request


def read_data(name):
    if name.endswith(('http', 'https', 'ftp')):
        return urllib.request.urlopen(name).open
    else:
        with open(name) as f:
            return f.read()
