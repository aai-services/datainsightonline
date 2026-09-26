---
title: "Python Dictionaries Overview"
author: "bismark boateng"
date: 2021-10-07
description: "Python dictionaries is one of the data types in python a developeror a data scientist can work with. It's a special kind of data type that accepts and store two entities, one being a key, and the..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-dictionaries-overview
---
Python dictionaries is one of the data types in python a developer

or a data scientist can work with.

It's a special kind of data type that accepts and store two entities,

one being a key, and the other being a value.

A key correspond to a value.

key's can be an integer or a string etc.

Creating a dictionary

```python
dict_1 = {}
```

When a dictionary is created using the above code, one can opt to either

hardcode the key and value pairs into the dictionary or can loop through

a dataset and update those values into the dictionary created.

An example of a dictionary:

```python
#dictionary
dict_1 = {
      "name" : "jack",
      "age" : 12,
      "height" : 2.3
      }
print(dict_1["name"])
```

In the above code, a dictionary called dict_1 is created and the details of a person is added into it.

The details contain the person's name, age and height .

unlike lists, dictionaries can be called by it's key. thus, to get the value of jack, the snippet of code wrapped in the print() function above does that.

likewise, to get the height of jack:

```python
print(dict_1["height"])
```

the code above print statement above outputs the height of jack from

the dictionary data type .

Adding key value pairs into a dictionary

Since a dictionary accepts a key, value pair, to add a data into the

dictionary, one has to specify the key that corresponds to the value he or she wants to assign it to

```python
dict_2 = {"sex": "Male"}
dict_1.update(dict_2)
```

In the above code, the sex of jack is specified as Male and it's being updated into the main dictionary dict_1.

take note; the update() method is used here, the update method accepts two values, meanwhile, since we passed in a dictionary, python will throw us an error
