"""多行匹配模式"""
import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/*this is a comment*/'
text2 = '''/*this is a
        multiline comment */
        '''

print(comment.findall(text1))
print(comment.findall(text2))

##re.compile() 函数接受一个标志参数叫re.DOTALL ，在这里非常有用。它可以让
##正则表达式中的点(.) 匹配包括换行符在内的任意字符

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))
