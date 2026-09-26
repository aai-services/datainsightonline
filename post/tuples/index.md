---
title: "Tuples"
author: "fredy chimire"
date: 2021-10-05
description: "Python tuples are a data structure that store an ordered sequence of values. Tuples are immutable. This means you cannot change the values in a tuple. Tuples are defined with parenthesis. Tuples are..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/tuples
---
Python tuples are a data structure that store an ordered sequence of values. Tuples are immutable. This means you cannot change the values in a tuple. Tuples are defined with parenthesis.

Tuples are a core data structure in Python. They let you store an ordered sequence of items. For example, you may use a tuple to store a list of employee names. You could use a tuple to store a list of ice cream flavors stocked at an ice cream shop.

A tuple is a comma-separated sequence of items. This sequence is surrounded by parenthesis (()). Let’s create a tuple:

```python
# Creating a tuple
ice_cream_flavors = ('Chocolate', 'Vanilla', 'Mint', 'Strawberry', 'Choc-Chip')
```

When we print our tuple to the console using the print()function, we will see the tuple that we originally declared. The values in our tuple are separated by commas:

```python
print(ice_cream_flavors)
('Chocolate', 'Vanilla', 'Mint', 'Strawberry', 'Choc-Chip')
```

Each item in a tuple has a unique index value, starting with zero. Index values continue in increments of one. You can access an individual item in a tuple by referencing the item’s index value.

```python
#we can access a single element individually.
#The following code allows us to get the item at the index value 3:
print(ice_cream_flavors[3])
out:Strawberry
```

Our code returns: Strawberry. Strawberry is the item whose index value is 3.

Each item in a tuple has a negative index value. These values let us count backward from the end of a tuple. They start at -1. Using a negative index number may be more convenient if you are working with a long list. This is because you can work backwards from the end of the list.

```python
#If we wanted to get the value at the index position of -1, we could use the following code:
print(ice_cream_flavors[-1])
out: Choc-Chip
```

**Tuple Slicing**
Similarly, if we want to get a range of items within our tuple, we can specify a range of indexes to retrieve. In order to do so, we need to specify where to start and end our range. We can use the following code to retrieve every item in the range of the 1 and 4 index values:

```python
print(ice_cream_flavors[1:4])
out: ('Vanilla', 'Mint', 'Strawberry')
```

Our code returns: (‘Vanilla’, ‘Mint’, ‘Strawberry’)

In this example, our code returns every value with an index value between 1 and 4, exclusive of the last index value. Our code does not return Choc-Chip because Choc-Chip does not appear in the defined range.

**Conclusion**

The tuple data type is an immutable, ordered data type that allows you to store data in Python. Tuples are somewhat faster to use than lists in Python because they cannot be changed. As such, they’re useful if you need to store data that will not change.

Use the
