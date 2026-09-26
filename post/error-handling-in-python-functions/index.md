---
title: "Error Handling in Python Functions"
author: "Musonda Katongo"
date: 2022-10-19
description: "When calling functions, we need to ensure that valid arguments are passed to the function for it to execute correctly. When we write our own functions, we will want to catch specific problems and..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/error-handling-in-python-functions
---
## Table of Contents

1. Introduction
2. Handling Exceptions
3. Raising an Error
4. Conclusion

## 1. Introduction

When calling functions, we need to ensure that valid arguments are passed to the function for it to execute correctly. When we write our own functions, we will want to catch specific problems and print specific error messages that will enable the user to know exactly why the function is not executing.

## 2. Handling Exceptions

An exception is an error that is caught during the execution of a function. The following is an example of a function that returns the square root of a number.

```python
def sq_root(num):
    """Returns square root of a number"""
    return num**0.5

sq_root(25)
```

```python
5.0
```

```python
sq_root('25')
```

```python
-------------------------------------------------------------TypeError                                 Traceback (most recent call last) Input In [33], in <cell line: 1>()
----> 1 sq_root('25')

Input In [31], in sq_root(num)
      1 def sq_root(num):
----> 2     return num**0.5

TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
```

When we pass a positive float or integer the function returns the square root of the number correctly. However, if we pass a string to it, an error is thrown, in this case a TypeError.

When we write our own functions we want to be able to provide error messages that are useful to the user. This is were we employ the try-except clause in which case we will specify within the code what the function should 'try' except in a case were it fails then we return an error message. The following is the code that will print out our custom error message.

```python
def sq_root(num):
    """Returns square root of a number"""
    #the function tries to compute the square root
    try:
        return num**0.5

    #print error message if input is not integer or float
    except:
        print('number must be an integer or float')
```

```python
sq_root(25)
```

```python
5.0
```

```python
sq_root('25')
```

```python
number must be an integer or float
```

## 3. Raising Errors

We note that our square root function will return complex numbers for for negative integers or floats. We only desire that the function only computes square roots for positive numbers. In this case, we might want to raise an error for negative values.

The following code in the function checks first whether the number is positive before proceeding to carrying out the computations. If the number is not positive then a Value error is raised.

```python
def sq_root(num):
    """Returns square root of a number"""

    #check whether number is string
    if type(num)==str:
        #raise typeError
        raise TypeError('number must be an integer or float')

    #check whether number is less than 0
    if num < 0:
        #raise ValueError
        raise ValueError('number must be non-negative')

    #try the computation catching any other exceptions
    try:
        return num**0.5
    except:
        print('number must be an integer or float')
```

Now if we pass a negative number, we will get ValueError with our custom message printed out. If we enter any other input that is not an integer or float we will get the message in the exception printed out which is specified to catch TypeErrors. Let us try the function with the inputs 25, '25' and -25

```python
sq_root(25)
```

```python
5.0
```

```python
sq_root('25')
```

```python
-------------------------------------------------------------TypeError                                 Traceback (most recent call last)
Input In [89], in <cell line: 1>()
----> 1 sq_root('25')

Input In [87], in sq_root(num)
      4 #check whether number is string
      5 if type(num)==str:
      6     #raise typeError
----> 7     raise TypeError('number must be an integer or float')
      9 #check whether number is less than 0
      10 if num < 0:
      11     #raise ValueError

TypeError: number must be an integer or float
```

```python
#raise ValueError for non-negative
sq_root(-25)
```

```python
-------------------------------------------------------------ValueError                                Traceback (most recent call last)
Input In [82], in <cell line: 2>()
      1 #raise ValueError for non-negative
----> 2 sq_root(-25)

Input In [79], in sq_root(num)
      9 #check whether number is less than 0
      10 if num < 0:
      11     #raise ValueError
 ---> 12     raise ValueError('number must be non-negative')
      14 #try the computation catching anyother exceptions
      15 try:

 ValueError: number must be non-negative
```

## 4. Conclusion

Handling errors in our functions allows us control of the arguments that the function should accept and provides for means of providing error messages for those arguments that are not accepted. This provides the user with useful information on how to deal with errors that a function might throw.

The notebook for the code in this writeup can be found on the following [GitHub link](https://github.com/Musonda2day/Error-Handling-in-Python-Functions)
