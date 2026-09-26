---
title: "Functions in Python and Python Functions"
author: "Abdi Tolesa"
date: 2021-10-13
description: "In programming, functions are blocks of code that accomplish a specific computation task. In other words, a set of instructions bundled together to achieve a specific outcome. To do so, a function..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/functions-in-python-and-python-functions
---
In programming, functions are blocks of code that accomplish a specific computation task. In other words, a set of instructions bundled together to achieve a specific outcome. To do so, a function has to be called from somewhere in accordance that complies to its definition, keeping its protocol.

Some of the advantages organizing a program into modular functions are:

• Creating a new function gives you an opportunity to name a group of statements, which makes your program easier to read, understand, and debug.

• Functions can make a program smaller by eliminating repetitive code. Later, if you make a change, you only have to make it in one place.

• Dividing a long program into functions allows you to debug the parts one at a time and then assemble them into a working whole.

• Well-designed functions are often useful for many programs. Once you write and debug one, you can reuse it.

A function may have a set of arguments and not at all. Arguments are just inputs a function takes in and use them to achieve its task. As well, a function may have a return value as an output or just return no value depending on its objective.

There are three types of functions in Python. Built-in functions, User Defined Functions and Anonymous functions.

Built-in functions are those that are shipped with the Python interpreter, the software that executes Python code. These are also called helper functions.

User Defined Functions on the other hand are functions that are written by developers to achieve something, that could span many lines of code. The are declared with the standard def keyword.

The last type of functions are also called Lambda Functions. Lambda functions are differentiated from the regular User Defined Functions in a few ways. Lambda functions can only have one expression. Consider the following example of lambda functions, that multiplies two numbers.

```python
x = lambda a, b : a * b

print(x(5,6)) # prints 30
```

To better illustrate a typical Python User Defined Function, lets write a simple function that takes in a set of arguments, does some computation and return an output as a result.

Some helpful rules to write a Python function include:

- Function blocks begin with the keyword **def** followed by the function name and parentheses ( ( ) ).
- Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
- The first statement of a function can be an optional statement - the documentation string of the function or *docstring*.
- The code block within every function starts with a colon (:) and is indented.
- The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.

Having the rules in place, lets go ahead and write a Python function that counts the number of times each item is present in a given list and return the result as a dictionary of key:value.

```python
def count_items(listing):
    d={}
    for i in range(len(listing)-1):
        x=listing[i]
        c=0
        for j in range(i,len(listing)):
            if listing[j]==listing[i]:
                c=c+1
        count=dict({x:c})
        if x not in d.keys():
            d.update(count)
    return d

languages =['Python','Java','PHP','Javascript','Node','Python','Java','Python','PHP','Javascript']
print (count_items(languages))
# result: {'Python': 3, 'Java': 2, 'PHP': 2, 'Javascript': 2, 'Node': 1}
```

This function takes in one argument, a list of items. After that it loops over the list and increment the count of each item whenever it is encountered in a given iteration.

There are some built-in Python functions and methods used in the function like range(), len(), dict() and update(). We can refer to <https://docs.python.org> to learn what each function does and how to use them.

range() - returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

len() - returns the length of a list, string, dictionary, or any other iterable data format in Python.

dict() - The *dict() function* creates a dictionary. A dictionary is a collection which is unordered, changeable and indexed.

update() - The *update()* method takes either a dictionary or an iterable object of key/value pairs (generally tuples).

The function we just wrote is not a complex one but can be a good example of a real world problem solving exercise with Python. Practically, more complex functions that take in multiple arguments can be written to solve different problems. The algorithm behind each function is what the developer creates and implement with the programming language so that it could be reused in other pieces of code.
