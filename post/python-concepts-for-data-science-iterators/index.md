---
title: "Python Concepts for Data Science: Iterators"
author: "abdelrahman.shaban7000"
date: 2021-09-27
description: "In this blog, we will talk about iterator which is an object used to iterate over an iterable object.Before moving to examples let's make a distinction between two things iterator and iterable..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-concepts-for-data-science-iterators
---
In this blog, we will talk about iterator which is an object used to iterate over an iterable object.

Before moving to examples let's make a distinction between two things ***iterator*** and ***iterable*** :

*Firstly*: An iterable object is that contains data that can be iterated over e.g. List, String, Set, Tuple, Dictionary. And you can get an iterator from it using the *iter*  method

*Second*: An iterator is an object that can return data one at a time while iterating over it as we said using the *next()* method.

__________________________________________________

let's take a look at an example of iterable:

```python
mylist=['red','blue','yellow']
```

if we tried to use the *next()* method over the above iterable, we will get an error like this:

```python
print(next(mylist) )
```

```python
---------------------------------------------------------------------------TypeError                                 Traceback (most recent call last)
<ipython-input-4-82d387c9e81c> in <module>      2 mylist=['red','blue','yellow']      3----> 4 print(next(mystring))TypeError: 'str' object is not an iterator
```

So we get this as the *next()* method accepts an iterator as an argument not iterable so if we want to use the *next()* method and deal with the iterators we have to transform it into an iterator object by the *iter()* method as follows:

```python
mylist=iter(mylist)

print(next(mylist))
print(next(mylist))
print(next(mylist))
```

```python
red
blue
yellow
```

As we said we first transform the iterable object to an iterator and then using the *next()* method we iterate over the list and each time we call it, it outputs one element after another.

But what is the difference between using for loop and using the next method as before?

It turns out that For loop actually calls *iter()* method to transform the iterable object into an iterator and then it will loop over it, so the following two examples will do the same thing:

```python
mylist2=['apple','orange','banana']
for item in mylist2:
    print(item)
```

```python
apple
orange
banana
```

```python
mylist2=['apple','orange','banana']
for item in iter(mylist2):
    print(item)
```

```python
apple
orange
banana
```

______________________________________________

At the end of this blog let's go to one last example to create an iterator by ourselves to get the even numbers:

```python
# creating an iterator for even numbers
class Even:
    def __init__(self,max):
        self.n=2
        self.max=max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <=self.max:
            result=self.n
            self.n+=2
            return result
        else:
            raise StopIteration
```

this Even class will get the even numbers up to maximum number that we should specify as an argument in the constructor and it has the *next()*  method that will get the next even number as long as this number is less than the maximum number that we provided as an argument otherwise it will raise StopIteration.

```python
# We will check if the above code works by creating an object from the Even class and set the maximum number to be 10
nums=Even(10)

# we will get the even numbers by iterating over them by the next method
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
```

```python
2
4
6
8
10
```

Here we created an object from the Even class and set the maximum number to be 10 and we iterate over these numbers through the *next()* method. So the output became as shown above.

If we get the *next*() method one more time we will get StopIteration as follows:

```python
print(next(nums))
```

```python
---------------------------------------------------------------------------StopIteration                             Traceback (most recent call last)
<ipython-input-10-ddf9ec797e52> in <module>----> 1 print(next(nums))<ipython-input-9-da5cd2672051> in __next__(self)     14             return result
     15         else:---> 16             raise StopIteration
     17     18StopIteration:
```

Link for GitHub repo [here](https://github.com/Abdelrahman7000/Abdelrahman7000-python_Concepts_for-Data_Science_Iterators)
