---
title: "Loops in python"
author: "Gehad Hisham"
date: 2022-02-05
description: "This is less like the for a keyword in other programming languages and works more like an iterator method as found in other object-orientated programming languages.1- while loop: Repeats a statement..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/loops-in-python-2
---
This is less like the for a keyword in other programming languages and works more like an iterator method as found in other object-orientated programming languages.

**1- while loop:**
Repeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body.

**2- for loop:**
Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.

## For loop
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

With the for loop, we can execute a set of statements, once for each item in a list, tuple, set etc.

**Example:**

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

Output:

```python
apple
banana
cherry
```

**Looping Through a String:**

Even strings are iterable objects, they contain a sequence of characters:

**Example**
Loop through the letters in the word "Gehad":

```python
for x in "Gehad":
  print(x)
```

Output:

```python
G
e
h
a
d
```

**The break Statement**

With the break statement we can stop the loop before it has looped through all the items:

**Example**
Exit the loop when x is "banana":

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
```

output:

```python
apple
banana
```

**The continue Statement**
With the continue statement we can stop the current iteration of the loop, and continue with the next:

**Example**
Do not print banana:

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
```

Output:

```python
apple
cherry
```

**The range() Function:**

To loop through a set of code a specified number of times, we can use the range() function, The range() function returns a sequence of numbers, starting from 0 by default, increments by 1 (by default), and ends at a specified number.

**Example**
Using the range() function:

```python
for x in range(6):
  print(x)
```

Output:

```python
0
1
2
3
4
5
```

Thank you..
