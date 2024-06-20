"""
=== === LOOPS === ===
"""

# Looping over lists and strings
superheroes = [
    "Spider-Man",
    "Captain Marvel",
    "Batman",
    "Wonder Woman",
    "Thor",
    "Black Widow",
]

nums = [1, 2, 3, 4, 5, 6]

# for-in loops

# using range()
for i in range(1, len(superheroes)):
    print(superheroes[i])

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        nums[i] = "even"

print(nums)

# range accepts arguments for start, stop, and step

# without range()
for hero in superheroes:
    print(hero)

# while loops (like a deconstructed for loop)
i = 0
while i < len(superheroes):
    print(superheroes[i])
    i += 1
