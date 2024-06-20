"""
=== === CONDITIONALS EXERCISE === ===
Write a Python program that takes an integer input
from the user and checks whether it is positive,
negative, or zero. Use conditional statements
(`if`, `elif`, `else`) to implement this logic.

Example Output:

Enter a number: 5
5 is a positive number.

Enter a number: -3
-3 is a negative number.

Enter a number: 0
0 is neither positive nor negative.
"""

num = input("Enter a number: ")

if not num.isnumeric():
    print(f"{num} is not a number")
    exit(1)

""" try:
    num = int(num)
except:
    print(f"{num} is not a number")
    exit(1) """

if num < 0:
    print(f"{num} is a negative number.")
elif num == 0:
    print(f"{num} is neither positive nor negative.")
else:
    print(f"{num} is a positive number.")
