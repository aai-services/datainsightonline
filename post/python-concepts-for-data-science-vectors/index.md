---
title: "Python Concepts for Data Science : Vectors"
author: "Safia Bashir"
date: 2021-10-05
description: "VectorsIn this tutorial, we will learn about various vector creation methods in Python.Python vectors are one-dimensional arrays that are the most common NumPy data structure.🛑 Do not confuse NumPy..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-concepts-for-data-science-vectors
---
## Vectors
In this tutorial, we will learn about various vector creation methods in Python.

Python vectors are one-dimensional arrays that are the most common NumPy data structure.

🛑 Do not confuse NumPy vectors with mathematical vectors.

Let’s see how they’re created:

## Creation
1-D arrays can be created in many ways, and we can create them based on our needs. Here are some ways to create 1-D arrays:

## Method 1
By entering the individual elements of an array, we can create an array. Here is an example:

```python
import numpy as np
​
x = np.array([1, 3, 5, 7, 9])
print(x)
```

By using the np.array() function with its input argument being a Python list, we are actually converting a Python list into a vector in the above code

**Method 2**

The np.ones(size) function creates an array of the specified size filled with 1. Similarly, np.zeros(size) creates an array of the value 0.

```python
v1 = np.ones(5)
v0 = np.zeros(5)
print(v1)
print(v0)
```

Note: Data type of values inside the vectors generated from ones() and zeros() functions are floating points.

**Method 3**
The arange() function can be used to initialize an array. It can take up to three arguments. np.arange(start, end, step)
The first argument indicates the start point, the second argument indicates the endpoint, and the third argument indicates the step size.

```python
print(np.arange(1, 7)) # Takes default steps of 1 and doesn't include 7
print(np.arange(5)) # Starts at 0 by defualt and ends at 4, giving 5 numbers
print(np.arange(1, 10, 3))   # Starts at 1 and ends at less than 10, with a step size of 3
```

**Method 4**
By using the linspace() function, we can also define an array of equally spaced elements containing both endpoints.
Run the code below to see the implementation of linspace():

```python
print(np.linspace(1, 12, 12))
print(np.linspace(1, 12, 5))
print(np.linspace(1, 12, 3))
```

The juypter notebook related to this post can be found [here](https://github.com/safia-bashir/Python-Concepts-for-Data-Science-Vectors)
