---
title: "Python Dictionaries"
author: "Isuru Lakshan"
date: 2021-10-11
description: "Come let's talk about amazing data structure in python language. DICTIONARIES !!! and How to use them."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-dictionaries-1
---
in this blog post, I am going to talk about everything about Python dictionaries. how they are created, how to access them, how to add elements to it, how to remove elements from them and some various built-in methods.

**What is a Dictionary?**

A dictionary is a data structure like an array but has clear differences between them. Basically, a dictionary is an unordered pool of items where each item has a key associated with it. This item can be identified as a value of the particular key. In arrays or lists, we had indexes for each element to address each element but here we have the key associated with the element to identify and address a particular element. Compared to arrays dictionaries have to store the key as well in memory rather than just the element in arrays, thus dictionaries consume more memory than arrays.

**Creating Python Dictionary**

There are several ways we can instantiate a python dictionary.

we can create a dictionary by just putting keys and their values inside curly brackets and separated by commas like in the following code snippet.

*[#dictionary](https://www.datainsightonline.com/blog/hashtags/dictionary) initiation*
dictionary = {
 "name": "Isuru Lakshan",
 "age": 25,
 "university": "University of Peradeniya"
}

print(dictionary)

This value can be of any type and can repeat but the keys associated with it should be of immutable types and unique. immutable types are strings, numbers or tuples.

Also, we can create a dictionary using a built-in function called dict(). this is showed below.

dictionary_2 = dict({
 "name": "Isuru Lakshan",
 "age": 25,
 "university": "University of Peradeniya"
})

print(dictionary_2)

**Access elements from a dictionary**

As stated before dictionaries have unique keys associated with every value in it. so we can use it to access a particular value.

We can use the key along with dictionary name like this,

print(dictionary['age'])

There's another way to do this. we can use the get() method to retrieve the values from the dictionary too.

print(dictionary.get('age'))

If a particular key is not found in the given dictionary key error is raised. if we used get() method, none will be returned from the method.

**How to Change and Add elements to a dictionary**

Again we need key for this. we can add an element to a dictionary like this,

*# add item*
dictionary['address'] = 'Colombo Srilanka'

If the newly added key is different from all of the keys currently in the dictionary, a new entry will be added with the new key at the end of the dictionary. if the key is present in the dictionary, the particular value will be updated.

*# update value*
dictionary['age'] = 27

*# output:{'name': 'Isuru Lakshan', 'age': 27, 'university': 'University of Peradeniya'}*
*# age got updated as key is already in the the dictionary*
print(dictionary)

**How to check a given key is in the dictionary**

we can use ' in ' keyword to check whether a particular key is in the dictionary. This is valid only for keys, not values.

*[#key](https://www.datainsightonline.com/blog/hashtags/key) check*

*# Output: True*
print('age' in dictionary)

*# Output: True*
print('studentID' not in dictionary)

*# this checks keys only not values*
*# Output: False*
print('Isuru Lakshan' in dictionary)

**How to remove a key-value pair from a dictionary**

There are several methods to do this.

one way is using pop() method. when we give the key as an argument the particular value will be popped from the dictionary and returned.

*# remove a particular item, returns its value*
*# Output: return the age 27*
print(dictionary.pop('age'))

*# Output: {'name': 'Isuru Lakshan', 'university': 'University of Peradeniya', 'address': 'Colombo Srilanka'}*
print(dictionary)

another method that we can use is popitem() method. this method will remove and return an arbitrary value from the dictionary.

This is showed in following code snippet,

*# remove an arbitrary item, return (key,value)*
*# Output: ('address', 'Colombo Srilanka')*
print(dictionary.popitem())

*# Output: {'name': 'Isuru Lakshan', 'university': 'University of Peradeniya'}*
print(dictionary)

we can use clear() method to remove all items at once from the dictionary.

*# remove all items*
dictionary.clear()

*# Output: {} :- all items deleted, empty dictionary is printed*
print(dictionary)

another method is del(). this method can delete the entire dictionary or particular values from the dictionary.

*# delete the dictionary itself*
del dictionary

*# no dictionry to print so throw an error*
print(dictionary)

I hope this would help you to improve your knowledge. Thank you for reading.
