"""在字符串中处理html 和 xml """

s = 'Elements are written as "<tag>text</tag>".'
import html

print(s)
print(html.escape(s))

# disable escaping of equotes
print(html.escape(s, quote=False))

s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))
