---
title: "List comprehension in Python"
author: "Gaurab Awal"
date: 2021-10-06
description: "List comprehension is the method to create a new list from the value of an existing list. Generally, list comprehension is more compact and faster than normal functions and loops for creating lists..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/list-comprehension-in-python
---
List comprehension is the method to create a new list from the value of an existing list. Generally, list comprehension is more compact and faster than normal functions and loops for creating lists. List comprehension always comes with a for-loop wrapped inside the square bracket.

#### Syntax of list_comprehension:
new_list = [*expression* for *item* in *iterable*]

We can use this syntax with an example so that we have a clear idea about how to use list comprehension.

#### Example:
a_list = [1,2,3,4,5]

if we need to get the square of the items in a list then,

```python
	new_list = [item**2 for item in a_list]
```

We have easily created a new_list with output [1, 4, 9, 16, 25], the square of values of a_list. If list comprehension is not available in python then we have to write multiple lines of code which is written below.

```python
new_list = []
a_list = [1,2,3,4,5]
for item in a_list:
	new_list.append(item**2)
```

#### List comprehension with if condition
**Syntax:**

new_list = [*expression* for *item* in *iterable* if *condition* == True]

**Example:**

```python
		new_list  = [item for item in a_list if item%2 ==0]
```

This code will create a list of even numbers only from values of a_list, output as [2, 4]. We can use if condition with for loop in a single line.

**Advantages of List Comprehension:**

1. Efficient in time and space than loops.
2. Fewer lines of code.

**When not to use List Comprehension:**

List comprehensions are useful and can help you write elegant code that’s easy to read and debug, but they’re not the right choice for all circumstances. They might make your code run more slowly or use more memory. If your code is less performant or harder to understand, then it’s probably better to choose an alternative.
