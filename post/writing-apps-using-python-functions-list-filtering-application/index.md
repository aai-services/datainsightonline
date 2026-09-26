---
title: "Writing Apps Using Python Functions: List Filtering Application"
author: "Ochuole Ogbeche"
date: 2022-01-21
description: "Python Functions: In Python, a function is a piece of reusable code. It eliminates the need to write code repetitively, thereby following the PEP8 standard of DRY (Don’t Repeat Yourself). A function..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/writing-apps-using-python-functions-list-filtering-application
---
**Python Functions**:
In Python, a function is a piece of reusable code. It eliminates the need to write code repetitively, thereby following the PEP8 standard of DRY (Don’t Repeat Yourself).
A function in python is written using the def keyword followed by the function name, a bracket containing the argument(s) for the function, and ending in a colon. A function depends on indentions, therefore, the block of code, that is the code to be executed, is indented.
Python functions have to be called with parameters that equal the arguments in the function bracket before the function can run. The function is usually called at the end of all the blocks of code needed by the function.

**List Filter App**

The function starts with the def keyword, the name of the function(list_filter), and a bracket containing the argument to be supplied when calling the function, which is a keyword argument (list = []). The pass keyword is supplied into the function to enable it to run before the parameter supplied is validated.

def list_filter(list=[]):

pass

The first code block for this function is an if…else block which starts with a while True statement, ensuring that this code block runs only when the parameters remain true. The if…else block which simply verifies if the list size is greater than zero, and if the list size is equal to zero prompts the user to enter an integer greater than zero by outputting a statement that the list must contain numbers. If the condition is met, then the else block that constructs the list based on the list size inputted plus one to include the end value of the list constructs the list and outputs it. This created list is supplied to the function as a parameter when it is called at the end of the code blocks. This block also contains a try…except block which verifies the inputted list size as an integer above zero, raises an error if a ValueError is caught, and displays a message for the user to enter an integer.

while True:

list_size = (input("Enter number of items in list...\n"))

if int(list_size) == 0:

print("List must contain Numbers")

else:

print("Constructing List...")

full_list = list(range(int(list_size) + 1))

print("List contains: ", full_list)

try:

val = int(list_size)

print("List size is: ", val)

break;

except ValueError:

print("This is not a Number.\nPlease enter a valid Number")

The second code block, and if…elif…else block, starts by asking the user for input of either “E” for the even numbers and “O” for the odd numbers to specify which type of numbers the user needs filtering out. The if block runs if the user opts to filter even numbers from the list, and contains a block of codes where the corresponding number on the list which is signified by “x” divided by 2 is equal to zero is outputted until the list is completely iterated over, and then the corresponding values are outputted. The elif block runs if the user opts to filter odd numbers from the list, and contains a block of codes where the corresponding number on the list which is signified by “x” divided by 2 is equal to one is outputted until the list is completely iterated over, and then the corresponding values outputted. The else block is executed when the option the user chooses is neither “E” nor “O”, and prompts the user to enter a value of either of the two.

numbers_to_filter = input("Enter type of number to select...\n 'E' for Even Number and 'O' for Odd Number \n").capitalize()

if numbers_to_filter == "E":

print("Sorting Even Numbers...")

print("The Even numbers in the list are: ")

for x in full_list:

if x % 2 == 0:

print(x)

elif numbers_to_filter == "O":

print("Sorting Odd Numbers...")

print("The Odd numbers in the list are: ")

for x in full_list:

if x % 2 == 1:

print(x)

else:

print("Invalid Option")

print("Enter 'E' or 'O'")

The function is called at the end, with the created list created as the parameter.

list_filter(full_list)
