---
title: "Explanation of Functions in Python"
author: "Hamza Khalid"
date: 2021-09-14
description: "Functions in python are block of code which are only used when they are called and it also helps in reusability of code. Functions are also called with no parameters or giving parameters having some..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/explanation-of-functions-in-python
---
### Functions in python are block of code which are only used when they are called and it also helps in reusability of code. Functions are also called with no parameters or giving parameters having some return back from the function like information can be passed as arguments.
Initiating a function using def and using pass for initiating an empty function.

```python
# Syntax of Initiating a Function
def func1():
    pass

# Pass is used for initiating an empty function
```

Lets print something in the function and then call the function.

```python
def func1():
    print('Hamza Khalid')
# Now Call the function below which will give Hamza Khalid as output when executed.
func1()
```

Now Lets check about arguments / passing parameters in functions.

```python
# Passed 2 paramters a,b in function as arguments
def func1(a, b):
    return a+b
# Printing func1(2,3) in print function becuse it will return a value and 2 and 3 respectively are parameters.
print(func1(2,3))
```

Functions can be used in many ways and are useful for code reusability.

Regards,

Hamza Khalid
