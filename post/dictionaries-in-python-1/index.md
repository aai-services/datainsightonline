---
title: "Dictionaries in Python"
author: "Bechir Mathlouthi"
date: 2021-10-06
description: "Dictionary in Python is an unordered collection of data values, used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, Dictionary holds..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/dictionaries-in-python-1
---
Dictionaryin Python is an unordered collection of data values, used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, Dictionary holds **key:value** pair. Key-value is provided in the dictionary to make it more optimized.

## Creating Python Dictionary:
Creating a dictionary is placing items inside curly braces {} separated by commas.

An item has a key and a corresponding value that is expressed as a pair **(key: value)**.

Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable.

Dictionary keys are case sensitive, the same name but different cases of Key will be treated distinctly.

```python
# empty dictionary
dict1 = {}

# dictionary using integer for keys
dict1 = {1: 'car', 2: 'bus'}

# dictionary using mixed keys
dict1 = {'color': 'yellow', 2: [3, 4, 5]}

# each item as a pair
dict1 = dict([(1,'car'), (2,'bus')])

# using dict()
dict1 = dict({1:'car', 2:'bus'})
```

## Accessing Elements from Dictionary :
A value is retrieved from a dictionary by specifying its corresponding key in square brackets ([]):

```python
# accessing elements
dict1 = {'color': 'red', 'score': 20}

# Output: red
print(dict1['color'])
```

**modifying Dictionary elements:**

Dictionaries are mutable. We can add new items or change the value of existing items using an assignment operator.

If the key is already present, then the existing value gets updated. In case the key is not present, a new (**key: value**) pair is added to the dictionary.

```python
# modifyingg Dictionary Elements
dict1 = {'color': 'blue', 'score': 12}

# update value
dict1['score'] = 18

# add item
dict1['color'] = 'green'
```

## Removing elements from Dictionary:
We can remove a particular item in a dictionary by using the pop() method. This method removes an item with the provided key and returns the value.

The popitem() method can be used to remove and return an arbitrary (key, value) item pair from the dictionary. All the items can be removed at once, using the clear() method.

We can also use the del keyword to remove individual items or the entire dictionary itself.

## Conclusion

dictionaries are one of the most frequently used Python types,

In this post, we covered the basic properties of the Python dictionary and learned how to access and manipulate dictionary data.
