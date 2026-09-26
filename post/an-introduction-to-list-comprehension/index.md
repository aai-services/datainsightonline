---
title: "An introduction to List Comprehension"
author: "bismark boateng"
date: 2021-10-07
description: "python is eminent for encouraging developers and Data Scientist write efficient, easy to understand code and a simple to read code as well List comprehensions are used for creating new lists from..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/an-introduction-to-list-comprehension
---
python is eminent for encouraging developers and Data Scientist write efficient, easy to understand code and a simple to read code as well

List comprehensions are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc. A list comprehension consists of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element.

syntax:

*newList* **=[** *expression(element)* **for** *element* **in** *oldList* **if** *condition* **]**

**Advantages of List Comprehension**

1. Require fewer lines of code
2. Transforms iterative statement into a formula
3. More time efficient and space efficient than loops

**Iterating through a String using List comprehensions**

```python
h_letters = [letter for letter in "letter"]
print(h_letters)
```

When we run the program, the output will be:

```python
['l','e','t','t','e','r']
```

in the above example, a new list is assigned to variable h_letters, and list contains the items of the iterable string 'letters'

we type the print() function to call the output
