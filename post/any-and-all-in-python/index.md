---
title: "any and all in python"
author: "aya abdalsalam"
date: 2022-01-22
description: "any vs all and or vs and"
categories: ["Python"]
image: images/d803c7_269ef9da811041958d30787d918675ac.webp
wix-url: https://www.datainsightonline.com/post/any-and-all-in-python
---
> Any and or are two built in functions in python Both functions are equivalent to writing a series of or , and operators respectively between each of the elements of the passed iterable

## The or operator

```python
x = 6
y = 7
z = 8
print((x >= 3 ) or (y >= 6 ) or (z > 7))
True
print((x == 3 ) or (y >= 6 ) or (z == 7))
True
print((x == 3 ) or (y == 6 ) or (z < 7))
False
```

As we see in the previous examples if any of the part of the code is True the all of the sentence is treated as true and if all the parts are false the all is treated as False so we can use another functions which can help us and make code small and not repeat any part of the code We use ***any*** and use iterable as list to loop over it

```python
print(any([x >= 3, y >= 6, z > 7]))
True
print(any([x == 3, y >= 6, z == 7]))
True
print(any([x == 3, y == 6, z < 7]))
False
```

## The and operator

```python
x = 6
y = 7
z = 8
print((x >= 3 ) and (y >= 6 ) and (z > 7))
True
print((x == 3 ) and (y >= 6 ) and (z == 7))
False
print((x == 3 ) and (y == 6 ) and (z < 7))
False
```

if all the parts are true the output is true

else it false

but there exist a function which like any make code small and easy called **all**

```python
print(all([x >= 3, y >= 6, z > 7]))
True
print(all([x == 3, y >= 6, z == 7]))
False
print(all([x == 3, y == 6, z < 7]))
False
```

#### *Note:*
##### 1- while using dictionary

it evaluate the value of the key not the value

Let's see example

```python
dict = {True : True, False: True,True:True,False:True}
print(any(dict))
print(all(dict))
True
False
```

As we noticed that all the values of the dict is True but it print True in the second case of use all because it not care about what is exist in value it only see the key

```python
2- Empty iterable
In case of any it print false and in case of all it will print True
print(any([]))
print(all([]))
False
True
```
