---
title: "List in python"
author: "Nehal Sherif"
date: 2021-10-07
description: "How to create a list?In Python programming, a list is created by placing all the items(elements) inside square brackets [], separated by commas.It can have any number of items and they may be of..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/list-in-python
---
## How to create a list?

In Python programming, a list is created by placing all the items

(elements) inside square brackets [], separated by commas.

It can have any number of items and they may be of different types (integer, float, string etc.).

```python
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

## Access List Elements

There are various ways in which we can access the elements of a list.

### List Index

We can use the index operator [] to access an item in a list. In Python, indices start at 0. So, a list having 5 elements will have an index from 0 to 4.

Trying to access indexes other than these will raise an IndexError. The index must be an integer. We can't use float or other types, this will result in TypeError.

Nested lists are accessed using nested indexing.

```python
# List indexing

my_list = ['p', 'r', 'o', 'b', 'e']

print(my_list[0])  # pprint(my_list[2])  # oprint(my_list[4]) # e# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexingprint(n_list[0][1])

print(n_list[1][3])
```

output:

```python
p
o
e
a
5
```

**Negative indexing**

Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.

```python
# Negative indexing in lists
my_list = ['p','r','o','b','e']

print(my_list[-1])

print(my_list[-5])
```

## output:

```python
e
p
```

## Add/Change List Elements

Lists are mutable, meaning their elements can be changed unlike [string](https://www.programiz.com/python-programming/string) or [tuple](https://www.programiz.com/python-programming/tuple).

We can use the assignment operator = to change an item or a range of items.

```python
# Correcting mistake values in a list
odd = [2, 4, 6, 8]

# change the 1st item
odd[0] = 1

print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]
print(odd)
```

output:

```python
[1, 4, 6, 8]
[1, 3, 5, 7]
```

## Delete/Remove List Elements

We can delete one or more items from a list using the keyword del. It can even delete the list entirely.

```python
# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]

print(my_list)

# delete multiple items
del my_list[1:5]

print(my_list)

# delete entire list
del my_list

# Error: List not defined
print(my_list)
```

output:

```python
['p', 'r', 'b', 'l', 'e', 'm']
['p', 'm']
```
