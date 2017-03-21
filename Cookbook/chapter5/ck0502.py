"""打印输出至文件中"""
# 文件必须是以文本模式打开
with open('test.txt', 'wt') as f:
    print('Hello World!', file=f)
