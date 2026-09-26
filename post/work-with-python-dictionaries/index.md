---
title: "Work with Python Dictionaries"
author: "pranita shrestha"
date: 2021-10-06
description: "Python provides an unordered collection of data values which can be used to store data called dictionary. The items are placed inside a curly bracket { } seperated by commas (,). It holds key:value..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/work-with-python-dictionaries
---
Python provides an unordered collection of data values which can be used to store data called dictionary. The items are placed inside a curly bracket { } seperated by commas (,). It holds key:value pair. Each key has its own corresponding value. These values can be of any data type and can be used multiple number of times, the keys on the other hand, can't be duplicated, and has to be immutable (integer, string, tuple) and unique.

**How to create dictionaries?**

There are two ways through which dictionaries can be created. One way is to initialize empty dictionary by just using the curly bracket **{}** and the second way is by using an in-built function called **dict()**.

```python
### To create a dictionary ###

# Empty dictionary
my_dict = {}
my_dict1 = dict()
```

While creating keys for the dictionary one can use only integers, only string or even mixed version of integers and string.

```python
# With integer keys
animals = {1 : "dog", 2 : "cat", 3 : "elephant"}

# With string keys
person = {"name" : "Kat", "age" : 25, "address" : "Baluwatar"}

# With mixed keys
cars = dict({"name" : "Ford", 1 : "BMW", "model" : "Mustang"})
```

**What is nested dictionary?**

In python, dictionary provides a nested dictionary feature. This means that a dictionary exists within the dictionary. Basically, its a collection of dictionary within a dictionary itself.

```python
### Nested Dictionary ###
car = dict({"dict1": {"name" : "Ford", "brand" : "Mustang", "year" : 1996}, "dict2" : {"name" : "BMW", "brand" : "Rolls-Royce", "year" : 2000}})
```

Here, the **car** dictionary contains two dictionaries called **dict1** and **dict2**.

**How to access elements in a dictionary?**

To access the elements in a dictionary, the key name should be used. The key can be used by placing it inside the square bracket ([ ]). Another way to access the elements is by using the **get()** method. The key name should be placed inside the get().

```python
### Access elements in the dictionary ###

# Access element by using key
p = person["name"]
c = car["dict1"]["brand"]

# Access elements by using get() method
g = person.get("age")
```

**How to add elements in a dictionary?**

There are multiple ways through which elements can be added to a dictionary. One way is to simply use **Dict[key] : value**. Another way is to create a dictionary and add that dictionary to the main dictionary itself.

```python
### Add elements to dictionary ###

# Simple way of adding elemtns to the dictionary
animals[3] = "crocodile"

# Add another dictionary in the nested dictionary
dict3 = {"name" : "Hyundai", "brand" : "Santro", "year" : 2010}
car["dict3"] = dict3
```

**How to update the elements in a dictionary?**

While adding a value, if the key already exists in the dictionary itself, then the existing value will be updated with the new value. The dictionary can simply be updated by using **Dict[key] : value**.

```python
person["name"] = "Woof"
car["dict1"]["name"] = "Toyota"
```
