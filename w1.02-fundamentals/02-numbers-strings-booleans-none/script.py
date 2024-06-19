import math

"""
PRIMITIVE (SIMPLE) DATATYPES
- Strings (str)
- Integers (int)
- Floating Point Numbers (float)
- Booleans (bool)
- None (NoneType)
"""

"""
=== === Strings === ===
Strings represent sequences of characters.
"""

# String creation:

# Literal assignment
my_name = "Narciso"

# Constructor function (type casting)
another_name = str("Kermit")

# Print function
print(another_name)

# printing with commas
print(my_name, another_name)

# Type function
print(type(my_name))

# Concatenation
my_last_name = "Lobo"
my_full_name = my_name + " " + my_last_name
print(my_full_name)

# f-string (string interpolation)
print(f"{my_name} {my_last_name}")

# TypeError
# Fix
print("hello" + str(42))
print(f"hello {42}")

# String Methods
# `split()` splits a string based on a separator
hello = "Greetings humans!"
hello_split = hello.split()
print(hello_split)

# upper, lower, title
phrase = "The answer to the question of life, the universe and everything is 42."
print(phrase.upper())
print(phrase.lower())
print(phrase.title())

# length
print(len(phrase))

# strip
string_with_whitespace = "     hello         "
print(string_with_whitespace)
print(string_with_whitespace.strip())

# string indices, index ranges
# slicing with index ranges
# negative indices
print(phrase[50])
print(phrase[5:12])
print(phrase[-2])
print(phrase[60:-2])

# the .format method
fav_food = "spaghetti"
fav_color = "green"
print("My favorite food is {} and my favorite color is {}.".format(fav_food, fav_color))

# %-Formatting
number = 42
print("My favorite food is %s." % fav_food)

team_info = {"team": "Chicago", "player": "Caleb Williams", "number": 18}

print(
    "My team is %(team)s and my favorite player is %(player)s. His number is %(number)d."
    % team_info
)

# Explore more string methods!
# https://www.w3schools.com/python/python_strings_methods.asp

"""
=== === INTEGERS AND FLOATS === ===
Integers represent whole numbers. Floats represent
decimal numbers.
"""

# Integer literal assignment

# Constructor function (casting)

# Float literal assignment

# Constructor function (casting)

# Arithmetic operations
# +, -, *, /, **, //

# +=, -=, *=, /= assignment operators

# Built-in functions for numbers

# abs, round

# Math module

# sqrt, ceil, floor

"""
=== === BOOLEANS === ===
Booleans represent the value of True or False.
"""

# Literal assignment

# Constructor function (casting)

"""
=== === NONE === ===
None represents the absence of a value.
like the javascript null
"""

# None literal assignment

# Why use None?
