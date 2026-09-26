---
title: "Functions in Python"
author: "Teresa Rady"
date: 2021-10-03
description: "DefinitionThe concept of functions in Python is the similar as in Algebra, where we define a certain operation to be performed on a variable. This variable can hold any value or range of values. For..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/functions-in-python-2
---
## Definition
The concept of functions in Python is the similar as in Algebra, where we define a certain operation to be performed on a variable. This variable can hold any value or range of values.

For example *f(x) = 2x + 1* and x can have all sort of values.

The same concept applies in Python but has a different way of expression i.e. syntax.

So function is: a block of code that perform a certain operation and can be reused.

There are two types of functions in python:

1) Built-in functions: those that come with the language like print() function.

2) User-defined functions : these are the topic of this tutorial.

## Syntax
Let's take a look at an example for a function that doubles any number.

```python
def double_num(number):
    return number * 2
```

To define a function we start with the keyword def followed by the name of the function which in this case is 'double_num'. Between the brackets is an argument which is a place holder for the input values to the function.

The second line is called the "body of the function" and it is defined by the keyword return. The function doesn't accept anything after the word return, unless it is indented to be outside the function.

Now let's see this function working or in programming "calling the function".

```python
a = 889
double_num(a)
1778
```

Calling the function on value of a and It works!

We can also store the output of the function:

```python
out_fun = double_num(a)
print(out_fun)
1778
```

Now this function is defined and stored in your code and you can call it over and over when needed.

Now Let's call the same function on a different type of data, e.g. a string.

```python
double_num('data ')
'data data '
```

The output indicates that functions can be performed on a string. Here as we know from before multiplying the string equals repeating it.

## Scope
The argument "number" in the double_num function only have meaning inside the function that they are part of. So If we defined a variable named number later in the code, that doesn't affect or be affected by what is under the function.

```python
number = 7
double_num(9)
18
```

Now let's look at an example of how functions can be reused with different user inputs.

```python
name_input = input('Name: ')
def greeter(name):
    return 'Hello ' + name + " I wanna play a game!"
print(greeter(name_input))
```

This is an example of a simple greeting program which can be used as a friendly prank!

The first line of code prompts the user to type their name which is saved as name_input. After that a function is defined to add the scary greeting from Saw movie series to the variable name.

The last step is to call the function on the result of the input by specifying the variable as name_input.

The result looks like this:

```python
Name: Amanda
Hello Amanda I wanna play a game!
```
