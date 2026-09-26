---
title: "Python data types"
author: "Nehal Sherif"
date: 2021-10-07
description: "Data types in PythonEvery value in Python has a datatype. Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-data-types
---
## Data types in Python

Every value in Python has a datatype. Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.

There are various data types in Python. Some of the important types are listed below.

## Python Numbers

Integers, floating point numbers and complex numbers fall under python numbers category. They are defined as int, float and complex classes in Python.

We can use the type() function to know which class a variable or a value belongs to. Similarly, the isinstance() function is used to check if an object belongs to a particular class.

```python
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))
```

output:

```python
5 is of type <class 'int'>
2.0 is of type <class 'float'>
(1+2j) is complex number? True
```

## Python List

List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible. All the items in a list do not need to be of the same type.

Declaring a list is pretty straight forward. Items separated by commas are enclosed within brackets [ ].

```python
a = [1, 2.2, 'python']
```

We can use the slicing operator [ ] to extract an item or a range of items from a list. The index starts from 0 in Python.

```python
a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])
```

output:

```python
a[2] =  15
a[0:3] =  [5, 10, 15]
a[5:] =  [30, 35, 40]
```

## Python Tuple

Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.

Tuples are used to write-protect data and are usually faster than lists as they cannot change dynamically.

It is defined within parentheses () where items are separated by commas.

```python
t = (5,'program', 1+3j)
```

We can use the slicing operator [] to extract items but we cannot change its value.

```python
t = (5,'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
t[0] = 10
```

output:

```python
t[1] =  program t[0:3] =  (5, 'program', (1+3j))

---------------------------------------------------------------------------TypeError                                 Traceback (most recent call last) <ipython-input-5-4413355158bb> in <module>      9 # Generates error     10 # Tuples are immutable---> 11 t[0] = 10TypeError: 'tuple' object does not support item assignment
```

## Python Strings

String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings. Multi-line strings can be denoted using triple quotes, ''' or """.

```python
s = "This is a string"
print(s)
s = '''A multiline
string'''
print(s)
```

output:

```python
This is a string
A multiline
string
```

## Python Set

Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }. Items in a set are not ordered.

```python
a = {5,2,3,1,4}

# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))
```

output:

```python
a =  {1, 2, 3, 4, 5}
<class 'set'>
```
