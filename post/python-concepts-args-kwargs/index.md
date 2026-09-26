---
title: "Python Concepts: args & kwargs"
author: "Sana Omar"
date: 2021-10-06
description: "Python concepts; *args & **kwargs"
categories: ["Python"]
image: images/82b983_a9661d744e2d459d97412ed87e4b33e5.webp
wix-url: https://www.datainsightonline.com/post/python-concepts-args-kwargs
---
***Concept No1: \*args and \*\*Kwargs:***

![](images/82b983_125f4eb33bc14121b2acef1eb2ce50af.webp)

**Args** and **kwargs** allow you to pass multiple arguments in the case of **args**, or keyword in the case of **kwarg**.

Normally, you can define the function with previous known number of arguments, but what if you want to have it work for unknown number of arguments which will be determine during the runtime. Here comes the functionality of **\*args**.

Lets see a normal function:

```python
def sum(no1, no2):
  return no1 + no2
```

Now, a function with a list of predetermined number of values:

```python
def sum(list_of_no):
  result = 0
  for x in list_of_no:
    result +=x
  return result

list_of_no= [2,5,6]
sum(list_of_no)
```

Despite that this solution allows the user to apply the function for multiple variables, still though it requires the no of variables to be determined previously. Thus, **\*args** come to place.

When passing **\*args** the function will accept any number of variables without predetermination of this number, and then will loop through them successfully.

It does not need to be **args**, it could be any other name, but it needs to have the asterisk as it works to unpack the tuple of variables into single iterable object called **args**. Here we are not passing a list, instead we’re passing three different positional arguments as a tuble, which is immutable object that cannot be modified.

```python
def sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

sum(2,5,6)
```

or, simply:

```python
def sum(*variables):
    result = 0
    # Iterating over the Python variables tuple
    for x in variables:
        result += x
    return result

sum(2,5,6)
```

***Now, what about \*\*kwargs?***

It works just as **\*args**, but instead it accepts any number of keywords or names.

Thus, **\*args** are positional arguments which are declared using the name only, while **\*\*kwargs** are keyword arguments which are declared using a name and a value; it is a **dictionary.**

```python
def keyarguments(a, b, **kwargs):
  print(a)
  print(b)
  print(kwargs)

keyarguments(5,6, third_no = 7, forth_no = 8)
```

the result will be:

```python
5
6
{'third_no': 7, 'forth_no': 8}
```

It turned the last two passed arguments in **keyarguments** function into a name value paired as a dictionary.

*Note: when passing* ***\*\*kwargs****, it should not be before the normal numbers, or else it will raise a syntax error.*

Lets try to iterate over \*\*kwargs as in dictionaries:

```python
def show_data(**kwargs):
    print("\nType of argument:",type(kwargs))

    for key, value in kwargs.items():
        print("{} is {}".format(key,value))

show_data(Name= "sana", Program= "data science", Platform= "Data Insight")
```

The result is:

```python
Type of argument: <class 'dict'>
Name is sana
Program is data science
Platform is Data Insight
```

We can see clearly that type of **\*\*kwargs** is dictionary.

Follow me on Twitter <3 :3

My twitter handle: @SanaOmarO
