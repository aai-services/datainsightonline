---
title: "Python Try Except"
author: "Abhishek Tuladhar"
date: 2021-10-05
description: "While executing a python program, one may encounter several errors and exceptions. Errors are the problem that will cause the program execution to stop while exceptions are raised when some event..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-try-except
---
While executing a python program, one may encounter several errors and exceptions. Errors are the problem that will cause the program execution to stop while exceptions are raised when some event changes the normal flow of the program. These exception errors can be: IOError, KeyboardInterrupt, ValueError, EOFError, etc.

But with the help of the Try and Except statement, these exception errors can be easily tackled without affecting the flow of the program.

Syntax:

```python
try:
    # Some Code
except:
    # Executed if error in the try block
```

The try block is used to check some code for errors i.e. the code inside the try block will execute when there is no error in the program. Whereas the code inside the except block will execute whenever the program encounters some error in the preceding try block.

Example:

```python
def divide(x, y):
    try:
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")

divide(3, 2)

divide(3, 0)
```

Output:

```python
Yeah ! Your answer is : 1
Sorry ! You are dividing by zero
```

In the above example, with the first function call *divide(3, 2)***,** the try() clause was executed as no exceptions were raised. However, for the second function call *divide(3, 0)*, the except() clause was run as the exception was raised.

**Else clause:**

The try and except statement can be further extended by adding the Else clause, which is only executed if the try block does not raise an exception.

Syntax:

```python
try:
    # Some Code
except:
    # Executed if error in the
    # try block
else:
    # execute if no exception
```

Example:

```python
def divide(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print "Denominator is zero."
    else:
        print c

divide(2.0, 3.0)
divide(3.0, 3.0)
```

Output:

```python
-5.0
Denominator is zero.
```

**Finally**

The **finally** block, if specified, will be executed regardless if the try block raises an error or not.

Syntax:

```python
try:
    # Some Code
except:
    # Executed if error in the try block
else:
    # execute if no exception
finally:
    # Some code .....(always executed)
```

Example:

```python
try:
    k = 5//0
    print(k)

except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print('This is always executed')
```

Output:

```python
Can't divide by zero
This is always executed
```
