# Python Dictionaries
A Python dictionary is a versatile data structure that allows you to store and manage data as key-value pairs. Here are some key points to understand:

1. **Key-Value Pairs**: Each item in a dictionary has a key and a corresponding value. Keys are unique identifiers, while values are the data associated with these keys.
2. **Syntax**: Dictionaries are defined using curly braces `{}`. For example:

    ```py
    strat = {
        "brand": "Fender",
        "model": "Stratocaster",
        "year": 1977,
        "is_new": False,
    }
    ```
    In this example, `"brand"`, `"model"`, `"year"`, and `"is_new"` are keys.
    
    `"Fender"`, `"Stratocaster"`, `1977`, and `False` are their respective values.

## Accessing values with bracket notation

We can access values in a dictionary by their key names. Use bracket notation with quotes
around the key name.

```py
print(strat["year"])  # 1977
```

## Dictionary Manipulation
Dictionaries are mutable, meaning we can change, add, or remove items.

For example:
```py
# Update existing key
strat["year"] = 1968

# Add new key-value pair
strat["color"] = "blue"

# Remove key-value pair
del strat["year"]
```

## Dictionary methods
Here are a few useful methods we can use with dictionaries.

### keys, values, items

- `.keys()` - returns an array of the dictionary's keys.
- `.values()` - returns an array of the dictionary's values.
- `.items()` - returns an array of tuples of the dictionary's key-value pairs.

```py
print(strat.keys())  # dict_keys(['brand', 'model', 'year', 'color', 'is_new'])
print(strat.values())  # dict_values(['Fender', 'Stratocaster', 1977, 'blue', False])
print(strat.items())
# dict_items([('brand', 'Fender'), ('model', 'Stratocaster'), ('year', 1977), ('color', 'blue'), ('is_new', False)])
```

### in, not in

We can use the 'in' and 'not in' keywords to check if a key
name exists in a dictionary.

```py
if "color" in strat:
    print(strat["color"])
else:
    print("key does not exist")

if "banana" not in strat:
    print("key does not exist")
```

[Explore more dictionary methods!](https://www.w3schools.com/python/python_ref_dictionary.asp)
