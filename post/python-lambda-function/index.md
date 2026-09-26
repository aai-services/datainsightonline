---
title: "Python Lambda Function"
author: "Musonda Katongo"
date: 2022-10-18
description: "A Python Lambda function is a function without a name and as such it is referred to as an anonymous function. Just as the 'def' key word is used for defining a normal function, the 'lambda' key word..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-lambda-function
---
## Table of Contents

1. Introduction
2. Lambda Function Syntax
3. Lambda Function Use
4. Lambda Function Example
5. Lambda Functions More Practical Examples
6. Conclusion

## 1. Introduction

A Python Lambda function is a function without a name and as such it is referred to as an anonymous function. Just as the 'def' key word is used for defining a normal function, the 'lambda' key word is used for defining a Lambda function.

Lambda functions are restricted to a single expression and allows users to write functions in a quick way

## 2. Lambda Function Syntax

The syntax for a lambda function is as follows:

```python
lambda argument(s): expression
```

The Lambda function is specified by a keyword 'lambda' after which the names of the arguments are specified followed by a colon and the expression that specifies what should be returned by the function. The Lambda function can take on any number of arguments but will only have one expression to be evaluated and returned.

## 3. Lambda Functions Use

Lambda functions are useful when one is writing simple logical operations that are easy to understand. In this case, they make the code more readable. When writing functions that will be used just once, lambda functions are a preferred way to do this.

One should take into consideration that Lambda functions can only perform one expression and as such they should be restricted to simple expressions with only one line of code that will be used only once within the code.

## 4. Lambda Function Example

We take an example of a function that accepts a number and returns the square of that number. The following would be the function definition for a normal python function and for a lambda function. Note that for a normal python function the function name is 'square_num' whereas the lambda function as no function name.

```python
# Normal Python Function
def square_num(x):
    return x**2

# Lambda Function
lambda x: x**2
```

### 4.1 Normal Python Function Implementation

```python
# define function
def square_num(x):
    return x**2

#square the number
squared_num = square_num(5)

squared_num
```

```python
25
```

### 4.2 Lambda Function Implementation

```python
squared_num = lambda x: x**2

squared_num(5)
```

```python
25
```

## 5. Lambda Functions More Practical Examples

The above example executes a simple operation of squaring a number using a lambda function. However, lambda functions can be used on a number operations which can be used for short operations and data manipulation in a number of ways. We will look at some of the other examples that we can apply the lambda function. This includes the use of lambda function with other functions.

### 5.1 Lambda Function with if-else

We can use a lambda function with an if-else statement. The function below accepts two numbers and returns the maximum between the two.

```python
max_num = lambda a, b: a if(a>b) else b

print(max_num(5,9))
```

```python
9
```

### 5.2 Lambda Function with Filter Function

The filter() function takes in a function and a list. The list is filtered based on the function that is passed and returns all of the elements for which the function returns True. We can use the lambda function with the filter() function to filter out the elements for which the lambda function returns True.

The example below is a the application of a filter function were we filter out even numbers from a given list. The lambda function checks for the condition for each of the elements whether its mod 2 is zero which means it is even.

```python
#create a list
our_list = list(range(1,11)
our_list
```

```python
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

```python
#filter out even numbers
even_list = list(filter(lambda x: x%2 == 0, our_list)
even_list
```

```python
[2, 4, 6, 8, 10]
```

### 5.3 Lambda Function with Map Function

The lambda function takes in a list and a function. The function operation is performed on all of the elements in the list. Let us say we want to square all of the elements in our list, we will then pass a function, a lambda function in this case, for squaring a number a list that we want to map that function on.

```python
sq_list = list(map(lambda x: x**2, our_list)
sq_list
```

```python
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## 6. Conclusion

Lambda Functions are useful you want to perform simple function operations within a single line of code. This functions will mostly not be used again in the code and as such making lambda functions a more appropriate option. One should be however, cautious when choosing to use lambda functions. Lambda functions should not be used for functions that require multiple lines of code and were comments might be needed to describe the function.

The notebook for the code in this writeup can be found on the following link on [GitHub](https://github.com/Musonda2day/Python-Lambda-Function-)
