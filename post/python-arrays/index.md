---
title: "Python Arrays"
author: "Bechir Mathlouthi"
date: 2021-10-06
description: "An array is a special variable, which can hold more than one value at a time. If you have a list of items (a list of student names, for example), storing the students in single variables could look..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-arrays
---
An array is a special variable, which can hold more than one value at a time. If you have a list of items (a list of student names, for example), storing the students in single variables could look like this:

```python
student1 = "john"
student2 = "jimmy"
student3 = "chris"
```

but what if you had not 3 students, but 500 and you want to loop through students and find a specific one

An array can hold many values under a single name, and you can access the values by referring to an index number.

## Access the Elements of an Array:
ou refer to an array element by referring to the *index number*.

```python
Get the value of the first array item:
x = student[5]
```

## The Length of an Array:

Use the len() method to return the length of an array (the number of elements in an array).

```python
Return the number of elements in the students array:
x = len(students)
```

## Looping Array Elements :
You can use the for in loop to loop through all the elements of an array.

```python
Print each item in the cars array:
    for x in cars:
     print(x)
```

## Adding Array Elements :
You can use the append() method to add an element to an array.

```python
Add one more element to the cars array:
students.append("Bechir")
```

## Removing Array Elements :
You can use the pop() method to remove an element from the array.

```python
Delete the second element of the students array:
students.pop(1)
```

## Conclusion :

An array is a collection of items stored at contiguous memory locations, and it allows to manipulate a lot of items
