"""
=== === LISTS === ===
In Python, arrays are called lists.

Lists are ordered and changeable.

Lists allow duplicate values.
"""

# List creation
colors = ["red", "blue", "green"]
me = ["Narciso", 53, True]

# List indices
"""
Lists have indices just like arrays have indices in
JavaScript. They are zero-indexed as well.
"""
print(colors[1])

# List negative indices
"""
Python supports negative indices. A -1 index will refer
to the last element in a list.
"""
print(colors[-2])

# Common list methods
"""
There are many useful methods we can use with lists.
"""

# length
"""
Pass a list to the len() method to return the number of
elements in the list.
"""
print(len(colors))

# append, remove, pop
"""
append() - adds an element to the end of a list.
remove() - removes the specified element from a list.
pop() - removes the element at the specified position
"""
colors.append("yellow")
print(colors)
# colors.remove("red")
print(colors)
# result = colors.pop(1)
# print(result)

# sort, reverse
"""
The sort() method sorts a list in ascending order in-place.
The reverse() method reverses a list.
"""
colors.sort()
print(colors)
nums = [5, 3, 2, 4, 2, 8]
nums.sort()
print(nums)
nums.reverse()
print(nums)

# Explore more list methods!
# https://www.w3schools.com/python/python_lists_methods.asp
