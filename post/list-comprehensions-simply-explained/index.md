---
title: "List Comprehensions Simply Explained"
author: "Magdy Ahmed"
date: 2021-10-05
description: "List comprehensions are one of the easiest and most efficient ways to create lists in Python. But first what does the term \"comprehension\" mean and does it belong exclusively to Lists ?Comprehensions..."
categories: ["Python"]
image: images/215973_334268a8f15948db983df145b0a61f4f.webp
wix-url: https://www.datainsightonline.com/post/list-comprehensions-simply-explained
---
![](images/215973_6d1672df9d634fcd917a0802272c3111.webp)

**List comprehensions** are one of the easiest and most efficient ways to create lists in Python. But first what does the term "comprehension" mean and does it belong exclusively to Lists ?

Comprehensions are constructs that allow sequences to be built from other sequences, Python has a special syntax called *comprehension* for combining iteration with the creation of a data structure. It is essentially a for loop wrapped in the appropriate brackets for creating data structures like :

- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Generator comprehensions

Comprehensions are an elegant way to write and make code more readable.

## Example of a Simple List Comprehension:
So what if you wanted to get the squares of the first five numbers, the code would go something like this:

```python
squares = [x**2 for x in range(5)]
# Output: [0, 1, 4, 9, 16]
```

**List Comprehension** consist of square brackets containing an expression followed by a for and that's it you're all set.

The same thing can be done using an empty list and a for loop but it would take more lines of code.

```python
squares = []
for x in range(5):
    squares.append(x**2)
# Output: [0, 1, 4, 9, 16]
```

And it wouldn't be as efficient, Of course the above examples are oversimplified to better understand the idea of the syntax.

## Example of List Comprehension with an If Condition:
So what if you wanted to get the squares of the first 10 even numbers, we would use an if condition to filter the code like this:

```python
evenSquares = [x**2 for x in range(10) if x % 2 == 0]
# Output: [0, 4, 16, 36, 64]
```

Same thing using a for loop:

```python
evenSquares=[]
for x in range(10):
    if x % 2 == 0:
        evenSquares.append(x**2)
# Output: [0, 4, 16, 36, 64]
```

## Example List Comprehension with If and Else Conditions:
So what if you wanted to get the squares of the first 10 even numbers and keep track of the odd numbers, we would use an if and else conditions to filter the code like this:

```python
S = [x**2 if x % 2 == 0 else x for x in range(10)]
# Output: [0, 1, 4, 3, 16, 5, 36, 7, 64, 9]
```

And the same thing using a for loop:

```python
S =[]
for x in range(10):
    if x % 2 == 0:
        S.append(x**2)
    else:
        S.append(x)
# Output: [0, 1, 4, 3, 16, 5, 36, 7, 64, 9]
```

## So When Is It Appropriate to Use List Comprehensions?
You can use **list comprehension** if you are doing simple filtering, modifications, or a formatting task on other iterative objects. It's also a good choice if you want to keep your code compact and readable.

Also, you can use it when even a small fraction of performance matters to you.

But you should avoid using **list comprehension** if you have too many conditions to add for filtering or modifying as it will make your code more complex and harder to read.

## Conclusion
Whenever you have to choose a list creation method, try multiple implementations and consider what’s easiest to read and understand in your specific scenario, Remember that while Python **list comprehensions** get a lot of attention, your intuition and ability to use data when it counts will help you write clean code that serves the task at hand.
