---
title: "Python Concepts for Data Science: Errors and Exceptions"
author: "ben othmen rabeb"
date: 2021-09-21
description: "Errors are the problems in a program due to which the program will stop the execution. On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the..."
categories: ["Python"]
image: images/bfaec5_a1eb42e4f2f64aac943fcdba58609bb0.webp
wix-url: https://www.datainsightonline.com/post/python-concept-for-data-science-errors-and-exceptions
---
![](images/bfaec5_a1eb42e4f2f64aac943fcdba58609bb0.webp)

Errors are the problems in a program due to which the program will stop the execution. On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the program.

**Two types of Error occurs in python**

1. Syntax errors
2. Logical errors (Exceptions)

## Syntax errors
When the proper syntax of the language is not followed then syntax error is thrown.

**Example**

```python
# initialize exam score
x = int(input("What is your exam score?"))

# check  whether the student has passed their exam or not
if(x>=10)
    print("Congrats! you succeed ")
else print("You did not pass the exam")
```

**this code returns a syntax error message because after if statement a colon : is missing.**

![](images/bfaec5_3dafe1d49b5c4d3bba5f1194dc766ca7.webp)

## logical errors(Exception)
Here’s a list of the common exception you’ll come across in Python:

- **ZeroDivisionError**: raised when you try to divide a number by zero
- **IndexError**: Raised when the wrong index of a list is retrieved.
- **AssertionErrorIt** Raised when assert statement fails.
- **AttributeErro**r Raised when an attribute assignment is failed.
- **ImportError**: Raised when an imported module is not found.
- **KeyError** Raised when the key of the dictionary is not found.
- **NameError** Raised when the variable is not defined.
- **TypeError** Raised when a function and operation is applied in an incorrect type.
- **MemoryError** Raised when a program run out of memory.
- **ValueError**: Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified
- **Exception**: Base class for all exceptions. If you are not sure about which exception may occur, you can use the base class. It will handle all of them.

**Example1: ZeroDivisionError**

```python
# initialize the amount variable
marks = 10000

# perform division with 0
a = marks / 0
print(a)
```

![](images/bfaec5_291e3e544d2241b48f70218a82ffdaf4.webp)

**Example2: Index Error**

```python
#initialize a list
a = [1, 2, 3]
print (a[3])
```

![](images/bfaec5_c2ac3651153e407cb3fe2da359632e03.webp)

**Example3: AttributeError**

```python
class Attributes(object):
    pass

object = Attributes()
print (object.attribute)
```

![](images/bfaec5_263a08a4f41c421995913a954203861a.webp)

**Example4: ImportError**

```python
import module
```

![](images/bfaec5_439b96e0edef463286714b66b615c2ce.webp)

**Example5: KeyError**

```python
array = { 'a':1, 'b':2 }
print (array['c'])
```

![](images/bfaec5_0dabc38f40b449df873b4ee29ce34e18.webp)

**Example6: NameError**

```python
def func():
    print (ans)

func()
```

![](images/bfaec5_04a6855ac7764bcc82bdc7c57278d6cd.webp)

**Example6: TypeError**

```python
arr = ('tuple', ) + 'string'
print (arr)
```

![](images/bfaec5_112eec64c75e4c1ab48e2a4f40ef2004.webp)

**Example7: ValueError**

```python
print (int('a'))
```

![](images/bfaec5_877f1a36bff141ffa66dbf2524784888.webp)

## Error Handling

When an error and an exception is raised then we handle them with the help of handling methods.

**Handling Exceptions with Try/Except/Finally**

We can handle error by Try/Except/Finally methods. We write unsafe code in the try, fall back code in except and final code in finally block.

```python
# put unsafe operation in try block
try:
     print("code start")

     # unsafe operation perform
     print(1 / 0)

# if error occur the it goes in except block
except:
     print("an error occurs")

# final code in finally block
finally:
     print("GeeksForGeeks")
```

![](images/bfaec5_94eff4c4c0eb44ff879b9827514b2b7f.webp)

```python
try:
    a = 10/0
    print (a)
except ArithmeticError as e:
        print ("This statement is raising an arithmetic exception.")
        print(e)
else:
    print ("Success.")
```

![](images/bfaec5_beb9c6e4b9124ba99c02cc7fa4b8bcf8.webp)

Thank you for regarding!

You can find the complete source code here [Github](https://github.com/rabebbenothmen/Data-Insight2021/blob/main/Assignments/4-Python%20Concept%20for%20Data%20Science%20Errors%20and%20Exceptions%20.ipynb)
