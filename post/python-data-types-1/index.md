---
title: "Python Data Types"
author: "Yosef Zeru Seyoum"
date: 2021-10-11
description: "IntroductionPython is becoming one the widely used and acceptable data science tool worldwide due to its open-source nature plus stability and can be executed in Windows, Linux, or MAC operating..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-data-types-1
---
## Introduction

Python is becoming one the widely used and acceptable data science tool worldwide due to its open-source nature plus stability and can be executed in Windows, Linux, or MAC operating systems.

Three common applications of python are, but not limited to:

A. Data Science with scopes of machine learning, data analysis and visualization.

B. Web Development and

C. Scripting.

Python has different built-in functions which simplifies our codes or data manipulation activities. From these built-in things in python knowing data types is vital. According to Wikipedia a data type is a classification of data which tells the compiler or interpreter how the programmer intends to use the data. Understanding data types ensures that data is collected in the preferred format and the value of each property is as expected.

Data Types in Python

Data types in python classified in to five major categories, two of them will subcategorized in to additional three types as follows.

A. Numbers

I- Integer

II- Float

III- Complex Number

B. Dictionary

C. Boolean

D. Set

E. Sequence

I- Strings

II- Lists

III- Tuples

Let us see some examples for numbers and dictionaries.

A. Numbers

- Numeric data types help us to deal with numbers of any type. This includes integers, floats and complex numbers.

Example of integers

```python
#Declare and print Integers
a=8
print(a)
```

Output

```python
8
```

We use the syntax type() to display the type of object we declared or listed as shown below.

```python
#To know What type of Data is a
print(type(a))
```

Output

```python
<class 'int'>
```

- Integers are non-decimal numbers and can be Positive or Negative, whereas floats are decimal numbers.

- integers can be converted to float and the vise versa.

```python
# TO Change a from integer to float
print(float(a))
```

Output

```python
8.0
```

- Complex number is a number that can be depicted as a + bi and python has functionality to handle and execute these numbers.

- Complex numbers contains both real and imaginary numbers.

[#Complex](https://www.datainsightonline.com/blog/hashtags/Complex) Numbers

```python
#Complex Numbers
#Declare Variables
x = 5
y = 9
#Syntax for Complex Numbers
B = complex(x, y)
#Print Real and Imaginary Numbers
print(B.real)
print(B.imag)
#Print the Data Type Complex
print(type(B))
#Convert to String
print(str(B))
```

Output

```python
5.0
9.0
<class 'complex'>
(5+9j)
```

B. Dictionary

Dictionaries are used to store values in python in a forms of keys and values as pair. They are ordered like lists, but doesn’t allow duplicates.

- Dictionaries used curly braces to create list.

- The syntax for dictionaries will looks like

My_dict = {“Key1” : Value1,

“Key2” : Value2}

Example

```python
#Creating of a dictionary which contains Continent_Name and Country Name
Cont_Country = {"Continet" : "Africa", "Country" : "Ethiopia"}
print(Cont_Country)
Cont_Country = {"Africa" : "Ethiopia", "Asia" : "China", "Africa" : "Angola", "Africa" : "Sierra Leone", "Middle East" : "Israel"}
print(Cont_Country)
print(type(Cont_Country))
```

Output

```python
{'Continet': 'Africa', 'Country': 'Ethiopia'}
{'Africa': 'Sierra Leone', 'Asia': 'China', 'Middle East': 'Israel'}
<class 'dict'>
```

Thank you.
