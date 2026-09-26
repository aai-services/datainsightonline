---
title: "Python Concepts for Data Science: Functions"
author: "Prativa Bhatta"
date: 2022-03-23
description: "A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity and higher level of code reuse for your application. Some..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-concepts-for-data-science-functions-3
---
A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity and higher level of code reuse for your application. Some functions are in built-in and some functions create according to own choice.

**Built-in-function**

Any function that is provided as part of a high-level language can be executed by a simple reference with the specification of the argument. Example(sum):

**Import Numpy**

```python
import numpy as np
a=[1,3,5,7]
```

**Summation**

```python
np.sum(a)
```

**Products**

```python
np.prod(a)
```

**Creating a function**

```python
def cube(x):
result = x*x*x
print(result)
```

**Calling function**

```python
cube(5)
```
