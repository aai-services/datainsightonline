---
title: "Python Concepts for Data Science: The Eval and Exec Functions"
author: "Pyae Phyo Kyaw"
date: 2021-09-30
description: "Python's input function produces a string from the user's keyboard input. If we wish to treat that input as a number, we can use the int or float function to make the necessary conversion:Here..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-concepts-for-data-science-the-eval-and-exec-functions
---
Python's **input** function produces a string from the user's keyboard input. If we wish to treat that input as a number, we can use the **int** or **float** function to make the necessary conversion:

Here, whether the user enters 2 or 2.0, 'x' will be a variable with type floating point.

```python
Please enter a number: 2
x =  2.0 type:  <class 'float'>
```

**What if we wish 'x' to be of type integer if the user enters 2 and 'x' to be floating point if the user enters 2.0?**

#### eval Function

Python's **"__builtins__"** module provides an function named **eval** that attempts to evaluate a string in the same way that the interactive shell would evaluate it.

when the user enters the text consisting of a single digit 10, the **eval** function interprets it as integer 10 and assigns an integer to the variable x1.

1. when user enters a single digit 5, the **eval** function interprets it as integer 5 and assigns an integer to the variable x1
2. When the user enters the text 5.0, the assigned variable is a floating-point variable.
3. For x3, the user supplies the string "Python", and the variable’s type is string.
4. When user enters x1. The **eval** function evaluates as a reference to the variable x1 which reference to the integer 5
5. When user enters x6. the **eval** function treats x6 as a name and attempts to evaluate it. Since no variable named x6 exists, the eval function prints an error message

User could enter multiple entries separated by commas, and the **eval** function would evaluate the text typed by the user as Python tuple.

### exec Function

The **exec** function, also from the **__builtins__** module, is similar to the **evel** function. The **exec** function accepts a string parameter that consists of a Python source statement. The **exec** function interprets the statement and executes it.

When we execute the codes, the program will be looping until 'exit()' commit is entered.

[Source Codes can be found here](https://github.com/DoublePK/DataScientistProgramAssignments/blob/master/Python%20eval%20and%20exec%20Function.ipynb)
