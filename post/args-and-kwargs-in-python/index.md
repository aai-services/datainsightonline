---
title: "Python Concepts for Data Science: *args and **kwargs"
author: "Kouamé Maïzan Alain Serge Kossonou"
date: 2021-10-03
description: "In this article we will be interested in the use of *args and **kwargs. But first we will try to know what it represents and the different cases where we could be trying to use them. Let me tell you..."
categories: ["Python"]
image: images/a33eeb_a3cd54be76f94fea96df30fb360b77f2.webp
wix-url: https://www.datainsightonline.com/post/args-and-kwargs-in-python
---
![](images/a33eeb_a3cd54be76f94fea96df30fb360b77f2.webp)

## General introduction
In this article we will be interested in the use of **\*args** and **\*\*kwargs**.

But first we will try to know what it represents and the different cases where we could be trying to use them.

Let me tell you that it is not require to write **\*args** or **\*\*kwargs** and only the **"\*"** is require. You could have also **\*vars** and **\*\*vars** or with the name that is best suited to the situation.

Usually **\*args** and **\*\*kwargs** allow you to pass unspecified number of argument. You don't need to know how many arguments will be used.

## Using of \*args
**In a function**

**\*args** is use for non-keyworded argument.

For clarity, we'll illustrate this with a few examples. First we're going to use a function that doesn't use **\*args** and then another that uses it.

```python
def my_sum(a, b):
    return a + b

print(my_sum(1, 4)) # output 5
```

With the previous example we see that the different variables used in the program are already known. If we want the same function to be able to calculate the sum of 3 numbers we will add another argument to the function.

```python
def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3, 4)) # output 10
```

With our new function we have no argument limit that we want to use in the function. We find that the body of our function has changed a bit, and **\*args** behaved as if we had passed a list to our function. This function could be compared to this one.

```python
def my_sum(to_add_up):
    result = 0
    for x in to_add_up:
        result += x
    return result

print(my_sum([1, 2, 3, 4])) # output 10
```

In summary when **\*args** is used in a function it could be likened to as if we are using a list in a function parameter. Except that the arguments are added one by one to our function.

**unpacking operators**

Unpacking operators are operators that unpack the values from iterable objects in Python.

The single asterisk operator **"\*"** can be used on any iterable that Python provides.

```python
my_list = [1, 2, 3, 4]
print(*my_list) # output 1 2 3 4
```

In the previous example we were able to display all the values ​​of our list without having to browse the values ​​inside.

```python
my_list = [1, 2, 3, 4]
first, *new_list, last = my_list

print(first) # output 1
print(new_list) # output [2, 3]
print(*new_list) # output 2 3
print(last) # output 4
```

If the number of variables is not equal as in the following example we get an error.

```python
my_list = [1, 2, 3, 4]
first, second, last = my_list #error
```

We note then that thanks to the unpacking operator **"\*"** we can retrieve the value of several variables directly inside a list.

```python
my_first_list = [1, 2, 3, 4]
my_second_list = [5, 6, 7, 8, 9]

my_list = [*my_first_list, *my_second_list]

print(my_list) # output [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Finally we can use this operator to fill a list

## Using of \*\*kwargs

**in a function**

**\*\*kwargs** is use for keyworded argument like dictionnary.

Trying to use this to a function which concatenates the words we have.

- **without using \*\*kwargs**

```python
def concatenate(a='', b='', c=''):
    return a + b + c

print(concatenate('Kwargs', ' is ', 'awesome')) # output "Kwargs is awesome"
```

In this function each argument passed has a default value, so the function can be used without parameters

- **using \*\*kwargs**

```python
def concatenate(**kwargs):
    result = ""
    for x in kwargs:
        result += x
    return result

print(concatenate(a='Kwargs', b=' is ', c='awesome')) # output "abc"
```

By default when we are a parameter we access keys and not values, so to have access to values ​​we have this new version of our code.

```python
def concatenate(**kwargs):
    result = ""
    for x in kwargs.values():
        result += x
    return result

print(concatenate(a='Kwargs', b=' is ', c='awesome')) # output "Kwargs is awesome"
```

If we use our function in the following way we will get an error.

```python
print(concatenate('Kwargs', ' is ', 'awesome')) # error
```

As with the **\*args** argument, the **\*\*kwargs** argument acts as a list so each element is a dictionary.

**unpacking operators**

As with **\*args**, **\*\*kwargs** can be used to create another dictionary

```python
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_dict = {**my_first_dict, **my_second_dict}

print(my_dict) # output {'A': 1, 'B': 2, 'C': 3, 'D': 4}
```

## Using \*args and \*\*kwargs together in function

In the event that we want to use both one or more normal variable with **\*args** and **\*\*kwargs**, then the order of the variables matters. If they are not placed in the correct order then we will have an error.

Here is the correct order that must be followed to be able to use them at the same time.

```python
def my_func(normal, *args, **kwargs)
```

## Conclusion
We enjoyed defining the **\*args** and **\*\*kwargs** arguments together,

then reviewed the different use cases. We hope you enjoyed learning with us, so it can be used for you later.
