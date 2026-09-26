---
title: "Python Lists"
author: "Yosef Zeru Seyoum"
date: 2021-10-11
description: "IntroductionPython is one of the world's most widely held programming languages, and the reason behind its popular acceptance includes, not limited to:· Use of simple and intuitive syntax which..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-lists-4
---
## Introduction

Python is one of the world's most widely held programming languages, and the reason behind its popular acceptance includes, not limited to:

· Use of simple and intuitive syntax which resembles to simple English

· Python is object-oriented programming language, everything in python considered as an object with different characteristics. Python allows working on various objects.

· Python has features to integrated with different software or components of a software for data cleaning, analysis, and interpretation.

## Lists
There are four built-in data types in python, namely **Lists**, **Tuples**, **Sets** and **Dictionaries**. Lists are mainly used to store multiple items in a single variable.

- Lists are prepared placing all data elements in a square bracket which are separated by comma.

- Single list can contain different data types like float, integer, or string.

- We can place lists inside the list, and it is called nested list.

Example of creating empty list

```python
#Empty List
Departments = []
```

Example of creating a list containing string values

```python
#List Containing departments In the Hospital
Departments = ["OutPatient", "Inpatient", "Dermatology", "STI", "Surgical", "Onchology", "Optalmology"]
print(Departments)
```

Output

```python
['OutPatient', 'Inpatient', 'Dermatology', 'STI', 'Surgical', 'Onchology', 'Optalmology']
```

Examples of lists inside the list...called Nested List

```python
#List containing other lists...Nested List
Departments = ["OutPatient", "Inpatient", "Dermatology", "STI", "Surgical", "Onchology", "Optalmology"]
Departments_2 = [Departments, 4, 5, "Laboratory", "Pharmacy", "ART-Clinic"]
print(Departments_2)
```

Output

```python
[['OutPatient', 'Inpatient', 'Dermatology', 'STI', 'Surgical', 'Onchology', 'Optalmology'], 4, 5, 'Laboratory', 'Pharmacy', 'ART-Clinic']
```

## Accessing Data from Lists

## We do have different types of options to see and manipulate lists in python.

## 1. Indexing

- Lists are saved in ordered form and they are indexed beginning from [0]. This means the 1st data element will be indexed as 0, the 2nd will be indexed as 1.

```python
#Displaying Lists using Indexes
Departments = ["OutPatient", "Inpatient", "Dermatology", "STI", "Surgical", "Onchology", "Optalmology"]
print(Departments[0])
print(Departments[1])
#displaying range of values from the list
print(Departments[0:4])
```

Output

```python
OutPatient
Inpatient
['OutPatient', 'Inpatient', 'Dermatology', 'STI']
```

2. List Length

- To count the number of items in the list we can use len () as shown below.

```python
#To see how many items are in the list
Departments = ["OutPatient", "Inpatient", "Dermatology", "STI", "Surgical", "Onchology", "Optalmology"]
print(len(Departments))
Departments_2 = [Departments, 4, 5, "Laboratory", "Pharmacy", "ART-Clinic"]
print(len(Departments_2))
```

Output

```python
7
6
```

Thank you.
