---
title: "Python Concepts For Data Science: lambda expressions"
author: "asma kirli"
date: 2021-09-23
description: "Lambda expression is an anonymous function, it can take any numbers of arguments but can only have one expression returned.Syntax: lambda arguments : expression ---> the expression is executed and..."
categories: ["Python"]
image: images/72a040_5eb91d1a11dd4c0ca45ff4df08858608.webp
wix-url: https://www.datainsightonline.com/post/python-concepts-for-data-science-lambda-expressions
---
![](images/72a040_5eb91d1a11dd4c0ca45ff4df08858608.webp)

**Lambda expression** is an anonymous function, it can take any numbers of arguments but can only have one expression returned.

**Syntax**: lambda arguments :

expression ---> the expression is executed and the result
 is returned in one line

Example01:

```python
#example 01
x=lambda i:i+10
print(x(5))
```

We start by assigning lambda to a value (x here) so that everytime we need it we call x . Here we gave 5 as an argument for x. The result here will be : 15.

Example02: lambda with 2 arguments

```python
#example 02 with 2 arguments
calculate= lambda x,y: x*y
print(calculate(5,9))
```

The result here will be 45.

Example03: lambda with 03 arguments

```python
#example03 with 03 arguments
math_op = lambda x,y,z:x*y+z
print(math_op(2,3,4))
```

The result here will be 10.

The power of lambda is better shown when we use it as an anonymous function in another function

```python
#example04with user function
def multiply (n):
    return lambda x:x*n
double=multiply(2)
print(double(5))
```

So we created a user function called multiply that has 1 argument n. Inside the body of the function we used a lambda function with a single argument x and it will return x\*m

This lambda expression result is just a returning expression for the return statement in the multiply function.

**How we call the function then?**

first we assign it to a variable with an argument n : double = multiply(2) than we print this variable with the x argument. Here it will return 10.

Thank you for reading.

You will find the code below here:

[Github](https://github.com/asmakrl/datacampstd/blob/main/lambda%20function.ipynb)
