---
title: "Understanding of args and kwargs"
author: "fredy chimire"
date: 2021-10-05
description: "args and kwargs allow you to pass multiple arguments or keyword arguments to a function.# Consider the following example. def my_sum(a, b): return a + b #This is a simple function that takes two..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/understanding-of-args-and-kwargs
---
*args and* kwargs allow you to pass multiple arguments or keyword arguments to a function.

```python
# Consider the following example.
def my_sum(a, b):
  return a + b
 #This is a simple function that takes two arguments and returns their sum:return a + b
```

The function above works fine, but it’s limited to only two arguments. What if you need to sum a varying number of arguments, where the specific number of arguments passed is only determined at runtime? Wouldn’t it be great to create a function that could sum all the integers passed to it, no matter how many there are?

**Using the Python args Variable in Function Definitions**

There are a few ways you can pass a varying number of arguments to a function. The first way is often the most intuitive for people that have experience with collections. You simply pass a list or a set of all the arguments to your function. So for my_sum(), you could pass a list of all the integers you need to add.

```python
# sum_integers_list.py
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result
​
list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))
6
```

This implementation works, but whenever you call this function you’ll also need to create a list of arguments to pass to it. This can be inconvenient, especially if you don’t know up front all the values that should go into the list.This is where \*args can be really useful, because it allows you to pass a varying number of positional arguments. Take the following example.

```python
# sum_integers_args.py
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))
```

In this example, you’re no longer passing a list to my_sum(). Instead, you’re passing three different positional arguments. my_sum() takes all the parameters that are provided in the input and packs them all into a single iterable object named args. Note that args is just a name. You’re not required to use the name args. You can choose any name that you prefer, such as integers:

```python
# sum_integers_args_2.py
def my_sum(*integers):
    result = 0
    for x in integers:
        result += x
    return result

print(my_sum(1, 2, 3))
```

The function still works, even if you pass the iterable object as integers instead of args. All that matters here is that you use the unpacking operator (\*). Bear in mind that the iterable object you’ll get using the unpacking operator \* is not a list but a tuple. A tuple is similar to a list in that they both support slicing and iteration. However, tuples are very different in at least one aspect: lists are mutable, while tuples are not. To test this, run the following code. This script tries to change a value of a list:

```python
# change_list.py
my_list = [1, 2, 3]
my_list[0] = 9
print(my_list)
[9, 2, 3]
```

The first value is no longer 0, but the updated value 9. Now, try to do the same with a tuple:

```python
# change_tuple.py
my_tuple = (1, 2, 3)
my_tuple[0] = 9
print(my_tuple)
```

```python
---------------------------------------------------------------------------TypeError                                 Traceback (most recent call last)
<ipython-input-7-b64716db8ace> in <module>      1 # change_tuple.py      2 my_tuple = (1, 2, 3)----> 3 my_tuple[0] = 9      4 print(my_tuple)TypeError: 'tuple' object does not support item assignment
```

Here, you see the same values, except they’re held together as a tuple. If you try to execute this script, you will see that the Python interpreter returns an error. This is because a tuple is an immutable object, and its values cannot be changed after assignment. Keep this in mind when you’re working with tuples and \*args.

## Using the Python kwargs Variable in Function Definitions

now we’ve understood what *args is for, but what about \**kwargs? \*\*kwargs works just like \*args, but instead of accepting positional arguments it accepts keyword (or named) arguments. Take the following example:

```python
# concatenate.py
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
```

When you execute the script above, concatenate() will iterate through the Python kwargs dictionary and concatenate all the values it finds: RealPythonIsGreat!. Like args, kwargs is just a name that can be changed to whatever you want. Again, what is important here is the use of the unpacking operator (\*\*).
So, the previous example could be written like this:

```python
# concatenate_2.py
def concatenate(**words):
    result = ""
    for arg in words.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
```

Note that in the example above the iterable object is a standard dict. If you iterate over the dictionary and want to return its values, like in the example shown, then you must use .values(). In fact, if you forget to use this method, you will find yourself iterating through the keys of your Python kwargs dictionary instead, like in the following example:

From the code above, you’ll notice the following output: abcde. As you can see, if you don’t specify .values(), your function will iterate over the keys of your Python kwargs dictionary, returning the wrong result.

**Conclusion**
You are now able to use *args and \**kwargs to accept a changeable number of arguments in your functions. You have also learned something more about the unpacking operators.

Use the
