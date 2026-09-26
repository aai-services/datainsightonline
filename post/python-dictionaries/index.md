---
title: "Python Dictionaries"
author: "Shawon Shariff"
date: 2021-10-06
description: "In this code segment, we will talk about python dictionaries. how they are created, accessing, adding, removing elements from them and various built-in methods.Python dictionary is an unordered..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-dictionaries
---
In this code segment, we will talk about python dictionaries. how they are created, accessing, adding, removing elements from them and various built-in methods.

Python dictionary is an unordered collection of items. Each item of a dictionary has a key/value pair. Dictionaries are optimized to retrieve values when the key is known.

## Creating Python Dictionary
Creating a dictionary is as simple as placing items inside curly braces {} separated by commas. An item has a key and a corresponding value that is expressed as a pair (key: value).

While the values can be of any data type and can repeat, keys must be of immutable type (string, number, or tuple with immutable elements) and must be unique.

```python
# empty dictionary
new_dict = {}

# dictionary with integer keys
new_dict = {1: 'John', 2: 'Doe'}

#dictionary with string keys
new_dict = {'first_name': 'John', 'last_name': 'Joe'}
```

## Accessing Elements

We can the keys to access elements of the dictionary. We use [] or get method to access elements. Let me give you an example of both.

```python
print(new_dict['first_name'])
```

```python
Output: John
```

```python
print(new_dict['middle_name'])
```

```python
-------------------------------------------------------
KeyError  Traceback (most recent call last)
<ipython-input-20-de885c9bc8c1> in <module>()----> 1 print(new_dict['middle_name'])
KeyError: 'middle_name'
```

Here we are getting an error because there is no key named "middle_name". To avoid this kind of situation, we can use the get method to access which will return nothing if there is no matched key.

```python
print(new_dict.get('middle_name')
output: None

print(new_dict.get('last_name'))
output: Joe
```

## Changing and Adding Dictionary elements

Dictionaries are mutable. We can add new items or change the value of existing items using an assignment operator.

If the key is already present, then the existing value gets updated. In case the key is not present, a new (key: value) pair is added to the dictionary.

```python
# Changing and adding Dictionary Elements
new_dict = {'first_name': 'Karim', 'last_name': 'Hasan','age':24}
print(new_dict)

# update value
new_dict['age'] = 27
print(new_dict)

# add item
new_dict['address'] = 'Downtown'
print(new_dict)
```

```python
Output:
{'first_name': 'Karim', 'last_name': 'Hasan', 'age': 24} {'first_name': 'Karim', 'last_name': 'Hasan', 'age': 27} {'first_name': 'Karim', 'last_name': 'Hasan', 'age': 27, 'address': 'Downtown'}
```

## Removing elements from Dictionary

We can remove a particular item in a dictionary by using the pop() method. This method removes an item with the provided key and returns the value.

The popitem() method can be used to remove and return an arbitrary (key, value) item pair from the dictionary. All the items can be removed at once, using the clear() method.

We can also use the del keyword to remove individual items or the entire dictionary itself.

```python
print("Before removing...")
print(new_dict)
print("After Removing Address...")
new_dict.pop('address')
print(new_dict)

new_dict.popitem()
print(new_dict)

# remove all items
new_dict.clear()

# Output: {}
print(new_dict)

# delete the dictionary itself
del new_dict
```

```python
Output:
Before removing...
{'first_name': 'Karim', 'last_name': 'Hasan', 'age': 27, 'address': 'Downtown'}

After Removing Address...
{'first_name': 'Karim', 'last_name': 'Hasan', 'age': 27}

{'first_name': 'Karim', 'last_name': 'Hasan'}
{}
```

## Iterating Through a Dictionary

We can iterate through each key in a dictionary using a for loop.

```python
# Iterating through a Dictionary
second_dict = {"name": "Shawon", "age": 24, "height": "5 feet 10 inch", "weight": "56 kg"}
for key,value in second_dict.items():
    print(key ,":",value)
```

```python
Output:
name : Shawon
age : 24
height : 5 feet 10 inch
weight : 56 kg
```
