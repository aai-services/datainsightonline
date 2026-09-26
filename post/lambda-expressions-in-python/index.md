---
title: "Lambda expressions in Python"
author: "Ahmed Shebl"
date: 2022-01-24
description: "Lambda expressions are one of the most useful tools in Python. lambda expressions allow us to create \"anonymous\" functions. This basically means we can define functions without using def.In Python..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/lambda-expressions-in-python
---
Lambda expressions are one of the most useful tools in Python. lambda expressions allow us to create "anonymous" functions. This basically means we can define functions without using def.

In Python, an anonymous function is a function that is defined without a name. The def keyword is used to define a normal function in Python. But the lambda keyword is used to define an anonymous function in Python.

**Python Lambda Function Syntax:**

lambda argument(s): expression

- Lambda function can have any number of arguments but only one expression, which is evaluated and returned.
- One is free to use lambda functions wherever function objects are required.
- Function objects returned by running lambda expressions work exactly the same as those created and assigned by def.

The lambda's body is similar to what we would put in a def body's return statement. We simply type the result as an expression instead of explicitly returning it.

Let's explain a lambda expression by starting from a normal function:

```python
def double_value(x):
    result = x * 2
    return result
```

```python
double_value(2)
```

```python
output: 4
```

Continuing the illustration:

```python
def double_value(x):
    return x * 2
```

```python
double_value(2)
```

```python
output: 4
```

We can write this function in one line (although it is a bad style to do that)

```python
def double_value(x): return x * 2
```

```python
double_value(2)
```

```python
output: 4
```

This is the form of a function that a lambda expression uses. A lambda expression can then be written as:

```python
lambda x: x * 2
```

```python
output: <function __main__.<lambda>(x)>
```

In the example above, the expression is composed of:

- The keyword: **lambda**
- A variable: **x**
- A body: **x \* 2**

Note how we get a function back. We can assign this function to a variable:

```python
double_value_with_lambda= lambda x: x * 2
```

and we can call the lambda function using this variable

double_value(3)

```python
double_value_with_lambda(3)
```

```python
output: 4
```

Let's see other examples:

**Example 1: Add two numbers**

In this example, we have two arguments: x, y

```python
add_numbers = lambda x, y: x+y
```

```python
add_numbers(3, 5)
```

```python
output: 8
```

**Example 2** Lambda **with lists:**

```python
list_num = [1,25,14,7,33,96,47,78,19]
```

The filter() function in Python takes in a function and a list as arguments.

The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True.

```python
list(filter(lambda x: x > 50, list_num))
```

```python
output: [96, 78]
```

### Example 3 Lambda with Series:
```python
import pandas as pd
df = pd.DataFrame({
    'Company': ['Microsoft','Google','Youtube','Apple'],
    'Year': [1975, 1998, 2005, 1976],
})
```

```python
df['duration'] = df['Year'].apply(lambda x: 2022-x)

df
```

```python
output: Company   Year   duration
      0 Microsoft 1975      47
      1 Google    1998      24
      2 Youtube   2005      17
      3 Apple     1976      46
```

lambda expressions really shine when used in conjunction with map(), filter(), and reduce(), which each function of them needs a separated article.
