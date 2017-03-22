"""读写压缩文件"""

import bz2
import gzip

with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

with bz2.open('somefile.bz', 'rt') as f:
    text = f.read()

with gzip.open('somefile,gz', 'wt') as f:
    f.write(text)

with bz2.open('somefile.bz', 'wt') as f:
    f.write(text)

with gzip.open('somefile.gz', 'wt', compresslevel=9) as f:
    f.write(text)
