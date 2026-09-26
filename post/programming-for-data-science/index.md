---
title: "Python: The Language for Data Science"
author: "Aina Adekunle"
date: 2019-06-21
description: "This will be a series of posts about python - a coding language that is becoming the most popular and how it is used for data science!"
categories: ["Python"]
image: images/a27d24_b0fe6ddbf80649748e1e48d822419f21.webp
wix-url: https://www.datainsightonline.com/post/programming-for-data-science
---
## An Introduction to Python for Beginners

This will be a series of posts about [python](https://www.python.org/) - a coding language that is becoming the most popular and how it is used for data science! Python is an open-source (free) general-purpose (unlimited) programming language created by [Guido van Rossum](https://gvanrossum.github.io//Publications.html) in early nineties. It is a powerful tool that can be used to do practically anything! Python can be used to efficiently perform repetitive tasks (scripting), build responsive websites, create computer software, perform incredible data analysis and train machine learning models. With this immense power, one would (and reasonably so) expect it to be a difficult language to learn. But nope! Python is actually one of the easiest programming languages to not only learn but also read and write.

This is why python is almost always recommended to newbies in programming. Because python has become one of the main skills in demand for the [sexiest job of the 21st century](https://hbr.org/2012/10/data-scientist-the-sexiest-job-of-the-21st-century), this series focuses on using python for data analysis and data science, particularly, for those who are new to programming or who want to learn a new programming language.

This series will consist of 5 sections:

1. Programming in Python for Data Science.
2. Numpy in Python for Numerical Computation.
3. Pandas in Python for Data Manipulation.
4. Matplotlib and Seaborn in Python for Data Visualization.
5. Scikit-learn in Python for Machine Learning.

**Top 5 Books for learning python for data science**

For this section, here are top 5 recommended books for learning to program in python for data science:

1. [Python Data Science Handbook: Essential Tools for Working with Data](https://amzn.to/2XEwCp5)
2. [Data Science from Scratch: First Principles with Python](https://amzn.to/30c9bAQ)
3. [Python Crash Course: A Hands-On, Project-Based Introduction to Programming](https://amzn.to/2LAY7sV)
4. [Python for Data Science For Dummies](https://amzn.to/2LCS33o)
5. [Beginning Data Science with Python and Jupyter: Use powerful tools to unlock actionable insights from data](https://amzn.to/2Ly6e9T)

In case reading from books is not your thing, [DataCamp](https://www.datacamp.com?tap_a=5644-dce66f&tap_s=557125-3912b0) is a good platform for learning through short videos and practical coding exercises. You can check out their course on [Python for data science.](https://www.datacamp.com/courses/intermediate-python-for-data-science?tap_a=5644-dce66f&tap_s=557125-3912b0)

Without any further delay, let us dive right into it!

**1. Programming in Python for Data Science**

### Fundamental Data Types in Python

The power of any programming language is largely dependent on its data structures. Therefore, the ability to wield the power of python is in the understanding of its data types.

### Ints, Floats and Strings

Python can create, store, and manipulate alphanumeric data. In other words, python can be used to work on numbers as well as letters (or alphabets). There are two types of numerical data in Python; integers and floats. The integers (e.g 1, 2, 3, 10, 100, 1000) are whole numbers while floats (e.g 1.2, 2.34, 100.5) are decimal numbers. In Python, we say integers are of type int and floats are of type float. Pretty simple, isn’t it? On the other hand, characters (anything that can be typed on the keyboard with a single keystroke, like a letter, a number, dollar symbol or even a space), words, phrases and sentences are of type str (short for string).

Right from the beginning, it is important to note that everything in python is an object and therefore can have a name. To create and name an integer or a float we just need to write name = value, where **value** is any integer whole number or floating-point number we want and **name** is the name we want to call the integer or float number. Now that is amazing! Unlike some programming languages, whereby you have to declare the type of any objects that you want, python automatically assigns the type dynamically. Similarly, to create and name a string, we need to write name = "value", where **value** is the string and **name** is the name of the string. However, note that the string must be in either single or double quotation marks (‘ ’ or “ ”). The name allows us to call the value anytime we need it just like people call your name anytime they need you. Makes sense, isn’t it?

Python provides the **print** function which enables us to print the value directly or using the name and also the **type** function to display the data type of a value directly or using its name. As you will soon appreciate, a **function** enables us to perform an action or a function like print a value or display the data type. To use (or call) a **function**, we write the name of the **function** with open and closing parenthesis and the name or value inside the parenthesis. For example, print(name) or type(value). Remember that strings should always be in either single or double quotation marks (‘ ’ or “ ”)!

Boolean Type

Python also provides the bool type (True or False), which represents truthfulness. The result of any comparison operation in Python is of type bool. In numeric contexts, False = 0 and True = 1.

### Mathematical Operations in Python

Python supports all basic **arithmetic operations** with integers and floats including addition (**+**), subtraction (**-**), multiplication (\*), division (**/**), modulo (**%**), floor division (**//**) and exponentiation (**\*\***). **Comparison** (or conditional) **operators** are used to compare two values to see whether they are equal (**==**), one is greater than or equal to (**>=**) the other or if they are not equal (**!=**) at all. **Logical operators** are used to combine comparison statements and **Membership operators** are used to test if an object is present in a sequence.

### String Manipulations

Python is a zero-indexed programming language, which means counting starts from 0. Strings are sequences of characters and can be manipulated in many interesting ways in python. Let us see some of them.

### Type Conversion

One of the most interesting things in python is that we can convert (change) from one data type to another very easily using a type constructor; a process called type **casting**. For instance, int() can be used to convert floats and strings of numbers to whole number integers. float() is used to convert to floating-point numbers and str() converts any object to string.

### Container Types in Python

In addition to the fundamental data types Python provides other derived data types, which are containers for the fundamental data types. These include lists, tuples, sets and dictionaries. Together, they offer an incredible structure for data storage and management in python. Do not worry, you will in a very short time understand what I mean by this. We will take a look at them one after another.

### The Python List

A list is a python type that can contain the sequence of any data type in python; ints, floats and strings. Lists are **ordered** type. That is, the items in a list are in the order in which they were added. Because new items can be added to a list and the current items in a list can be changed or completely removed, we say that lists are **mutable**. Lists also allow **duplication** of items. To create a list in python, we simply put the items separated by commas in a square bracket [‘a’, 1, ‘python’, ‘a’, ‘python is awesome!’].

### Immutable Python Tuples

Tuples are like python lists but not completely. They are sequences that can contain any data type including ints, floats and strings. Tuples are **ordered** and also allow **duplication** of items. However, tuples are **immutable** in Python. We can **NOT** change a tuple once it is created. New items can not be added to a tuple. Items can not be changed nor removed. But we can delete the whole tuple. In order to create a tuple in python, we put the items separated by commas in a parenthesis (‘a’, 1, ‘python’, ‘a’).

### Python Dictionary

Dictionaries are **uniquely indexed** collection of objects (any of the data types in python). They allow us to get their **values** (items) by using a **key** (index). Thus, they are a collection of key-value pairs. The keys and values are separated by a colon (:). Dictionaries are **mutable** and can be created with curly braces {key1: value1, key2: value2, key3: value3}.

### The Unique Sets in Python

A set is a collection of **unique** objects (any of the data types in Python). Like python list, the items in a set are **mutable**. Unlike Python lists, sets are **unordered**. To create a set in Python, we put the items separated by commas in curly braces {'a', 1,'python'} or what is called a set constructor, set([‘a’, 1, ‘python’]). Notice that the items have to be in a list for the constructor. Tuples, dictionaries and even lists can also be created using their respective constructor tuple(), dict() and list(). Python sets allow us to perform mathematical set operations like intersection and union.

*To be continued ...*

[Aina Adekunle](https://www.linkedin.com/in/aina-adekunle/)
