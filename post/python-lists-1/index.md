---
title: "Python Lists"
author: "Vanessa Arhin"
date: 2021-10-04
description: "A python list collection of different items put together. In our lives, we make lists for certain things, activities, etc. The same thing can be done with python programming language. A python list..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-lists-1
---
A python list collection of different items put together. In our lives, we make lists for certain things, activities, etc. The same thing can be done with python programming language.

A python list could contain a single item or a collection of multiple items saved under a single variable. List is one of the six standard python data types. A python list is said to be ordered, changeable and allows duplicate members. It is indicated by square brackets [ ] and all items are separated by a comma.

```python
list_1 = []
```

Python lists could contain different date types in relation to the items included. These are data types are integers, floats, strings, boolean, etc.

```python
 list_1 = ['my name', 3, True, 4.6]
```

**What is meant by python lists are ordered?**

Thismeans that items in a list follows a particular order and does not change. This order brings about indexing(numbering) of the items in a list.

Index of items helps you to access them easily and quickly. The first item of a list has an index of 0, the second has an index of 1, the third has an index of 2, it follows in that order. So, you can access an item by call the list an putting the index in a square bracket by the list variable.

```python
list_1 = ['my name', 3, True, 4.6]
list_1[1]
3
```

Negative indexing is another way of selecting items using negative index. This way of numbering starts from the bottom of the list with the last item indexed -1.

```python
list_1 = ['my name', 3, True, 4.6]
list_1[-1]
4.6
```

However, a range of items can be selected from a list. It is done by specifying the index of where you want your range to start from to where it ends. The last index specified is not included. For instance if the last index you select is 3, the last item to be displayed is index 2.

```python
list_1 = ['my name', 3, True, 4.6]
list_1[1:3]
[3, True]
```

**List allows duplicate items**

Python list allows items to have the same value.

```python
list_2 = ['red','white','cyan','white','black']
```

**Lists are Changeable.**

This means that you can add, remove or change items in a list after you have created it. There are some methods that can help you make these changes. Some of these methods are:

.append() - used to add an item at the end of the list.

.insert() - used to add an item at a specified position.

.extend() - used to add items to the end of a list.

.remove() - removes an item with a specified value.

.pop() - removes an item with a specified position.

.copy() - used to make a copy of a list.

.sort() - used to sort a list.

**Checking the Length and Type of a List.**

You can check the length of a list to know how many items are contained in a list. You can do so by passing the list name to the syntax **len()** with the list name inside the parentheses.

```python
list_2 = ['red','white','cyan','white','black']
len(list_2)
5
```

Also, you can check what kind of data type a list is. You can do so by passing the list name to the syntax **type()** with the list name inside the parentheses, and print it as well.

```python
list_2 = ['red','white','cyan','white','black']
print(type(list_2))
<class 'list'>
```

**Joining Lists.**

As you continue to write codes, you may want to combine two or more lists. Combining lists could be done in several ways. You can use the **+** operator for joining lists, the **append** method or the **extend** method.

```python
list_1 = ['my name', 3, True, 4.6]
list_2 = ['red','white','cyan','white','black']
list_1 + list_2
['my name', 3, True, 4.6, 'red', 'white', 'cyan', 'white', 'black']
```

```python
list_1.append(list_2)
print(list_1)
['my name', 3, True, 4.6, 'red', 'white', 'cyan', 'white', 'black']
```

```python
list_1.extend(list_2)
print(list_1)
['my name', 3, True, 4.6, 'red', 'white', 'cyan', 'white', 'black']
```

However, these are just the basics of using python lists. There are lots of things you could do with lists in python.
