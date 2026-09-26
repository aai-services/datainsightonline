---
title: "Lists in Python"
author: "Mariam Ahmed"
date: 2022-05-15
description: "The list is a data structure in Python that is a mutable, ordered sequence of elements. It is one of 4 built-in data types in Python. It is used to store collections of data. Its items' index is..."
categories: ["Python"]
image: images/47a959_70d88123e33840cdab8564883d80364a.webp
wix-url: https://www.datainsightonline.com/post/lists-in-python-1
---
![](images/47a959_70d88123e33840cdab8564883d80364a.webp)

The list is a data structure in Python that is a mutable, ordered sequence of elements. It is one of 4 built-in data types in Python. It is used to store collections of data. Its items' index is zero-based.

The list denotes by [] brackets and is heterogeneous as follows:

```python
List = ['Hana', 35, True]
```

The new list may define using list () i.e.:

```python
Fruit = "Apple", "Banana", "Pear"
FruitList = list(Fruit)
```

It allows duplicate members as follows:

```python
List = ['Good', 'Fail', 'Very Good', 'Good', 'Good', 'Fail']
```

The items in a list can be accessed or changed through indexing and slicing. Accessing and Changing by indexing as follows:

```python
List = ['red', 'blue', 'green']
List [1] = 'black'
```

Then the list will become:

```python
List = ['red', 'black', 'green']
List[-1] = 'white'
```

Then the list will become:

```python
List = ['red', 'black', 'white']
```

Accessing by slicing may be as the following example:

```python
List = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
SmallLst = List[:4]
```

**Note** it selects all elements from the start with index 0 to the element with index 3 and ignores the element with index 4.

So, it will contain [10, 20, 30, 40].

```python
MedLst = List[4:7]
```

**Note** it selects all elements from the element with index 4 to the element with index 6 and ignores the element with index 7.

So, it will contain [50, 60, 70].

```python
LargeLst = List[7:]
```

**Note** it selects all elements from the element with index 7 to the end of the list.

So, it will contain [80, 90, 100].

We can copy a list of items in another list using slicing as follows:

```python
NewLst = List[:]
```

So, it will contain [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

We can do the same thing as in the previous statement by writing in the end index of the period number greater than the length of the list and it won't get any error messages as follows:

```python
NewLst2 = [:50]
```

So, it will contain also [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

We can go throw the list with a specific step number that makes us jump from some elements and ignores these as follows:

```python
QuickLst = List[::3]
```

So, it will contain [30, 60, 90]

There are some important functions that are used with the lists i.e.:

1. Adding elements to the list using the following functions:

1.1 append(): to add an element to the end of the list.

```python
Lst = [1, 2, 3]
Lst.append(4)
```

So it will become: [1, 2, 3, 4]

1.2 insert(): to add an element to a specific place in the list.

The syntax is:

```python
insert(index, object)
```

If we use the previous list as follows:

```python
Lst.Insert(2, 5)
```

It will become:

[1, 2, 5, 3, 4]

1.3 extend(): to a list to the end of another list.

If we use the previous list as follows:

```python
Lst.extend([6, 7, 8])
```

It will become:

[1, 2, 5, 3, 4, 6, 7, 8]

2. Removing elements from a List using the following functions:

2.1 remove(item): to remove the first occurrence of the item from the list.

```python
Lst.remove(1)
```

It will become:

[2, 5, 3, 4, 6, 7, 8]

2.2 clear(): it turns any list into an empty list.

```python
Lst.clear()
```

It will become:

[]

2.3 del list_name: delete the entire list.

```python
del Lst
```

Then the output of:

```python
Print(Lst)
```

Will become:

```python
NameError: name 'Lst' is not defined.
```

3. Finding an element in the list using the function as follows:

index(): it returns the first occurrence of the element or returns ValueError if the element does not exist.

```python
Lst = [1, 5, 7,5]
Lst.index(5)
```

It will return:

```python
 1
```

That's it, I hope this article was worth reading and helped you acquire new knowledge no matter how small.

Feel free to check up on the [notebook](https://github.com/MariamAlsaedy/Data-Insight-Scholarship-Article-1/blob/main/Lists.ipynb). You can find the results of code samples in this post.
