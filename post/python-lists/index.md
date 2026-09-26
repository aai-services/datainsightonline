---
title: "Python Lists"
author: "tasnim assali"
date: 2021-09-29
description: "Python offers a range of compound data types often referred to as sequences. list is one of the most frequently used and very versatile data types used in Python.How to create a list?In Python..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-lists
---
Python offers a range of compound data types often referred to as sequences. list is one of the most frequently used and very versatile data types used in Python.

### How to create a list?

In Python programming, a list is created by placing all the items (elements) inside square brackets [], separated by commas.

It can have any number of items and they may be of different types (integer, float, string etc.).

```python
#Creat list
# empty list
my_list = []
# list of integers
my_list = [1, 2, 3]
# list with mixed data types
my_list = [1, "Hello", 3.4]
```

A list can also have another list as an item. This is called a nested list.

```python
# nested list
my_list = ["mouse", [8, 4, 6], ['a']]
```

### Access List Elements

There are various ways in which we can access the elements of a list.

### List Index

### We can use the index operator [] to access an item in a list. In Python, indices start at 0. So, a list having 5 elements will have an index from 0 to 4. Add/Change List Elements

Lists are mutable, meaning their elements can be changed unlike [string](https://www.programiz.com/python-programming/string) or [tuple](https://www.programiz.com/python-programming/tuple). We can use the assignment operator = to change an item or a range of items.

```python
# Correcting mistake values in a list
odd = [2, 4, 6, 8]

# change the 1st item
odd[0] = 1print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]

print(odd)
```

We can add one item to a list using the append() method or add several items using extend() method.

```python
# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)

print(odd)

odd.extend([9, 11, 13])

print(odd)
```

We can also use + operator to combine two lists. This is also called concatenation.

The \* operator repeats a list for the given number of times.

```python
# Concatenating and repeating lists
odd = [1, 3, 5]

print(odd + [9, 7, 5])

print(["re"] * 3)
```

### Delete/Remove List Elements

We can delete one or more items from a list using the keyword del. It can even delete the list entirely.

```python
# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one itemdel my_list[2]

print(my_list)

# delete multiple itemsdel my_list[1:5]

print(my_list)

# delete entire listdel my_list

# Error: List not definedprint(my_list)
```

We can use remove() method to remove the given item or pop() method to remove an item at the given index.

The pop() method removes and returns the last item if the index is not provided. This helps us implement lists as stacks (first in, last out data structure).

We can also use the clear() method to empty a list.
