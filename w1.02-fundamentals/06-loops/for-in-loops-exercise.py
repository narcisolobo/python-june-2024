"""
=== === FOR-IN LOOPS EXERCISE === ===
Write a Python program that takes a list of numbers as
input from the user and calculates the sum of all the
numbers using a `for` loop.

Example Output:

Enter the numbers separated by spaces: 10 20 30 40 50
The sum of the numbers is: 150
"""

sum = 0
user_input = input("Enter the numbers separated by spaces:")

nums = user_input.split(" ")

for num in nums:
    sum += int(num)

print(sum)
