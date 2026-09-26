---
title: "Modules in python"
author: "Imene Maallem"
date: 2021-10-18
description: "A python module can be described as a python program file which contains a python code including python functions, class, or variables. In other words, It can be said that a python code file saved..."
categories: ["Python"]
image: images/e0a26d_4a2b5f0dfc8a4208b3bbf7d742eb25d3.webp
wix-url: https://www.datainsightonline.com/post/modules-in-python
---
![](images/e0a26d_4a2b5f0dfc8a4208b3bbf7d742eb25d3.webp)

A python module can be described as a python program file which contains a python code including python functions, class, or variables. In other words, It can be said that a python code file saved with the extension (.py) is treated as the module. We may have a runnable code inside the python module.

Modules in Python provides us the flexibility to organize the code in a logical way.

To use the functionality of one module into another, we must have to import the specific module. *a module in python, is python file with py extension it is like a section of a physical library it contains functions that are related to one another*

*[#We](https://www.datainsightonline.com/blog/hashtags/We) use these modules to break down large program into small manageable and organized files module allows reusability of code. For example*

Example

In this example, we will create a module named as file.py which contains a function func that contains a code to print some message on the console.

*:*

```python
# Function takes in 2 numbers and returns their sum :
def add(x,y):
    Result =x+y
    return(Result)
print(add(5,6))
11
```

```python
#We can import a module by renaming it as follows:
import math as m
print("the value of pi is" , m.pi)
# We renamed math module as m
the value of pi is 3.141592653589793
```

```python
#We can also import specific names from module without importing the whole module
from math import pi
print("the value of pi is", pi)
#We imported only the pi attribute from math module
the value of pi is 3.141592653589793
```

```python
# We can also  import all names from module using this syntax:Import all names from standard
from math import *
print("the value of pi is" , pi)
the value of pi is 3.141592653589793
```
