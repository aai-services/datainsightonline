---
title: "What is Python's Map Function?"
author: "Magdy Ahmed"
date: 2021-10-05
description: "Python map() applies a function on all the items of an iterable given as input. An iterable, for example, can be a list, a tuple, a set, a dictionary, a string, and it returns an iterable map object..."
categories: ["Python"]
image: images/215973_0314e6a15f32429cba36348a777aa071.webp
wix-url: https://www.datainsightonline.com/post/what-is-python-s-map-function
---
![](images/215973_a87274853f8e4421b78227a3daec72bd.webp)

Python map() applies a function on all the items of an iterable given as input. An iterable, for example, can be a list, a tuple, a set, a dictionary, a string, and it returns an iterable map object. Python map() is a built-in function.

Sometimes you might face situations in which you need to perform the same operation "like applying a certain function" on all the items of an input iterable to build a new iterable. The quickest and most common approach to this problem is to use a Python for loop. However, you can also tackle this problem without an explicit loop by using map().

So the key concept here is transformation which can include but is not limited to:

- Converting strings to numbers
- Rounding numbers
- Getting the length of each iterable member
- Cleaning columns "features" in datasets

You might be wondering, "why can't I just do the above with a for loop?"

The answer is, you can. But using the Python Map Function saves you memory (which means that your code runs faster) and requires less code. Let's walk through an example so you can understand what I mean.

## First Let's Start with a For Loop
Let's say you have a list of strings that are actually numbers, but you need to convert the list of strings to integers, You could use an empty list and a for loop to accomplish this:

```python
list_of_strings = ["5", "6", "7", "8", "9", "10"]

result = []

for string in list_of_strings:
    result.append(int(string))
print(result)
# Output:[5, 6, 7, 8, 9, 10]
```

You may be happy with the result, but think about what your code just did.

You told the computer to go through each member ("5", "6", "7", etc...), convert the member, and then store that member in a new list. While using a for loop to transform a list is functional, it isn't optimal.

## Python Map Function
Instead, let's use the Python Map Function to produce a functional & optimal result. We'll start with our list of strings that need to be converted, Then we'll use the Python Map Function to transform the list of strings to a list of integers:

```python
list_of_strings = ["5", "6", "7", "8", "9", "10"]

result = map(int,list_of_strings)
print(list(result))
# Output:[5, 6, 7, 8, 9, 10]
```

Before we get to why the Python Map Function is more optimal than using a for loop, let's break down what we just did, All we did here is create a variable that stores the list of strings that we want to convert to numbers.

The Python Map Function's syntax is as follows:

```python
map(insert function here, insert iterable here)
```

map() is simply the name of the Python Map Function, nothing fancy here.

insert function here is the space where you would write in a function. In the above code example, we used the int function. We could have used another built-in function like len() or we could have built our own function and used it here as well.

insert iterable here is the space where you would write in the iterable of your choice. In this instance, we inserted our list (list_of_strings).

result is the variable where we're storing our newly transformed members, Then list() takes our newly transformed iterable members and tells our computer these members are apart of a list.

> *So instead of iterating through each member of the list of strings, the Python Map Function transformed the entire list of strings to a list of numbers. You saved memory and your code ran faster.*

## Conclusion
In the end, the Python Map Function is more elegant than a for loop and will help you compile your code faster.

Using the Python Map Function will help take your coding skills to the next level and become a better programmer.

That said, the Python Map Function is just the beginning. There are plenty more Python tricks that will help you write more elegant code and improve your programming skills. Happy coding!
