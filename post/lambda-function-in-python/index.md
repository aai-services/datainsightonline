---
title: "Lambda Function in Python"
author: "Tahani Reesh"
date: 2021-10-06
description: "Introduction Python Lambda Functions are ‘Anonymous function’ means that the function can be defined without a name. normal functions are defined using the def keyword, anonymous functions are..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/lambda-function-in-python
---
## Introduction
Python Lambda Functions are ‘Anonymous function’ means that the function can be defined without a name. normal functions are defined using the def keyword, anonymous functions are defined using the lambda keyword. However, they are restricted to a single line of expression.

## Function Syntax:

The syntax for lambda function is given by :

```python
lambda arguments: expression
```

Notice, This function can have any number of arguments but only one expression, which is evaluated and returned. There is no return statement which is usually present in the def function syntax.

Now Let’s look at next example to understand the **difference between a normal def defined function and lambda function**. This is a program that returns the **square** of a given value:

```python
# calculate squares using lambda
lambda_squares = lambda x: x**2
print('Using lambda: ', lambda_squares(5))
```

output :

```python
Using lambda:  25
```

Do the same with def :

```python
def squares_def(x):
        return x*x
print('Using def: ', squares_def(5))
```

Output:

```python
Using def: 25
```

As we can see in the above example both the square() function and lambda_square() function behave the same and as intended. Let’s analyse the above example a bit more:

- **Without using Lambda:** Here, both of them return the square of a given number. But, while using def, we needed to define a function with a name cube and needed to pass a value to it. After execution, we also needed to return the result from where the function was called using the *return* keyword.
- **Using Lambda:** Lambda definition does not include a “return” statement, it always contains an expression that is returned. We can also put a lambda definition anywhere a function is expected, and we don’t have to assign it to a variable at all. This is the simplicity of lambda functions.

Let’s see some more commonly used examples of lambda functions.

## 1. lambda function in filter()
**filter()** function is used to filter a given iterable (list like object) using another function that defines the filtering logic. A lambda function is typically used to define the filtering logic and is passed as the first argument of **filter()**. An iterable like a list object is passed as the second argument to the filter function.

The example below filters a list for even numbers.

```python
list_1 = [1,2,3,4,5,6,7,8,9]

filter(lambda x: x%2==0, list_1)

list(filter(lambda x: x%2==0, list_1))
```

Output:

```python
[2, 4, 6, 8]
```

## 2. lambda function with if-else

Example of lambda function using if-else

```python
Min= lambda a,b : x if(a>b) else b
print(Min(9,7))
```

Output:

```python
7
```

## 3. lambda function in map()

**map()** function applies a given function to all the itmes in a list and returns the result. Similar to **filter()**, simply pass the lambda function and the list (or any iterable, like tuple) as arguments.

```python
# python code to get the double of list
li= [3, 2, 5 ,6]

final_list= list(map(lambda x:x*2,li))

print(final_list)
```

Output:

```python
[6, 4, 10, 12]
```

## Conclusion

Many programmers who don’t like Lambdas usually argue that you can replace them with the more understandable [**list comprehensions**](https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/)**,** [**built-in**](https://docs.python.org/3/library/functions.html) functions, and standard libraries. [**Generator expressions**](https://djangostars.com/blog/list-comprehensions-and-generator-expressions/) (similar to list comprehensions) are also handy alternatives to the map() and filter() functions.

Check out the code used here in My [GitHub](https://github.com/tahanijaber/Lamda_func/upload)

. Thank you for reading!

## References:
- https://www.analyticsvidhya.com/blog/2020/03/what-are-lambda-functions-in-python/
- Overusing lambda expressions in Python
