---
title: "Python Concepts for Data Science: List Comprehension"
author: "Abhishek Tuladhar"
date: 2021-10-05
description: "List comprehension is an elegant way to define and create lists based on existing lists. It is generally more compact and faster than normal functions and loops for creating lists. The syntax:newlist..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-concepts-for-data-science-list-comprehension
---
List comprehension is an elegant way to define and create lists based on existing lists. It is generally more compact and faster than normal functions and loops for creating lists.

**The syntax:**

```python
newlist = [expression for item in iterable if condition == True]
```

The return value is a new list, leaving the old list unchanged. Here, the 'condition' is like a filter that only accepts the items that evaluate to True. The 'iterable' can be any iterable object, like a list, tuple, set etc. The 'expression' is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list.

**Example:**
Let us take an example of creation of a new list based on both with and without list comprehension. Suppose, based on a list of fruits, we want a new list, containing only the fruits with the letter "a" in the name.

**Without list comprehension:**

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
```

Output:

```python
['apple', 'banana', 'mango']
```

**With list comprehension:**

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
```

Output:

```python
['apple', 'banana', 'mango']
```

**Conditionals in List Comprehension**

1. Using if with List Comprehension

Example:

```python
number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)
```

Output:

```python
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

2. Nested IF with List Comprehension

Example:

```python
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)
```

Output:

```python
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
```

3. if...else With List Comprehension

Example:

```python
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)
```

Output:

```python
['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
```

**Nested Loops in List Comprehension**

For this, we will use the transpose of a matrix using nested loops.

```python
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)
```

Output:

```python
[[1, 3, 5, 7], [2, 4, 6, 8]]
```

One main benefit of using a list comprehension in Python is that it’s a single tool that we can use in many different situations. However, they’re not the right choice for all circumstances as they might make the code run more slowly or use more memory. Hence, based on the requirements, one can choose list comprehension or other alternatives.
