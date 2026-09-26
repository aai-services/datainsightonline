---
title: "Use Cases of the Python Lambda Function"
author: "rubayat tithi"
date: 2021-10-04
description: "Python is an object-oriented programming language. Like all other programming languages such as C, C++, Dart, and even Java has a lambda function in its syntax. Python lambda functions are anonymous..."
categories: ["Python"]
image: images/00cdd5_9d697293de0a43568986e0be2a38f9ba.webp
wix-url: https://www.datainsightonline.com/post/use-cases-of-the-python-lambda-function
---
![](images/00cdd5_9d697293de0a43568986e0be2a38f9ba.webp)

Python is an object-oriented programming language. Like all other programming languages such as C, C++, Dart, and even Java has a lambda function in its syntax.

Python lambda functions are anonymous in behavior and can take any number of arguments with a single expression.

Python lambda functions are anonymous in behavior and can take any number of arguments with a single expression. In this article, we will learn about one fundamental python syntax.

1. Lambda function

**Short Story of Lamda Function:**

Before starting to learn a new concept it is wise to know its history like how it came to be in the first place, who, and how it was developed.

Every tree has its root. Python and any other object-oriented programming language that supports lambda expressions have their root in lambda calculus. Basically, lambda calculus is a computational model developed by Alonzo Church. The inventor systematized the [lambda function](https://en.wikipedia.org/wiki/Lambda_calculus) based on pure abstraction.

Python is was not a functional language from the beginning. But later in 1994, it has adopted functions like [reduce()](https://realpython.com/python-reduce-function/#:~:text=Python's%20reduce()%20is%20a,to%20a%20single%20cumulative%20value.) , [filter()](https://www.geeksforgeeks.org/filter-in-python/), and lambda.

**Syntax:**

The basic python function looks like below code snippet.

```python
>>> def test(x):
...     return x
```

Here, a function 'test' is returning its argument 'x'.

Lambda expression for this regular function will be,

```python
>>> lambda x: x
```

The expression is composed of,

1. Keyword: lambda
2. Argument: x
3. Body: x

Let me elaborate on this code with a bit for you. I am adding a number 5 to the x argument.

```python
>>> lambda x: x + 5
```

Here, I am adding 5 to an unknown value. We can surround the above lambda with parenthesis.

```python
>>> (lambda x: x + 5)(2)
7
```

Here is the explanation of how the above line of code worked behind the scene,

```python
(lambda x: x + 5)(2) = lambda 2: 2 + 5
                     = 2 + 5
                     = 7
```

This can seem a bit hard for the beginner. Some of you are thinking it would be nice to set a name for this function. So, what are you waiting for? Let's add an appropriate name to this lambda function.

```python
>>> add = lambda x: x + 5
>>> add(2)
7
```

We can also write this lambda function in a regular syntax like below,

```python
def add(x):
    return x + 2
```

This is all about lambda function fundamental. I hope this article helped you understand the basics of the lambda function. Also, you can find the code [here](https://github.com/rubayat-tithi/lambda-function-of-python).
