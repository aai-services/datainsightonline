---
title: "Python Functions"
author: "Rohit Roy"
date: 2021-10-04
description: "Functions are a group of statements which is used to perform a task.These tasks can repetitive , big task which is divided in smaller chunks of code. Syntax of the Function :def..."
categories: ["Python"]
image: images/22a2e8_66a05013179843d49fa092e10c5134b1.webp
wix-url: https://www.datainsightonline.com/post/python-functions-4
---
Functions are a group of statements which is used to perform a task.These tasks can repetitive , big task which is divided in smaller chunks of code.

Syntax of the Function :

```python
def function_name(parameters):
    code_body
    return_statement(s)
```

The above syntax can be broken into five parts mainly

1. 'def' here is used as a keyword to start a function.
2. 'function_name' is used for uniquely identifying the function with a proper name.
3. Parameter are nothing but the arguments which are passed inside the code_body to perform a certain task and is optional.
4. 'code_body' block of codes telling the function what exactly to do .
5. 'return _statement' is optional and is being used to return value of function.

For Example of Simple Function

```python
def tell_me_yourname(name):
    print("Hi ! My name is "+ name)
```

This function will print a name which has been assigned by the user in the variable name.

How to call a function ?

Calling the function is very easy and let you re-use the code.All you have to do is take the name of the function and use it appropriate parameters.

For Example:

```python
>> tell_me_yourname(Roy)
Hi ! My name is Roy
```

Return Statement
It 's one of the statement which is used return the value which has been passed by going back to starting point that is "def" followed by function_name. The idea here is to exit and re - run the code as per the convenience of the user.

For Example:

```python
def real_value(a,b):
    if a>0:
     return a
    else a<0:
     return -b

print ((real_value(4,-9))

Output:
4
-9
```

**Types of Functions**
1.User Defined Functions

2.Built-In Functions

What we have just seen are "User Defined Functions" as user is directly in control how he wants execute the things.

Built-In Functions are which performs certain tasks in python just calling out the names of function. For example dict() - creates dictionary in python, float()- returns floating point number from string/number etc.

![](images/22a2e8_66a05013179843d49fa092e10c5134b1.webp)

I hope you are cleared with functions check out the code provide in the link for more [information](https://github.com/rohitroycanny/adventures/blob/main/Functions%20Explained.ipynb).
