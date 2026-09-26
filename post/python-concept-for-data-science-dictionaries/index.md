---
title: "Python Concept for Data Science : Dictionaries"
author: "mairajsaleem92"
date: 2021-10-05
description: "What are Python Dictionaries?Dictionary is a built-in Python Data Structure that is mutable. It is similar to List, Set, and Tuples. However, it is not indexed by a sequence of numbers but indexed..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-concept-for-data-science-dictionaries
---
**What are Python Dictionaries?**

Dictionary is a built-in Python Data Structure that is mutable. It is similar to List, Set, and Tuples. However, it is not indexed by a sequence of numbers but indexed based on keys and can be understood as associative arrays. It consists of a key with an associated value.

**How to Create a Dictionary in Python?**

A dictionary is represented by a pair of curly braces {} in which enclosed are the key: value pairs separated by a comma.

Let's look at the syntax of a dictionary: dictionary = {"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}

Example:

```python
my_dict1 = {'Fruit': 'Apple', 'Vegetable' : 'Potato', 'Food' : 'Fried Chicken'}
print(my_dict1)
```

The output is:

{'Fruit' : 'Apple', 'Vegetable' : 'Potato', 'Food' : 'Fried Chicken'}

**Make a Dictionary with dict() command:**

Using the dict() function, you can convert a compatible combination of constructs into a Python dictionary. Let’s take an example for converting a list into the dictionary with dict() command:

```python
# first create the list
list_1 = ([1,2],[3,4])

# Now make dictionary by using dict()
my_dict2 = dict(list_1)
print(my_dict2)
```

The output is :

{1: 2, 3: 4}

**Print Keys and Values from any Dictionary:**

We can access the keys and values like the name of dictionary comes first and then after a dot, we type the required category either keys or values.

```python
print(my_dict1.keys())
print(my_dict1.values())
```

The output shows all keys and values in my_dict1 :

dict_keys(['Fruit', 'Vegetable', 'Food'])

dict_values(['Apple', 'Potato', 'Fried Chicken'])

**Declaring one key more than once:**

Dictionaries are mutable but their keys are immutable. If we placed the same key more than once. The output shows the last value related to this key. Let’s check with example.

```python
my_dict3 = {'name' : 'Sam', 'city' : 'London', 'country' : 'United Kingdom', 'city' : 'Bristol'}
print(my_dict3)
```

The output shows the city as Bristol in place of London because it defines after London and the last defined value of city key in the dictionary:

{'name' : 'Sam', 'city' : 'Bristol', 'country' : 'United Kingdom'}

**How to Access Value from a Python Dictionary?**

1. By using Square Bracket

To access an item from a list or a tuple, we use its index in square brackets. This is the python syntax to be followed. However, a Python dictionary is unordered. So, to get a value from it, you need to put its key in square brackets.

```python
# To access the value from Dictionary
print(my_dict3['name'])
print(my_dict3['country'])
```

The output is :

Sam

United Kingdom

2. By using get() command:

We also access value from dictionary by using get() command shown below:

```python
# Another way to access the value from Dictionary by using get() command:
print(my_dict3.get('city'))
print(my_dict3.get('name'))
```

The output is :

Bristol

Sam

**For accessing multiple values from Dictionary:**

To get the multiple values from the dictionary, the above two methods not working and produce an error. There are many other methods to get the values from the dictionary, we use for loop function to get the multiple values. Lets explain with an example:

```python
# For multiple values from Dictionary
# first make the list of keys to access
keys = ['name', 'country']

# Now apply for loop
for key in keys:
    print(my_dict3.get(key))
```

The output shows the values related to keys name and country shown below:

Sam

United Kingdom

**Reassigning and adding new pair in a Python Dictionary:**

The Python dictionary is mutable. This means that we can change it or add new items without having to reassign all of them.

1. Updating the Value of an Existing Key

If the key already exists in the Python dictionary, you can reassign its value using square brackets.

For example, we reassign the city Bristol to Manchester in the my_dict3.

```python
my_dict3['city'] = 'Manchester'
print(my_dict3)
```

The output shows Manchester in place of Bristol.

{'name' : 'Sam', 'city' : 'Manchester', 'country' : 'United Kingdom'}

2. Adding a new key

We use a similar approach to updated a value but define a new key that’s not available in the dictionary. This new defined key and values make a new pair of the dictionary.

Let’s define key ‘gender’ to value ‘male’ in my_dict3.

```python
my_dict3['gender']='Male'
print(my_dict3)
```

The output shows the new pair of gender and its value is male.

{'name' : 'Sam', 'city' : 'Manchester', 'country' : 'United Kingdom', 'gender' : 'Male'}

**How to Delete Python Dictionary?**

**1. Deleting an entire Python dictionary :**

To delete the whole Python dictionary, simply use its name after the keyword ‘del’.

```python
# Deleting an entire dictionary
del my_dict2
print(my_dict2)
```

The output error shows us my_dict2 is deleted and not available for printing.

-------------------------------------------------------------

NameError
Traceback (most recent call last)
<ipython-input-46-0df85467a370> in <module>
 1 # Deleting an entire dictionary
 2 del my_dict2
----> 3 print(my_dict2)
NameError: name 'my_dict2' is not defined

**2. Deleting a single key-value pair:**

To delete just one key-value pair, use the keyword ‘del’ with the key of the pair to delete. Let’s explain by example.

```python
# Deleting the gender key from my_dict3
del my_dict3['gender']
print(my_dict3)
```

The output shows only three pairs in my_dict3. The gender pair is deleted from the dictionary.

{'name': 'Sam', 'city': 'Manchester', 'country': 'United Kingdom'}

**Conclusion:**

In this blog, we learn to create a new dictionary from scratch, access the keys and values from the dictionary, impact of two same keys in the dictionary, update and add a new pair in the dictionary also deleting the selective keys and whole dictionary. I believe this blog is helpful for you, kindly check my Git Hub repository

https://github.com/MuhammadMairajSaleem92/Projects/blob/main/Prime%20Numbers.ipynb
