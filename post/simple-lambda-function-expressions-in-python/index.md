---
title: "Simple Lambda Function Expressions in Python"
author: "Umme Rubaiyat Chowdhury"
date: 2021-10-06
description: "When you utilize lambda as an anonymous function inside another function, the power of lambda is better demonstrated.Assume you have a function definition that takes one parameter and multiplies that..."
categories: ["Python"]
image: images/981941_024b42af72cc49209ebc268f4a1ee4a2.webp
wix-url: https://www.datainsightonline.com/post/simple-lambda-function-expressions-in-python
---
![](images/981941_024b42af72cc49209ebc268f4a1ee4a2.webp)

When you utilize lambda as an anonymous function inside another function, the power of lambda is better demonstrated.

Assume you have a function definition that takes one parameter and multiplies that argument by an unknown number:

```python
def myfunc(x):
    return lambda a : a * x
```

I have made a function that always doubles the number you send in using that function definition:

```python
def myfunc(n):
    return lambda a : a * n

dbl = myfunc(3)
print(dbl(6))
```

This is a simple example of the use of lambda function in python. Try to change the arguments and practice by your own.
