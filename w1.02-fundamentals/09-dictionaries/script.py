"""
=== === DICTIONARIES === ===

Python dictionaries are collection datatypes. We can
store a series of key-value pairs in these collections.
Use curly braces at the bookends, separate each pair
with a comma, use a colon between keys and values, and
surround the key name with quotation marks.
"""

strat = {"brand": "Fender", "model": "Stratocaster", "year": 1977, "is_new": False}

# Accessing/getting values with bracket notation
key_name = "brand"
print(strat[key_name])

# We can access values in a dictionary by their
# key names. Use bracket notation with quotes.

"""
=== === DICTIONARY MANIPULATION === ===
"""
# Bracket notation

# Changing an existing value
strat["year"] = 1968
print(strat)

# Adding a new key-value pair
strat["color"] = "blue"
print(strat)

# Removing a key-value pair with pop() and del
""" strat.pop("year")
print(strat)"""

del strat["color"]
print(strat)

# Testing for an existing key
# in, not in
if "color" in strat:
    print(strat["color"])
else:
    print("color key not in strat")

# We can use the 'in' and 'not in' keywords to check if a key
# name exists in a dictionary.
