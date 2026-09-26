---
title: "Python's Functions"
author: "Amr Mohamed Salama"
date: 2022-02-04
description: "Why use a Function?Functions are a convenient way to group our code into reusable blocks. A function contains a sequence of steps that can be performed repeatedly throughout a program without having..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-s-functions
---
**Why use a Function?**

Functions are a convenient way to group our code into reusable blocks. A function contains a sequence of steps that can be performed repeatedly throughout a program without having to repeat the process of writing the same code again

**Function Key Components**

There are some key components we want to note here:

- The def keyword indicates the beginning of a function (also known as a function header). The function header is followed by a name in **snake_case format** that describes the task the function performs. It’s best practice to give your functions a descriptive yet concise name.
- Following the function name is a pair of parenthesis ( ) that can hold input values known as arguments.
- A colon: to mark the end of the function header.
- Lastly, we have one or more valid python statements that make up the function body.

**Function Types**

There are three types of functions in Python:

**1.** **Built-in functions:**

such as help() to ask for help, min() to get the minimum value,
 print() to print an object to the terminal.

**2.** **User-Defined Functions (UDFs):**

which are functions that users create to help them out

**3.** **Anonymous Functions / Lambda Function:**

which are also called lambda functions because they are not
 declared with the standard (**def)** keyword.

**Calling a Function**

The process of executing the code inside the body of a function is known as calling it (This is also known as “executing a function”). To call a function in Python, type out its name followed by parentheses ( ).

**Function Arguments**

arguments are the things that are given to any function or method call, while the function or method code refers to the arguments by their parameter names.

1. *Positional arguments*:

arguments that can be called by their position in the function definition.

```python
def func(name, job):
    print(name, 'is a', job)

func('Bob', 'developer')
# Prints Bob is a developer
```

*2.* *Keyword arguments*:

arguments that can be called by their name.

```python
# Keyword arguments can be put in any order
def func(name, job):
    print(name, 'is a', job)
func(name='Bob', job='developer')
# Prints Bob is a developer
func(job='developer', name='Bob')
# Prints Bob is a developer
```

*3.* *Default arguments*:

arguments that are given default values.

```python
# Set default value 'developer' to a 'job' parameter
def func(name, job='developer'):
    print(name, 'is a', job)
func('Bob', 'manager')
# Prints Bob is a manager
func('Bob')
# Prints Bob is a developer
```

4. *Variable Length Positional Arguments (\*args)*:

arguments that allow the function to take an unlimited number of *positional* arguments

```python
def print_arguments(*args):
    print(args)
print_arguments(1, 54, 60, 8, 98, 12)
# Prints (1, 54, 60, 8, 98, 12)
```

*5.* *Variable Length Keyword Arguments (\*\*kwargs):*

arguments that allow the function to take an unlimited number of *keyword* arguments

```python
def print_arguments(**kwargs):
    print(kwargs)
print_arguments(name='Bob', age=25, job='dev')
# Prints {'name': 'Bob', 'age': 25, 'job': 'dev'}
```
