---
title: "Functions In Python"
author: "James Owusu-Appiah"
date: 2022-03-03
description: "Python Functions A function is a piece of code that performs a specific task and only runs when called. It is made up of a set of statements that accomplish a specified function. Parameters are data..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/functions-in-python-9
---
## Python Functions
A function is a piece of code that performs a specific task and only runs when called. It is made up of a set of statements that accomplish a specified function. Parameters are data that can be provided into a function. Arguments can be used to transmit data through a function. Arguments are supplied inside the parenthesis after the function name.

A function can have many arguments, but they should all be separated by commas. The phrases "parameters" and "arguments" can both refer to the same thing: data that is supplied into a function. Functions help a program become more ordered and controllable as it expands in size. It also eliminates duplication and makes the code reusable.

## Types Of Functions
There are 3 main types of functions in python. There 3 main types are:

- **Anonymous functions** are also called *lambda* functions because they are not declared with the standard *def* keyword.
- **User-Defined Functions (UDFs**), are functions that users create to help them out.
- **Built-in functions**, such as print() to print an object to the terminal and others.

## Syntax Of A Function
The principles that define a language's structure are referred to as syntax. Syntax in computer programming refers to the rules that govern the organization of a programming language's symbols, punctuation, and words.

```python
def function_name(parameters):
	"""docstring"""
	statement(s)
```

- The keyword ‘def’ marks the start of the function reader.
- A function name to uniquely identify the function. The same criteria apply to naming functions as they do to naming identifiers in Python.
- Parameters or arguments through which we pass values to a function. They are optional.
- A colon (:) to mark the end of the function header.
- An optional documentation string (docstring) to describe what the function does is provided.
- One or more valid python statements that make up the function body. Statements must have the same indentation level which is usually 4 spaces.
- An optional return statement to return a value from the function.

## Function Call
When you call a function, you're instructing the computer to carry out that set of instructions. A function definition can be placed anywhere in your code; in certain ways, it exists independently of the rest of the code. To call a function in Python, type out its name followed by parentheses ( ).

## Example Of A Function
```python
def power_value(num,pow):
    #function to raise a particular number num to a power pow
    num = int(num)
    pow = int(pow)
    return num**pow

#Taking user input
n = input('Number to find its power: ')
p = input('Number to raise the number to: ')

#Calling the function by passing n as num and p as pow
value = power_value(n,p)

#Printing the value out
print('The final answer is: ', value)
```

```python
>>> Number to find its power: 2
>>> Number to raise the number to: 2
>>> The final answer is: 4
```

- This function aims to raise a particular number *num* to the given power *pow*. The function name is *power_value* and it takes 2 variables; *num* and *pow.*
- The function then converts the inputs which will be input as strings to integer values.
- It then returns the answer that is the number *num* raised to the given power *pow*.

The remaining part of the code from where there is taking of user input. It takes inputs from the user as strings. It then passes them into our *power_value* function and then finally prints the value.

## How A Function Works In A Larger Program
A function is essentially a "chunk" of code that you may reuse instead of writing it out several times. Programmers can use functions to break down or break down an issue into smaller pieces, each of which performs a specific purpose. A larger program that performs a complex task typically comprises a number of functions that conduct specific tasks in order to achieve the program's desired result.
