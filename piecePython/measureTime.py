from timeit import timeit

print(timeit('"c">="a" and "c"<="z"',number=10000000))
print(timeit('"c".isalpha()',number=10000000))
