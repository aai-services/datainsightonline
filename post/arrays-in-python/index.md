---
title: "Arrays in Python"
author: "Marehan Refaat"
date: 2022-02-06
description: "The idea of arrays comes from that we have multiple variables of the same type and we want to put them together like this name1 = 'Ahmed' name2 = 'Ali' name3 = 'Manar'We put them in one array called..."
categories: ["Python"]
image: images/d86598_17bae26a63a34d61bb90e772a0a0333e.webp
wix-url: https://www.datainsightonline.com/post/arrays-in-python
---
The idea of arrays comes from that we have multiple variables of the same type and we want to put them together like this

```python
name1 = 'Ahmed'
name2 = 'Ali'
name3 = 'Manar'
```

We put them in one array called "names"

```python
names = ['Ahmed','Ali','Manar']
```

## Access the Elements of an Array
You refer to an array element by referring to the index number.

```python
x = names[1]
print(x)
Ali
```

## Modify a value in the array
```python
names[0] = "John"
print(names)
['John', 'Ali', 'Manar']
```

## The Length of an Array
Use the len() method to return the length of an array (the number of elements in an array).

```python
x = len(names)
print(x)
3
```

## Looping Array Elements
You can use the for in loop to loop through all the elements of an array.

```python
for i in names:
  print(i)
John
Ali
Manar
```

## Adding Array Elements
You can use the append() method to add an element to an array.

```python
names.append("Hoda")
print(names)
['John', 'Ali', 'Manar', 'Hoda']
```

## Removing Array Elements
You can use the remove() method to remove an element from the array.

```python
names.remove("Hoda")
print(names)
['John', 'Ali', 'Manar']

You can refer to the code form here
```
