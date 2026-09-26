---
title: "Python *args and **kwargs"
author: "Jihed 503"
date: 2021-10-06
description: "In this article we will discover the meaning of *args and **kwargs and find their different implementations throughout examples.*args and **kwargs are two special symbols used for passing variable..."
categories: ["Python"]
image: images/2e83aa_1807b3ea40ed4142bf25de151c6b145e.webp
wix-url: https://www.datainsightonline.com/post/python-args-and-kwargs
---
In this article we will discover the meaning of \*args and \*\*kwargs and find their different implementations throughout examples.

![](images/2e83aa_1807b3ea40ed4142bf25de151c6b145e.webp)

\*args and \*\*kwargs are two special symbols used for passing variable number of arguments to a function.

1. **\*args :** Non-Keyword Arguments

2. **\*\*kwargs :** Keyword Arguments

## *\*args*
The special syntax \*args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-key worded, variable-length argument list.

\* The syntax is to use the symbol \* to take in a variale number of arguments. By convention, it is often used with the word args, but we can as well use any other word.

\* What \*args allows you to do is take in more arguments than the number of formal arguments that you previously defined. With \*args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).

\* Using the \*, the variable that we associate with the \* becomes an iterable meaning you can do things like iterate over it, run some higher-order functions such as map and filter, etc.

### Example 1:

We can implement a function to take as many arguments as the user give and print them each in a separate line.

```python
def fun(*strings):
    for string in strings:
        print(string)

fun("Hello", "Welcome", "to", "Data Insight")
```

```python
Hello
Welcome
to
Data Insight
```

**NB: Notice that we replaced args by strings here and its totally legal.**

### Example 2:

We want to make a sum function that takes any number of arguments and be able to sum them all together.

```python
def sum(*args):
    s=0
    for i in args:
        s += i
    return s

print("The sum of 1, 2, 6, 9 is {}".format(sum(1, 2, 6, 9)))
```

```python
The sum of 1, 2, 6, 9 is 18
```

**PS: You can find more about the python string format method here : https://www.w3schools.com/python/ref_string_format.asp**

## \*\*kwargs
The special syntax \*\*kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).

\* A keyword argument is where you provide a name to the variable as you pass it into the function.

\* One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.

### Example :

We can use \*\*kwargs to take keys and values of an unknown-length dictionary.

```python
def fun(**dict):
    for key,value in dict.items():
        print("%s == %s" %(key, value))

fun(one='Python', two='for', three='data', four='science')
```

```python
one == Python
two == for
three == data
four == science
```

### Using \*args and \*\*kwargs to call a function (Unpacking Operators)

Unpacking operators are operators that unpack the values from iterable objects in Python.

The single asterisk operator "\*" can be used on any iterable that Python provides.

Also, "\*\*" can be used to create another dictionary.

```python
def fun(arg1, arg2):
    print("arg1:", arg1)
    print("arg2:", arg2)

args = ("Data", "Insight")
fun(*args)

kwargs = {"arg1" : "Data", "arg2" : "Insight"}
fun(**kwargs)
```

```python
arg1: Data
arg2: Insight
arg1: Data
arg2: Insight
```

### Using \*args and \*\*kwargs in same line to call a function

```python
def fun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

fun('Python', 'Data', 'Insight', first="Python",mid="'Data",last="Insight")
```

```python
args:  ('Python', 'Data', 'Insight')
kwargs:  {'first': 'Python', 'mid': "'Data", 'last': 'Insight'}
```

## Conclusion
We use the “wildcard” or “\\*” notation like this – \\*args OR \\*\\*kwargs – as our function’s argument when we have doubts about the number of arguments we should pass in a function.

#### GitHub: https://github.com/Jihed503/data_insight_python_concepts_for_data_science

#### Source: [geeksforgeeks.org](http://geeksforgeeks.org)
