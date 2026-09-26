---
title: "Python Concepts for Data Science: Lists and Dictionaries"
author: "cheikhbadiane99"
date: 2022-05-30
description: "Python is one of the most used language in data science. In this post, i'll be talking about lists and dictionaries in Python.Lists in PythonLists in Python are one of the 4 built-in data types that..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-concepts-for-data-science-lists-and-dictionaries
---
Python is one of the most used language in data science. In this post, i'll be talking about lists and dictionaries in Python.

### Lists in Python

Lists in Python are one of the 4 built-in data types that we can use to store collections of data.

#### How to create a list in Python

***Lists are changeable, ordered and can take dublicate values.***

We can print out the values of the list by using print.

### Get a random Element from a list

### Get multiple random elements from a list

Suppose i want to get randomly 3 elements from my list.

### Adding a list to an existing list by using the Append method.

And we can see a new list added to the existing list.

### Adding elements to the list by using Extend methode

And when we print the list1 again, we see tree new elements added on it.

We can also count the number of elements of the list using the Len function.

### Dictionaries in Python

In Python, dictionaries are used to store data in key:value pairs. Unlike lists, dictionaries in Python do not accept duplicates.

A dictionary can store any kind of data type.

Let's print out the output of our dictionary.

### Example of Dictionary in real word project

In the example below, a have a column (**Primarypropertytype**) in my dataset with many values. I have 32 types of Appartments and i create a dictionary to group these 32 types of appartments into 7 groups.

In the example below, a have a column (**Primarypropertytype**) in my dataset with many values. I have 32 types of Appartments and i create a dictionary to group these 32 types of appartments into 7 groups.

Now let's create a dictionary to group all these 32 small propertytypes into 7 groups and assign these 7 groups as the new values of the Primarypropertytype column values of our dataset.

I can now use the Map function to group all these 32 values of the Primarypropertytype column into only 7 values for this column in my dataset.

And we can see that the Primarypropertype has now only 7 unique values.

Thank you
