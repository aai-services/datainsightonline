---
title: "Lambda Expressions in Python"
author: "Nargiz Huseynova"
date: 2021-10-03
description: "Anonymous functions in Python are functions that are defined without a name. Anonymous functions can accept multiple inputs and return single output. They contain only one single executable..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/lambda-expressions
---
Anonymous functions in Python are functions that are defined without a name. Anonymous functions can accept multiple inputs and return single output. They contain only one single executable statement.

Now, there are various types of anonymous functions in Python but we are going to learn only the lambda functions in this blog.

Lambda function is a small anonymous function. It can take any number of arguments but can have only one expression. The syntax for the lambda function is:

```python
lambda arguments: expression
```

Now let us try to understand the lambda functions by taking an example. Suppose we have a number and we want the square of that number as a result. So let us define our lambda function following the syntax.

```python
#Lambda function with a single argument
x = lambda a: a*a
print(x(5))
```

When we run the above code we get:

```python
25
```

Let us define another lambda function, which has more than one argument

```python
#Lambda function with more than one argument
y = lambda a, b: a+b
print(y(4,6))
```

As a result we get 4+6:

```python
10
```

Now it is time to solve following exercise using lambda function.

**Exercise.**

Write a program to rearrange positive and negative numbers in a given list *L1* using lambda.

```python
L1=[-10, -4, 6, 8, -3, 7, 3, -9]
```

Firstly, we should use the inbuilt *sorted* function, and inside that use the lambda to check if the value is positive or negative.

```python
#Exercise
L1=[-10, -4, 6, 8, -3, 7, 3, -9]
print('Original list: ')
print(L1)
result=sorted(L1, key = lambda i: 0 if i==0 else -1 / i)
print('Rearranged positive and negative numbers of the given list')
print(result)
```

```python
Original list:
[-10, -4, 6, 8, -3, 7, 3, -9]
Rearranged positive and negative numbers of the given list
[3, 6, 7, 8, -10, -9, -4, -3]
```

So at first, we are initializing the list L1 with the given values, then print the original list to show the difference and we are passing the list L1 to the sorted function. Inside the sorted function, we are passing the *lambda* function as a *key* to the sorted function. In this lambda function, it will check if each element in the list is zero or not. If it is equal to zero, then it will keep the key as zero and do the sorting based on that, or else it will calculate the key value by minus one divided by the current element, and it will do the sorting. This key will help us to sort the positive and negative elements separately.

Lambda functions are much recommended to use whenever we have smaller functions to execute in our Python program. Lambda functions are widely used for data manipulation and feature engineering where we have to make smaller changes to larger datasets.

You can find the GitHub repo of this code through this [link](https://github.com/iamNargiz/Py_Concepts_Lambda).
