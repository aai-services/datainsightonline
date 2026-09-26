---
title: "LIST COMPREHENSION"
author: "Blessing Oluwadaara"
date: 2021-10-17
description: "Python is one of the most widely used programming languages in the world. Its widespread popularity can be attributed to its simple and easy-to-understand code. If you’re familiar with the syntax..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/list-comprehension-2
---
Python is one of the most widely used programming languages in the world. Its widespread popularity can be attributed to its simple and easy-to-understand code. If you’re familiar with the syntax, writing code in Python is a breeze. Its list comprehension feature is one of its key attractions. With just one line of code, you can perform Python comprehension for lists.

Python provides several methods for creating lists. The list comprehension feature is one of the most effective of these methods. It allows you to create lists with just one line of code. It can be used to create new lists from other iterable elements such as arrays, strings, tuples, lists, and so on. It consists of brackets containing the expression. To iterate over all of the elements, the system uses the for loop to execute the expression for each one.

When doing data science, you might find yourself wanting to read lists of lists, filtering column names, removing vowels from a list, or flattening a matrix. You can easily use a lambda function or a for a loop; As you well know, there are multiple ways to go about this. One other way to do this is by using list comprehensions.

```python
list comprehension = [output expression for variable in input expression]
outcome = [x**2 for x in range(1,11)]
#x**2 is the output expression
#x is the variable
#range(1,11) is the input sequence
```

Every list comprehension in Python includes three elements:

1. **expression** is the member itself, a call to a method, or any other valid expression that returns a value. In the example above, the expression x\*\*2 is the square of the member value.
2. **member** is the object or value in the list or iterable. In the example above, the member value is x.
3. **iterable** is a list, set, sequence, generator, or any other object that can return its elements one at a time. In the example above, the iterable is range(1,11).
