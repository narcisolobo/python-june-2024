"""
Exercise: Phone Book
Write a Python program to create a simple phone book. The program
should allow users to perform the following operations:

- Add a new contact to the phone book.
- Display the phone number of a given contact.
- List all contacts in the phone book.

To implement this, you can use a dictionary where the keys are the
names of the contacts, and the values are their corresponding phone
numbers.

Expected output:

Added Alice with phone number 1234567890 to the phone book.
Added Bob with phone number 9876543210 to the phone book.
The phone number of Alice is 1234567890.
Charlie is not found in the phone book.
Contacts in the phone book:
Alice: 1234567890
Bob: 9876543210
"""


# Function to add a new contact to the phone book
def add_contact(phone_book, name, phone_number):
    pass


# Function to display the phone number of a given contact
def display_phone_number(phone_book, name):
    pass


# Function to list all contacts in the phone book
def list_contacts(phone_book):
    pass


# Main program
my_phone_book = {}

add_contact(my_phone_book, "Alice", "1234567890")
add_contact(my_phone_book, "Bob", "9876543210")

display_phone_number(my_phone_book, "Alice")
display_phone_number(my_phone_book, "Charlie")

list_contacts(my_phone_book)
