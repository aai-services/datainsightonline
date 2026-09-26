---
title: "Dictionaries in Python"
author: "Eslam Elkot"
date: 2021-10-06
description: "Dictionaries in Python could do a great job, sometimes. For example, when using companies’ names as keys and their prices on the market as values. Working with dictionaries is similar to working with..."
categories: ["Python"]
image: images/b9ba6c_6b3d6e53a1fa4aa0a1f387d4463b7fe1.webp
wix-url: https://www.datainsightonline.com/post/dictionaries-in-python
---
![](images/b9ba6c_6b3d6e53a1fa4aa0a1f387d4463b7fe1.webp)

Dictionaries in Python could do a great job, sometimes. For example, when using companies’ names as keys and their prices on the market as values. Working with dictionaries is similar to working with lists. The key in a dictionary represents one unique thing, and you can associate a value with that key.

Each dictionary having multiple keys is common in Python, because the language makes it easy to isolate the specific item of data you want using object. Key syntax. We will discuss Protein Content of Foods.

```python
food = {
'beef': 19,
'chicken_breast': 24.7,
'turkey': 25.9,
'ham': 21,
'salami': 25,
'egg': 13.5,
'duck': 19
}
```

**Accessing dictionary data**

After you have added the data in, you can work with it in a number of ways. Using print(food) — that is, a print() function with the name of the dictionary in the parentheses — you get a copy of the whole dictionary, as follows:

```python
print(food)
```

Typically this is not what you want. More often, you’re looking for one specific item in the dictionary. In that case, use this syntax:

```python
print(food['duck'])
So what do you think would happen if you executed the following code?
delicious = 'beef'
print(food[delicious])
```

You would, of course, see 19, the name (value) that goes with the key 'beef'.

## Getting the length of a dictionary
The number of items in a dictionary is considered its length. As with lists, you can use the len() statement to determine a dictionary’s length. The syntax is:

```python
food = {
'beef': 19,
'chicken_breast': 24.7,
'turkey': 25.9,
'ham': 21,
'salami': 25,
'egg': 13.5,
'duck': 19
}
# Count the number of key:value pairs and put in a variable.
howmany = len(food)
# Show how many.
print(howmany)
```

## Seeing whether a key exists in a dictionary
You can use the in keyword to see whether a key exists. If the key exists, then in returns True. If the key does not exist, in returns False. following code shows a simple example with two print() statements. The first one checks to see whether egg exists in the dictionary. The second checks to see whether beans exists in the dictionary.

```python
# Make data dictionary named food
food = {
'beef': 19,
'chicken_breast': 24.7,
'turkey': 25.9,
'ham': 21,
'salami': 25,
'egg': 13.5,
'duck': 19
}
# Is there an egg in food dictionary ?
print('egg' in food)
# Is there an ham in food dictionary ?
print('beans' in food)
```

## Getting dictionary data with get()
Having the program kind of crash and burn when you look for something that isn’t in the dictionary is a little harsh. A more elegant way to handle that is to use the .get() method of a data dictionary. The syntax is:

```python
# Look for a food.
delicious = 'turkey'
print(food.get(delicious))
```

You get the same result as you would using square brackets. What makes .get() different is what happens when you search for a nonexistent name. You don’t get an error, and the program doesn’t just crash and burn. Instead, get() just returns the word None to let you know that no food named beans is in the food dictionary.

```python
# Make data dictionary named food
food = {
'beef': 19,
'chicken_breast': 24.7,
'turkey': 25.9,
'ham': 21,
'salami': 25,
'egg': 13.5,
'duck': 19
}
# Look for a food
delicious = 'beans'
print(food.get(delicious))
```

## Changing the value of a key
Dictionaries are mutable, which means you can change the contents of the dictionary from code (not that you can make the dictionary shut up). For example, supposed the man who make this list is changing turkey's protein content from 25.9 to 26.3 for the turkey breasts he is usually uses. You want to keep the same key, just change the value.

```python
# Print turkey's current value
print(food['turkey'])
# Change the value of turkey key
food['turkey'] = 26.3
#Print turkey key to verify the value has updated
print(food['turkey'])
```

## Adding or changing dictionary data
You can use the dictionary update() method to add a new item to a dictionary, or to change the value of a current key. Replace key with the key of the item you want to add or change. If the key you specify doesn’t already exist with the dictionary, it will be added as a new item with the value you specify.

If the key you specify does exist, then nothing will be added. The value of the key will be changed to whatever you specify as the value.

```python
# Make a data dictionary named food.
food = {
'ham': 21,
'turkey': 25.9
}
# Change the value of the turkey key.
food.update({'turkey':26.3})
print(food)
# Update the dictionary with a new property:value pair.
food.update({'salami':25})
print(food)
```

If the key already exists in the dictionary, then its value is updated, because no two items in a dictionary are allowed to have the same key.

If the key does not already exist, then the key-value pair is added because there is nothing in the dictionary that already has that key, so the only choice is to add it.

```python
# Show what's in the data dictionary now.
for value in food.keys():
  print(value + " = " + food[value])
```

You may have noticed that some of the methods for data dictionaries look similar to those for lists, tuples, and sets. So maybe now would be a good time to list all the methods that dictionaries offer for future reference.

|  |  |
| --- | --- |
| **Method** | ​**What it Does** |
| ​clear() | ​Empties the dictionary by remove all keys and values. |
| copy() | Returns a copy of the dictionary. |
| fromkeys() | Returns a new copy of the dictionary but with only specified keys and values. |
| get() | Returns the value of the specified key, or None if it doesn’t exist. |
| items() | Returns a list of items as a tuple for each key-value pair. |
| keys() | Returns a list of all the keys in a dictionary. |
| pop() | Removes the item specified by the key from the dictionary, and stores it in a variable. |
| popitem() | Removes the last key-value pair. |
| setdefault() | Returns the value of the specified key |
| update() | Updates the value of an existing key, or adds a new key-value pair. |
| values() | Returns a list of all the values in the dictionary. |

Hopefully, this article was helpful to you.

Link to the GitHub repository [here](https://github.com/EslamElkot/EslamEklot.github.io/blob/main/Dictionaries.ipynb)
