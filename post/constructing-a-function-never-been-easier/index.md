---
title: "constructing a function never been easier !"
author: "Rawda Rumaieh"
date: 2021-10-11
description: "Have you ever spent time to determine how many arguments you should pass to your function?After each line of code you realize you should add one more argument to the function?Did you run into errors..."
categories: ["Python"]
image: images/d96e14_b5c1f1afe02d404a8dde3632677b8e58.webp
wix-url: https://www.datainsightonline.com/post/constructing-a-function-never-been-easier
---
Have you ever spent time to determine how many arguments you should pass to your function?

After each line of code you realize you should add one more argument to the function?

Did you run into errors because of passing more of less parameters to the function?

![](images/d96e14_b5c1f1afe02d404a8dde3632677b8e58.webp)

Well after learning this python concept you will never have to worry again about these issues !

**\*args / \*\*kwargs** are special symbols used for passing arguments

**\*args** is when we are passing (*non key-word arguments list on which operations of the list can be performed*)

while **\*\*kwargs** is we are passing (key-word arguments)

passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed

to elaborate with an example:

let's start with **\*args** and define a function that sums two numbers the user will enter

```python
def sum_this(a,b):
     result=a+b
     return result
```

If we passed more than two arguments an error will appear telling us:

```python
TypeError: sum_this() takes 2 positional arguments but 3 were given
```

To fix this error:

```python
#defining a function that will take a list of arguments
def sum_these(*args):
    #defning the variable
    sum_this=0
    for i in args:
        #adding all the values in the args list together
        sum_this=sum_this+i
    return sum_this
```

I can now pass to the functions as much arguments as I wish

```python
print(sum_these(1,2,3,4,5))
```

and the function will sum them all .. I can call the same function with the double amount of arguments without worrying about how many arguments I constructed the function with.

For **\*\*Kwargs:**

```python
#printing information of clients
def print_info(**kwargs):
    for key , val in kwargs.items():
        print(key,":",val)
```

```python
print_info(Firstname="Rawda", Lastname="Rumaieh", Age=22, Phone=12345678910,country="Egypt")
```

we **\*\*kwargs** the same as a dictionary

On a side note:

we can rename kwargs and args with whatever name we like just don't forget the **\*** if it's a *non key-word argument*and **\*\***if it's a*key-word argument*

To recap:

we use **\*\*kwargs** and **\*args** for:

1. functions we don't fully understand what's going on with them
2. functions having many different features you are not aware of
3. functions features we will not use at first
