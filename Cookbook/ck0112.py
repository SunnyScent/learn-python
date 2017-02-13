"""Determining the Most Frequently Occurring Items in s Sequence """

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
word_counts.update(morewords)
top_three = word_counts.most_common(3)
print(top_three)

a = Counter(words)
b = Counter(morewords)
print(a)
print(b)
print(a + b)
print(a - b)
