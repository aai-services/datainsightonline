---
title: "Python Concepts for Data Science: Lambda Functions"
author: "Sujan Karki"
date: 2021-10-02
description: "Functions are a handy tool whenever we want to perform a repetitive task. It helps us by preventing to write the same section of codes over and over again. However, situations can arise when we want..."
categories: ["Python"]
image: images/73dae0_71d70f73ab984b37839d85ee3312afef.webp
wix-url: https://www.datainsightonline.com/post/lambda-functions
---
Functions are a handy tool whenever we want to perform a repetitive task. It helps us by preventing to write the same section of codes over and over again. However, situations can arise when we want to define a function for a single use. Like for example, a function such as:

```python
def plus_one(x):
    return x+1
```

One can argue why define such single line functions. The answer would be because some functions such as [map()](https://docs.python.org/3/library/functions.html#map), [filter()](https://docs.python.org/3/library/functions.html#filter), etc. required a function as an argument.

A lambda function thus allows us to define a single line, readable and temporary function for such use. The above specified plus_one() function can be written as a lambda function as

```python
plus_one = lambda x: x+1
```

However note that, although a variable name can be assigned for lambda function, it is not a good practice to do so. A lambda function is thus also known as a *'Anonymous function'* i.e. a function without a name.

## Syntax
```python
lambda arguments: expression
```

The syntax of lambda function is the keyword lambda followed by the argument. Then comes the expression separated from argument by the : *(colon)* sign.

To get a better understanding of the lambda function, lets look at a few examples.

## Example 1: use with filter()
The filter() function in Python takes in a function and a list as arguments.

The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True. Here is an example use of filter() function to filter out only even numbers from a list.

```python
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)
```

The above function might look complex in first sight. For simplicity we can create a normal function for comparison.

```python
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

def even(x):
  if x%2 == 0:
    return True
  else:
    return False

new_list = list(filter(even, my_list))
print(new_list)
```

If we compare the two functions above, the entire even() function has been reduced into a single line code. This makes the code shorter and easier to read. The output of both the codes is

```python
[4, 6, 8, 12]
```

## Example 2: use with map()
The map() function in Python takes in a function and a list.

The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item. Here is an example use of map() function to double all the items in a list.

```python
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)
```

The output of the above code is:

```python
[2, 10, 8, 12, 16, 22, 6, 24]
```

## The pros and cons of lambda
Now we've looked at defining and using lambda function, lets look at its advantages and disadvantages.

**Pros**

- Good for simple logical operations that are easy to understand. This makes code more readable too.
- Good when you want a function that you will use just one time.

**Cons**

- They can perform one expression, It's possible to have multiple independent operations in one lambda function.
- Bad for operations that would span more than one line in a normal def function. If you need a minute or two to understand the code, use a named function instead.
- Bad because you can't write a doc-string to explain all the inputs, operations, and outputs as you would in a normal def function.

Choosing whether or not to use a lambda function depends entirely on the user. However, it is essential to understand their use since one will inevitable come across it in other people's code. Although overwhelming at first sight, lambda function is rather easy to implement once you understand its syntax and will definitely come handy when you clean large data in data science.

You can find the example in my [GitHub](https://github.com/Clown-Face/DataInsight/blob/0aaf800edaf5badb9bd784de9530bdf890204c8d/Lambda%20function.ipynb)
