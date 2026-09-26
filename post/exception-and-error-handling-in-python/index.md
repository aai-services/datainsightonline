---
title: "Exception and Error Handling in Python"
author: "arijbentej"
date: 2021-10-12
description: "Every programmer has faced many errors. Facing bugs and dealing with them is very important to learn more and become a better programmer. In this post, we will see together the different types of..."
categories: ["Python"]
image: images/c10f9f_67143ad46ef74c839a82b6aa12fbfa21.webp
wix-url: https://www.datainsightonline.com/post/exception-and-error-handling-in-python
---
![](images/c10f9f_67143ad46ef74c839a82b6aa12fbfa21.webp)

Every programmer has faced many errors. Facing bugs and dealing with them is very important to learn more and become a better programmer.

In this post, we will see together the different types of errors and how to deal with them. First of all, we will start by defining the mainly two types of errors. Then, we will understand the different types of exceptions that we can face while coding and how to deal with these situations.

## 1) Introduction

There are two main types of errors that every one of us can face:

**Syntax errors:** It occurs when you don't respect the rules while writing your code. For example, when you forget to put a colon ':' after the while statement as shown in the code below:

In the case of a syntax error, the code does not execute until the error is fixed. We can see that the line of error is indicated with an arrow pointing to the place where the error was detected.

**Exceptions:**

Some times, your code syntax can be correct but while execution an error still throwing up. These errors detected during execution are called *exceptions* and dealing with them is called exception Handling. We will see some of exception types and how to deal with these errors.

## 2) Different type of Exceptions

There are some native Exceptions and these are some examples:

**Name Error:** When a name is not found. This error appears.

**ZeroDivisionError:** It is raised when we try to divide by zero.

**ValueError:** When an expression or a function receives the correct type but an an inappropriate value.

**TypeError:** It is thrown when we use an object with the wrong type.

The code below show some examples of these exceptions:

[#Output](https://www.datainsightonline.com/blog/hashtags/Output)

```python
-------------------------------------------------------------NameError   Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_15576/557461111.py in <module>
----> 1 print(z)
NameError: name 'z' is not defined
```

```python
-------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_15576/4252762792.py in<module>
      3
      4
----> 5 print(divide(7,0))~\AppData\Local\Temp/ipykernel_15576/4252762792.py in divide(a, b)
1 def divide(a,b):
----> 2     return a/b
      3
      4
      5 print(divide(7,0))
ZeroDivisionError: division by zero
```

```python
-------------------------------------------------------------ValueError               Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_15576/1550433386.py in <module>
      1 import math
      2
      ----> 3 math.sqrt(-1)
ValueError: math domain error
```

```python
-------------------------------------------------------------TypeError                 Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_15576/1342124575.py in <module>
----> 1 print(divide('i',10))
~\AppData\Local\Temp/ipykernel_15576/4252762792.py in divide(a, b)
      1 def divide(a,b):
      ----> 2     return a/b
      3
      4
      5 print(divide(7,0))
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

There are other native exceptions that you can check them [here](https://docs.python.org/fr/3/library/exceptions.html#bltin-exceptions).

## 3) Handling exceptions

We can handle exceptions using **try** and **except** statement. The try clause will be executed first, if no exceptions occurred then the except is skipped.

This is an example of exceptions handling in Python:

[#Output](https://www.datainsightonline.com/blog/hashtags/Output):

5.0

Can't divide by Zero

None

References:

<https://docs.python.org/3/library/exceptions.html>

<https://docs.python.org/3/tutorial/errors.html>
