---
title: "Python concept: Functions"
author: "Blessing Oludele"
date: 2022-05-02
description: "A function in simple terms is a collection of code that performs a single function.How to know when you need a function:Never repeat yourself: whenever you find yourself writing the same piece of..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-concept-functions
---
A function in simple terms is a collection of code that performs a single function.

**How to know when you need a function:**

Never repeat yourself: whenever you find yourself writing the same piece of code again and again, you probably should use a function.

**Rule of the thumb for functions:**

Do only one thing: A function should ONLY do one thing. If you have a function calculating several things and combining them, you probably should split it up into several functions. We can have a function that only displays one thing (It's still performing a function)

**In-built functions:**

There are several inbuilt function in python, some of which we are already familiar with. e.g. sum(), max(), upper(), lower(), strip(). etc. From the names of this functions we can easily imply the purpose. If we are confused on the purpose of a function we can use help() in our shell, using the function as an argument.

**Creating your own functions:**

In creating your functions, you use the def keyword followed by the function name and a bracket which may or may not contain arguments and lastly a column... this first line is called the function headline.

after the headline you can include a docstring which basically describes what the function does. This is written between three semicolons.

the code implementing the function is written below this in an indented block. the indented block is also used to specify the scope of the function.

A function can include return values or not.

A simple function snippet to greet a user is displayed below:
