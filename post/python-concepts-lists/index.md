---
title: "Python Concepts: Lists"
author: "mrbenjaminowusu"
date: 2021-10-08
description: "A list is an in-built datatype in python used to store a collection of data. a list can be written as a sequence of comma-separated values between square brackets. An important aspect of lists is..."
categories: ["Python"]
image: images/996a18_311097bc86af453a8e3c9d4db709810a.webp
wix-url: https://www.datainsightonline.com/post/python-concepts-lists
---
A list is an in-built datatype in python used to store a collection of data. a list can be written as a sequence of comma-separated values between square brackets. An important aspect of lists is that the items in a list do not need to be of the same type. This means a list can contain strings, integers and floats. Below are three examples of a list. The **list_a** contains a sequence of strings, **list_b** contains a series of integers of the multiples of 2 and **list_c** contains a mixture of string, integer and float.

```python
list_a= ['school', 'clinic',' church', 'cinema', 'stadium']
list_b= [2,4,6,8,10,12,14,16,18,20]
list_c= [0.25,80,'people']
```

**Accessing values in a list**

The values in a list can be accessed by using square brackets to slice along with the index or indices to obtain the value available at that index. An index is the position of a value in a list. An index of a value in a list starts from zero. Hence the first value of any list has an index of zero.

For example, using the list examples above, we execute the following codes:

```python
print(list_a[3])
print(list_b[5])
print(list_c[0])
print(list_b[2:6])
```

when the above code is executed, it produces the following results:

```python
cinema
12
0.25
[6, 8, 10, 12]
```

The string 'cinema' corresponds to the fourth value in list_a, the integer 12 corresponds to the sixth value in list_b, the float 0.25 corresponds to the first value of list_c and the list [6,8,10,12] is the third value to the sixth value in list_b. Note the sixth value is not the same as the 6th index.

**Changing elements in a list**

We can change elements of a list either by giving the index or the slice on the left-hand side of the assignment operator. Single or multiple elements in a list can be changed. Examples below

```python
list_a[1]= 'hospital'
print(list_a)
list_b[2:5]=[7,9,11]
print(list_b)
```

When list_a and list_b is recalled again, it executes the below outputs,

```python
['school', 'hospital', ' church', 'cinema', 'stadium']
[2, 4, 7, 9, 11, 12, 14, 16, 18, 20]
```

The **del** statement can be used to remove values in a list provided you know which element you are deleting.

```python
del list_b[2:5]
list_b
```

**Basic List Operators**

Here we look at 3 basic list operations. That is +, \*, and in. This means concatenation, repetition and members. Concatenation in lists ads the elements of one list to another list. Repetition is means duplicating the elements of the list by how many times you choose. Members return a Boolean value of True or False if the element is in the list or not. Below are illustrations

```python
list_1=list_a + list_b
print(list_1)

list_2= list_c*4
print(list_2)

'church' in list_a
```

**List Functions**

Python has the following list fuctions.  **len()**, **max()**, **min()** and **list().**

The **len()** function returns the number of elements in the list. The **max()**  function returns the maximum value in the list. The **min()**  function returns the minimum value in the list. The **list()** function takes a sequence type and converts it into a list. This is used to convert tuples into a list.

```python
print(len(list_b))
print(max(list_a))
print(min(list_b))
print(list(range(5)))
```

When this is executed, it produces the following outputs:

```python
7
stadium
2
[0, 1, 2, 3, 4]
```

7 is the number of elements in the modified list_b list. Stadium has the highest number of characters in the modified list_a. 2 is the smallest number in list_b. [0, 1, 2, 3, 4] is the converted list of the range of values of 5.

**List Methods**

Methods are pieces of reusable code that belong to a particular Datatype. We call methods with a dot on the datatype passed on the object you want. This applies to list methods. We look at some of the most used list methods below.

**List append() Method:** This adds a new object or element to the back of a list. This is used to update and change a list. The syntax and an example are below. We append **list_a**  with the string 'factory'

```python
list.append(obj)

list_a.append('factory')
```

**List count Method:**  This returns the number of times an element occurs in a list. The syntax and example are below. We count the number of times the float 0.25 appears in the list_2

```python
list.count(obj)

list_2.count(0.25)
```

**List sort Method:** This sorts the items of the list in ascending order by default. It has a reverse parameter which set to True can sort the elements of list in descending order. Here we sort the items in list_a in ascending order.

```python
list.sort()

list_a.sort()
```

**List index Method:** This returns the index of the object in a list. If the object is not found in the list, it raises an exception indicating the value is not found. For this method, we create a new list called countries. We call the index method on the string 'Ghana'.

```python
list.index(obj)

countries=['Germany','Japan','Russia','Brazil','Congo', 'Italy', 'Ghana','Spain','Iran' ]
countries.index('Ghana')
```

**list insert Method:**  this inserts an object at a specific index. The insert method has two parameters. The index, where you want the object to be inserted and the object, the element to be inserted into the given list. Using the countries list, we insert the string 'China' into the 7th index.

```python
list.insert(index,obj)

countries.insert(7,'China')
```

**List pop method:** this method on its own removes and returns the last object on its own or given the index of an element, it removes and returns the element at that index. The index parameter is optional. Using the countries list, we call the pop method on it without an index parameter and with an index parameter.

```python
list.pop(index)

countries.pop()
print(countries)

countries.pop(4)
print(countries)
```

List remove method: This method removes a given object from a list. This method has the object parameter that is the value you want to remove. Note, in instances where there are multiple occurrences of particular elements in a list, the remove method deletes the first occurrence in the list.

```python
list.remove(obj)

countries.remove('Ghana')
print(countries)
```

**Iteration of Lists**

Elements in a list can be iterated. The first value in a list is assigned to the iterating variable. Next, the statement block is executed and so on. Each item in the list is assigned to the iterating value until the sequence is exhausted. Below is the syntax and an example iterating with the for statement.

```python
for iterating_var in list:
    statement(s)

for x in countries:
    print(x)
```

When the above code is executed it produces the following result

```python
Germany
Japan
Russia
Brazil
Italy
China
Spain
```

References:

[Python Tutorial (tutorialspoint.com)](https://www.tutorialspoint.com/python/index.htm)
