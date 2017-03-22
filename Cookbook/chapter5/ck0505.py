"""文件不存在才能写入"""

with open('somefile', 'wt') as f:
    f.write('Hello\n')

# with open('somefile', 'xt') as f:
#     f.write('Hwllo\n')

import os

if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write()
else:
    print('File already exists')
