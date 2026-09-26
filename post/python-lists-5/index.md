---
title: "Python lists"
author: "amrali150"
date: 2022-02-07
description: "ListsIn this section we will learn about:1.) Creating lists 2.) Indexing and Slicing Lists 3.) Basic List Methods 4.) Nesting Lists 5.) Introduction to List ComprehensionsLists are constructed with..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-lists-5
---
## Lists

In this section we will learn about:

```python
1.) Creating lists
2.) Indexing and Slicing Lists
3.) Basic List Methods
4.) Nesting Lists
5.) Introduction to List Comprehensions
```

Lists are constructed with brackets [] and commas separating every element in the list.

Let's go ahead and see how we can construct lists!

```python
# Assign a list to an variable named my_list
my_list = [1,2,3]
```

We just created a list of integers, but lists can actually hold different object types. For example:

```python
my_list = ['A string',23,100.232,'o']
```

Just like strings, the len() function will tell you how many items are in the sequence of the list.

```python
len(my_list)
```

Output is:

```python
 4
```

### Indexing and Slicing
Indexing and slicing work just like in strings. Let's make a new list to remind ourselves of how this works:

```python
my_list = ['one','two','three',4,5]
```

```python
# Grab element at index 0
my_list[0]
```

Output is:

```python
'one'
```

--------------------------------------------------------------------------------------------------

```python
# Grab index 1 and everything past it
my_list[1:]
```

Output is:

```python
['two', 'three', 4, 5]
```

--------------------------------------------------------------------------------------------------

```python
# Grab everything UP TO index 3
my_list[:3]
```

Output is:

```python
['one', 'two', 'three']
```

We can also use + to concatenate lists, just like we did for strings.

```python
my_list + ['new item']
```

Output is:

```python
['one', 'two', 'three', 4, 5, 'new item']
```

Note: This doesn't actually change the original list!

```python
print(my_list)
```

Output is:

```python
['one', 'two', 'three', 4, 5]
```

You would have to reassign the list to make the change permanent.

```python
# Reassign
my_list = my_list + ['add new item permanently']
```

```python
print(my_list)
```

Output is:

```python
['one', 'two', 'three', 4, 5, 'add new item permanently']
```

We can also use the \* for a duplication method similar to strings:

```python
# Make the list double
my_list * 2
```

Output is:

```python
['one',
 'two',
 'three',
 4,
 5,
 'add new item permanently',
 'one',
 'two',
 'three',
 4,
 5,
 'add new item permanently']
```

```python
# Again doubling not permanent
print(my_list)
```

Output is:

```python
['one', 'two', 'three', 4, 5, 'add new item permanently']
```

## Basic List Methods

If you are familiar with another programming language, you might start to draw parallels between arrays in another language and lists in Python. Lists in Python however, tend to be more flexible than arrays in other languages for a two good reasons: they have no fixed size (meaning we don't have to specify how big a list will be), and they have no fixed type constraint (like we've seen above).

Let's go ahead and explore some more special methods for lists:

```python
# Create a new list
list1 = [1,2,3]
```

Use the **append** method to permanently add an item to the end of a list:

```python
# Append
list1.append('append me!')
```

```python
# Show
print(list1)
```

Output is:

```python
[1, 2, 3, 'append me!']
```

Use **pop** to "pop off" an item from the list. By default pop takes off the last index, but you can also specify which index to pop off. Let's see an example:

```python
# Pop off the 0 indexed item
list1.pop(0)
```

Output is:

```python
1
```

```python
# Show
print(list1)
```

Output is:

```python
[2, 3, 'append me!']
```

```python
# Assign the popped element, remember default popped index is -1
popped_item = list1.pop()
```

```python
print(popped_item)
```

Output is:

```python
append me!
```

```python
# Show remaining list
print(list1)
```

Output is:

```python
[2,3]
```

It should also be noted that lists indexing will return an error if there is no element at that index. For example:

```python
list1[100]
```

Output is:

```python
IndexError                                Traceback (most recent call last)
<ipython-input-22-af6d2015fa1f> in <module>()----> 1 list1[100]IndexError: list index out of range
```

For more **List Methods you can reach out our notebook from** [**here**](https://github.com/Amr-Ali/Python-lists/blob/main/Lists.ipynb)
