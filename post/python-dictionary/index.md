---
title: "Python Dictionary"
author: "sefako dorlote djaman"
date: 2021-10-06
description: "Creating Python DictionaryA dictionary is a data structure allowing to have access to a set of data. It is used to have variables with their correspondences. However, the difference between a..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-dictionary
---
**Creating Python Dictionary**

A dictionary is a data structure allowing to have access to a set of data. It is used to have variables with their correspondences. However, the difference between a dictionary and a list is that the bracket delimiter and the indexes of lists are replaced by braces and keys in dictionaries. To create a dictionary, you need two elements which are the keys and the values separated by a colon. Keys and values can be in different type.There are several methods to build a dictionary. The syntaxes are written as follows:

```python
#create dictionary
dict = {}
#Or
dict = {'keys':'values', 'keys':'values','keys':'values'}
```

A key can have values as a list or as a dictionary. In both cases, the creation of the dictionary is done as follows:

```python
#dictionary of dictionairies
dict ={'keys':{'keys': 'values', 'keys':'values', 'keys':'values'}}

#dictionary with value as a list
dict_list={'keys':['...','...','...']}
```

**Verification element in the dictionary**

The verification of keys, values in any dictionary is done respectively by these methods. They are written as follows in the lines of code below:

```python
# print Keys
'Keys'in dict

# Print out value that belong to 'keys'
print(dict['keys'])
```

**Deleting**

Delete a key in a dictionary is done in the same way as in a list.

```python
#delete keys
del(dict['keys'])
```

The method of adding a new element to a dictionary is identical to the method of updating it. The code below illustrates this in detail:

```python
#add new element
Dict['keys'] ='values'
```

**Merge dictionaries**

The merging of two dictionaries is done with .update(). The code below tells us this:

```python
# creating two new dictionary
dict_1 ={}
dict_2 ={}

# merge of dictionaries
dict_1. update (Dict_2)
print(dict_1)
```

**Concrete example**

In this practical case, we would create a dictionary and perform the operations seen above. Our dictionary contains information about the price of foodstuffs in Senegal.

```python
#create dictionary
dict_food ={'rice':350, 'oil':150,'sugar':650,'milk':100}

# delete ‘milk’
del(dict_food['milk'])

#add new keys
dict_food['corn'] =300
print(dict_food)
output:
{'rice': 350, 'oil': 150, 'sugar': 650, 'corn': 300}

# another dictionary
dict_sen = {'tomate':1000,'oignon':500,'Pomme de terre':500}

#merging dict_food and dict_sen
dict_food.update(dict_sen)
print(dict_food)
output:
{'rice': 350, 'oil': 150, 'sugar': 650, 'corn': 300, 'tomate': 1000, 'oignon': 500, 'potatos': 500}
```
