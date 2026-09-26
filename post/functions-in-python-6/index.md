---
title: "Functions in Python"
author: "Gehad Hisham"
date: 2022-02-04
description: "Python is a general-purpose language so it is not just for data science. It can be used for web development, mobile application, game development, et cetera. I will give a tutorial on some of these..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/functions-in-python-6
---
Python is a general-purpose language so it is not just for data science. It can be used for web development, mobile application, game development, et cetera.
I will give a tutorial on some of these concepts that, in my opinion, are very important for dealing with data using python.

let’s create these concepts and see how they can be applied.

## Functions
Function, a fundamental building block of modules in any programming language, are single self-contained blocks of code that ideally perform a single task.

Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.
Furthermore, it avoids repetition and makes the code reusable.

Here’s a list of topics we will discuss on functions:

1. Defining function in Python,
2. How to call a function,
3. Example of a function,
4. How to call a function in python?

**Defining function in Python**

Let's start by writing the Syntax of Function

```python
def function_name(parameters):
    """docstring"""
    statement(s)
```

**Let's break what we wrote above.**

Above shown is a function definition that consists of the following components.

- Keyword def that marks the start of the function header.
- A function name to uniquely identify the function. Function naming follows the same rules of writing identifiers in Python.
- Parameters (arguments) through which we pass values to a function. They are optional.
- A colon (:) to mark the end of the function header.
- Optional documentation string (docstring) to describe what the function does.
- One or more valid python statements that make up the function body. Statements must have the same indentation level (usually 4 spaces).
- An optional return statement to return a value from the function.

**Example of a function**

```python
def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")
```

**How to call a function in python?**

To call a function we simply type the function name with appropriate parameters.
Once we have defined a function, we can call it from another function, program, or even the Python prompt.

```python
greet('Gehad')

--> Hello, Gehad. Good morning!
```

**Note:** In python, the function definition should always be present before the function call, Otherwise, we will get an error.

```python
# function call
greet2('Gehad')
​
# function definition
def greet2(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")
```

**-------------------------------------------------------------------------------------------------**

**NameError** Traceback (most recent call last) **<ipython-input-4-f1f5f188df8c>** in <module> 1 **# function call****----> 2**greet2**(****'Gehad'****)** 3 4 **# function definition** 5 **def** greet2**(**name**):****NameError**: name 'greet2' is not defined

**Types of Functions**

Basically, we can divide functions into the following two types:

1. Built-in functions - Functions that are built into Python.
2. User-defined functions - Functions defined by the users themselves.

Thank you.

​
