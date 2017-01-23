""""Calculating with Dictionaries"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))
print(sorted(zip(prices.values(), prices.keys())))

prices_and_name = zip(prices.values(), prices.keys())
print(min(prices_and_name))
prices_and_name = zip(prices.values(), prices.keys())
print(max(prices_and_name))

min(prices, key=lambda k: prices[k])
max(prices, key=lambda K: prices[k])

min_value = prices[min(prices, key=lambda k: prices[k])]
max_value = prices[max(prices, key=lambda K: prices[k])]
