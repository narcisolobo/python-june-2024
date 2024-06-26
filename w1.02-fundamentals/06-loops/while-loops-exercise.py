import random

"""
=== === WHILE LOOPS EXERCISE === ===
Write a Python program that simulates a guessing game.
The program should generate a random number between 1
and 100, and then ask the user to guess the number. If
the user's guess is higher than the actual number, the
program should print "Too high, try again." If the guess
is lower, the program should print "Too low, try again."
The game should continue until the user correctly
guesses the number.

Example Output:

Guess the number (between 1 and 100): 50
Too high, try again.
Guess the number (between 1 and 100): 30
Too low, try again.
Guess the number (between 1 and 100): 40
Too low, try again.
Guess the number (between 1 and 100): 45
Congratulations! You guessed the number correctly.
"""

target = random.randint(1, 100)

guess = int(input("Guess the number (between 1 and 100): "))

while guess != target:
    if guess < target:
        print(f"{guess} is too low, try again.")
        guess = int(input("Guess again: "))
    else:
        print(f"{guess} is too high, try again.")
        guess = int(input("Guess again: "))

print("Congratulations! You guessed the number correctly.")
