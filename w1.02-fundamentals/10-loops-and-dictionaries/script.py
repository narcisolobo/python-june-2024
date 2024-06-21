"""
=== === LOOPS AND DICTIONARIES === ===

Dictionaries are also iterable. When we iterate through a
dictionary, the iterator is each key of the dictionary.
"""

strat = {
    "brand": "Fender",
    "model": "Stratocaster",
    "year": 1977,
    "color": "blue",
    "is_new": False,
}

"""
=== === DICTIONARY METHODS === ===
There are many useful methods we can use with dictionaries.

keys(), values(), items()

.keys() - returns a list of the dictionary's keys.
.values() - returns a list of the dictionary's values.
.items() - returns a list of tuples of the dictionary's key-value pairs.
"""

for key in strat:
    print(strat[key])

for key in strat.keys():
    print(strat[key])

print(strat.values())

for val in strat.values():
    print(val)

print(strat.items())

for key, val in strat.items():
    print(f"key: {key}, value: {val}")
