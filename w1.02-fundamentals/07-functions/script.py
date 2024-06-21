"""
=== === FUNCTIONS === ===
"""


# Function declaration
def greeting():
    print("Hello!")


# Function invocation
greeting()


# Parameters and arguments
# declaration = parameters
def greet_by_name(name):
    print(f"Hello {name}!")


banana = "Narciso"
# invocation = arguments
greet_by_name(banana)


def greet_with_time(name, time_of_day):
    print(f"Good {time_of_day}, {name}!")


greet_with_time("Fozzie", "morning")


# Returning values
def add(num1, num2):
    return num1 + num2


result = add(2, 2)
result = add(result, 5)
print(result)


print(add(2, 2) + add(2, 2))


# default parameters and named arguments


def greet_with_default(name="whoever", time_of_day="morning"):
    print(f"Good {time_of_day}, {name}!")


greet_with_default()
greet_with_default(time_of_day="morning")


def greet_with_named(name, time_of_day):
    print(f"Good {time_of_day}, {name}!")


# named arguments
# greet_with_named(time_of_day="afternoon", name="Kermit")
