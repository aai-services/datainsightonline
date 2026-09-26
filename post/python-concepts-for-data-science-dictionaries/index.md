---
title: "Python Concepts For Data Science: Dictionaries"
author: "Ishan Chudali"
date: 2021-10-07
description: "Python Dictionaries:Python dictionary is an unordered collection of items. Each item of a dictionary has a key/value pair. Each key is separated from its value by a colon (:), the items are separated..."
categories: ["Python"]
image: images/4cb298_083e4d0651cc49f5a444cfc54eddaa28.webp
wix-url: https://www.datainsightonline.com/post/python-concepts-for-data-science-dictionaries
---
**Python Dictionaries:**

![](images/4cb298_083e4d0651cc49f5a444cfc54eddaa28.webp)

**Python dictionary** is an unordered collection of items. Each item of a dictionary has a key/value pair.

Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: {}.

dict ={

"Name": "Any_name",

"Age": "18",

}

This is how the python dictionary looks. Here 'name' and "age' are the keys while 'any_name' and '18' are their corresponding values in the dictionary named 'dict'.

**Creating a dictionary:**

In Python, a Dictionary can be created by placing a sequence of elements within curly **{}** braces, separated by ‘comma’. Dictionary holds a pair of values, one being the Key and the other corresponding pair element being its **Key:value**.

```python
dict ={

"Name": "Any_name" ,

"Age": "18",
}
print(dict)
```

```python
{'Name': 'Any_name', 'Age': '18'}
```

**Accesing values in dictionary:**

To access dictionary elements, you can use the familiar square brackets along with the key to obtain its value.

```python
dict ={
"Name": "Any_name",
"Age": "18",
}
print(dict['Name'])
print(dict['Age'])
# printing both values
print(dict['Name']+"is"+dict['Age']+"years old.")
```

```python
Any_name
18
Any_nameis18years old.
```

**Adding,Updating ,Deleting dictionary elements:**

**Adding items:**

Adding an item to the dictionary is done by using a new index key and assigning a value to it:

```python
dict ={
"Name": "Any_name",
"Age": "18",
}
dict['Address']="your_add"
print(dict)
```

```python
{'Name': 'Any_name', 'Age': '18', 'Address': 'your_add'}
```

**Updating items:**

We can change the value of a specific item by referring to its key name:

```python
dict ={
"Name": "Any_name",
"Age": "18",
}
dict['Age']="20"
print(dict)
```

```python
{'Name': 'Any_name', 'Age': '20'}
```

The update() method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.

```python
dict ={
"Name": "Any_name",
"Age": "18",
}
dict.update({"Age": 22})
print(dict)
```

```python
{'Name': 'Any_name', 'Age': 22}
```

**Deleting items:**

The del keyword removes the item with the specified key name:

Example:

```python
dict ={
"Name": "Any_name",
"Age": "18",
}
del dict['Name']
print(dict)
```

```python
{'Age': '18'}
```

We can also delete the entire dictionary using del keyword.

```python
dict ={
"Name": "Any_name",
"Age": "18",
}
del dict
print(dict)
```

```python
<class 'dict'>
```

Summerizing :

```python
#creating dictionary dict
dict ={
"Name": "Any_name",
"Age": "18",
}
print(dict)

#accessing values
print(dict['Name'])

#adding items
dict['Address']="your_add"
print(dict)

#updating items
dict.update({"Age": 22})
print(dict)

#deleting items
del dict['Name']
print(dict)
```

```python
{'Name': 'Any_name', 'Age': '18'}
Any_name
{'Name': 'Any_name', 'Age': '18', 'Address': 'your_add'}
{'Name': 'Any_name', 'Age': 22, 'Address': 'your_add'}
{'Age': 22, 'Address': 'your_add'}
```

**Iterating through dictionaries in python:**

we can loop through a dictionary by using a for loop.There are multiple ways to iterate over a dictionary in Python.

- Iterate through all keys
- Iterate through all values
- Iterate through all key, value pairs

***Iterate through all keys***

Here we create a dictionary named **firstand_lastname** and iterate through all keys.

```python
firstand_lastname = {

                     'john' : 'bista',

                     'Jeff' : 'bezos',

                     'Suraj' : 'raaj',

                     }


 print('firstnames:')

  # Iterating over keys

for f_name in firstand_lastname   :

    print(f_name)
```

```python
firstnames:
john
Jeff
Suraj
```

***Iterate through all values:***

```python
firstand_lastname = {
                     'john' : 'bista',
                     'Jeff' : 'bezos',
                     'Suraj' : 'raaj',
                     'anthony' : 'charlie'
                     }

print('lastnames:')

# Iterating over values
for  last_name in firstand_lastname.values():
    print(last_name)
```

**In this case the values may not be printed in the order they are stored.**

```python
lastnames:
bista
bezos
raaj
charlie
```

***Iterate through all key, value pairs:***

here in this example all the key values pairs are printed.

```python
firstand_lastname = {
                     'john' : 'bista',
                     'Jeff' : 'bezos',
                     'Suraj' : 'raaj',
                     'anthony' : 'charlie'
                     }

# Iterating over keys and values
print("the  complete names are:")

for lname, last_name in firstand_lastname.items():
    print(lname, ":", last_name)
```

```python
the  complete names are:
john : bista
Jeff : bezos
Suraj : raaj
anthony : charlie
```

The link to the notebook in github repo is [here](https://github.com/Techy-Ishan/Python-dictionaries/blob/master/Python%20dictionaries.ipynb) .
