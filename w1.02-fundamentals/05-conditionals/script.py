"""
=== === CONDITIONALS === ===
"""

# Example:
temperature = 0

if temperature > 80:
    print("It's a hot day!")
elif temperature > 60:
    print("It's a warm day!")
elif temperature > 40:
    print("It's a cool day!")
else:
    print("It's a cold day!")


# Nested conditionals:
temperature = 70
is_raining = True

if temperature > 60:
    if is_raining:
        print("It's a warm and rainy day!")
    else:
        print("It's a warm and sunny day!")
else:
    print("It's not warm today.")


# Predict the output:
is_sunny = True
temperature = 45
is_raining = False
what_to_bring = "I should bring: "

if is_sunny:
    what_to_bring += "sunglasses, "
if temperature < 50:
    what_to_bring += "a coat, "
if is_raining:
    what_to_bring += "an umbrella, "
what_to_bring += "and a smile!"

print(what_to_bring)
