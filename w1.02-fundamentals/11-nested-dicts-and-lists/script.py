from pprint import pprint

"""
=== === NESTED DICTIONARIES & LISTS === ===
Nesting is also allowed in dictionaries. In other words,
dictionaries may contain lists and tuples as well as other
dictionaries. Likewise, lists may contain dictionaries,
tuples, lists, etc. All of these may be many levels deep!
"""

monty_python = [
    {"first_name": "Graham", "last_name": "Chapman"},
    {"first_name": "John", "last_name": "Cleese"},
    {"first_name": "Terry", "last_name": "Gilliam"},
    {"first_name": "Eric", "last_name": "Idle"},
    {"first_name": "Terry", "last_name": "Jones"},
]

# Loop through the list of dictionaries with a nested for loop
# and the .items method

# Add Michael Palin to the list.

# Getting and Setting Values in Nested Dictionaries
# Print "Gilliam".

# Change "John" to "Johnathan".

instrument_brands = {
    "electric_guitars": ["Les Paul", "Fender", "PRS"],
    "banjos": ["Deering", "Gold Tone"],
    "ukuleles": ["Kamaka", "Koaloha", "Kanilea"],
}

# Add another key to the dictionary - "acoustic_guitars".
# Make its value an empty list.

# Add "Martin" and "Taylor" to the acoustic_guitars list.

# Getting and Setting Values in Nested Lists
# Print "Deering".
print(instrument_brands["banjos"][0])
# Change "PRS" to "Paul Reed Smith".
instrument_brands["electric_guitars"][2] = "Paul Reed Smith"
pprint(instrument_brands)

"""
=== === LET'S LOOP! === ===
"""

# Loop through the Monty Python list, printing each key of
# each nested dictionary
for each_actor in monty_python:
    for key in each_actor:
        print(key)

# Loop through the Monty Python list, printing each value of
# each nested dictionary
for each_actor in monty_python:
    for value in each_actor.values():
        print(value)

# Loop through the Monty Python list, printing each key and
# value of each nested dictionary
for each_actor in monty_python:
    output = ""
    for key, value in each_actor.items():
        output += f"{key}: {value}, "
    print(output[0:-2])

# Loop through the instrument_brands dictionary, printing
# the length of each nested list
for item in instrument_brands:
    print(len(instrument_brands[item]))

# Loop through the instrument_brands dictionary, printing
# each value of each nested list
for type in instrument_brands:
    for element in instrument_brands[type]:
        print(element)

# Loop through the instrument_brands dictionary, printing
# the length of each nested list, each key, and each value
for type in instrument_brands:
    print(len(instrument_brands[type]), type)
    for element in instrument_brands[type]:
        print(element)


# Expected output:
"""
3 electric_guitars
Les Paul
Fender
Paul Reed Smith

2 banjos
Deering
Gold Tone

3 ukuleles
Kamaka
Koaloha
Kanilea

2 acoustic_guitars
Martin
Taylor
"""
