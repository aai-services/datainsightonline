---
title: "A simple guide to Lambda Expression in Python"
author: "Aayushma Pant"
date: 2021-10-06
description: "The lambda operator or lambda function used in python can be called a simple function without name. It is generally used when the function is needed for a temporary period of time and is used inside..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/a-simple-guide-to-lambda-expression-in-python
---
The lambda operator or lambda function used in python can be called a simple function without name. It is generally used when the function is needed for a temporary period of time and is used inside the other functions like filter(), map() etc. It reduces the line of code as compared to normal functions. The general syntax of a lambda function is quite simple:

### lambda argument_list: expression

argument_list= represents the comma-separated list of arguments

expression= arithmethic expressions using arguments.

```python
multiply=lambda x,y:x*y
multiply(5,4)
```

Compare to the normal function, the above lambda expression can as be written as:

```python
def multiply(x,y):
    mul=x*y
    return mul
multiply(5,4)
```

Now let's use the map() function to express the lambda function

The map() function can be expressed as shown as below:
**r = map(func, seq)**
It uses two expressions, the first argument is the function and the second argument is a sequence (example list) which are applied to the function.

```python
weight_of_students=[50,55,67,40,43]
height_of_students=[1.82,1.50,1.60,1.55,1.48]
BMI = list(map(lambda x,y: round(x/(y*y),3), weight_of_students,height_of_students))
print("The Body Mass Index of students are",BMI)
```

```python
OUTPUT: The Body Mass Index of students are [15.095, 24.444, 26.172, 16.649, 19.631]
```

```python
a = [21, 51, 12]
b = [-12, -12, 1, 1]
c = [-1, -4, 5, 9]

answer=list(map(lambda x, y, z : 52*x-z/y*z, a, b, c))
print(answer)
OUTPUT:[1092.0833333333333, 2653.3333333333335, 599.0]
```

Hence in this way Lambda expression can be used to optimize and maintain better code efficiency.
