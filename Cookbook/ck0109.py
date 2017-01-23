"""Finding Commonalities in Two Dictionaries"""

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# Find key in common
a.keys() & b.keys()

# Find key in a that are not in b
a.keys() - b.keys()

# Find (key,value) pairs in common
a.items() & b.items()

# Make a new dictionary with certain key removed
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
