---
title: "Formatting Strings in Python"
author: "Heba Elwazzan"
date: 2021-10-07
description: "As of Python 3.6 there are 5 ways of formatting strings and showing variables in a given string: • % Strings • .format() • f-strings • template strings • concatenationIn this article we will explore..."
categories: ["Python"]
image: images/73e331_8ca3f2b93c3548b38275b8d54b5a9caa.webp
wix-url: https://www.datainsightonline.com/post/formatting-strings-in-python
---
![](images/73e331_8ca3f2b93c3548b38275b8d54b5a9caa.webp)

As of Python 3.6 there are 5 ways of formatting strings and showing variables in a given string:

- % Strings
- .format()
- f-strings
- template strings
- concatenation

In this article we will explore each's usages and list the pros and cons of each.

## % Strings
This is the old style of strings that is still used in many languages such as C. However, it is fairly uncommon to see code written using newer versions of Python using it. The reason is simple: it is a rather inconvenient way, and easier alternatives are readily available.

The way to use it is simple: substitute the variable name you wish to use with %sthen follow the string with the % operator then the variable you wish to use

```python
name = 'Ahmed'
'Hello, %s' % name  # Hello, Ahmed
```

If you are familiar with C functions such as **sprintf(),** you would know that there are a variety of alternatives to %s such as %d, %f, and %x.

```python
print('This will print an integer: %d' % 3213)  # 3213
print('This will print a float: %f' % 3213)  #  3213.000000
print('This will convert a number to its hexadecimal equivalent: %x' % 3213)  # c8d
```

If you need to use more than one variable in one print statement, you must use a tuple. It is easy to see how this gets messy very quickly:

```python
print('This actor\'s name is %s. He is %d years old. His height is %f metres. Some movies he starred in are %s' % ('Benedict Cumberbatch', 45, 1.83, ['Doctor Strange', 'The Imitation Game', 'The Hobbit']))
# This actor's name is Benedict Cumberbatch. He is 45 years old. His height is 1.830000 metres. Some movies he starred in are ['Doctor Strange', 'The Imitation Game', 'The Hobbit']
```

**Note** how we had to escape the ' character using . This is present in all formatting methods not just % strings. An alternative way was to use the opposite quotation marks. For example if you were to use double quotes in a string, surround the string with single quotes, and vice versa.

```python
'His name is "Ahmed"'
"The actor's name is Benedict Cumberbatch"
```

Back to % strings -- in standard Python fashion, built-in features of the programming language are utilized to the max -- yes even with an archaic formatting method such as this!

You can, for example, embed dictionaries in your strings:

```python
print('%(name)s has %(number)d cats.' %
      {'name': "Ahmed", "number": 2})
#  Ahmed has 2 cats
```

Other features like zero padding, pace padding, and float precision can also be used:

```python
print('Agent %03d' % 7)  # Agent 007
print('Can I have %.2f dollars?' % 5)  # Can I have 5.00 dollars?
```

Padding, hexadecimal conversion, float precision, and other features are not unique to % strings. Other forms of formatting have them as well.

**Why we don't use % Strings anymore**
The obvious reasons include its difficulty and readability, as well as a host of other problems where it doesn't display dictionaries and tuples correctly. Even the official [Python documentation](https://docs.python.org/3/library/stdtypes.html#old-string-formatting) does not recommends using it:

> The formatting operations described here exhibit a variety of quirks that lead to a number of common errors (such as failing to display tuples and dictionaries correctly). Using the newer formatted string literals, the str.format() interface, or template strings may help avoid these errors. Each of these alternatives provides their own trade-offs and benefits of simplicity, flexibility, and/or extensibility.

## .format()
This method was introduced in python 2.7. It works just like any other string method and is an improvement on readability and usage than its predecessor.

```python
print('Hello, {}'.format(name))  # Hello, Ahmed
```

If you want to add more than one variable, you can list them in the order they are mentioned, or index them in different ways:

```python
cat = 'Tom'
mouse = 'Jerry'
print('I love {} and {}'.format(cat, mouse))
# I love Tom and Jerry

print('I also love {cat} and {mouse}'.format(cat=cat, mouse=mouse))
# I also love Tom and Jerry
```

Keep in mind that **str.format()** is a method just like any other, meaning you can call it on a predefined string.

```python
string_temp = 'Hello my name is {} and I love {}'
print(string_temp.format('Ahmed', 'Tom and Jerry'))
# Hello my name is Ahmed and I love Tom and Jerry
```

## f-strings
.format() is already an improvement on formatting strings, but in version 3.6, Python introduced f-strings, which made formatting strings simple and intuitive.

```python
print(f'Hello {name}')  # Hello Ahmed
```

Simple enough, right? But it doesn't end here. You can embed *pretty much anything* in your f-strings. Below are a couple of examples:

```python
# Arithmetic
x = 3
y = 4
print(f'{x} + {y} is {x + y}')
# 3 + 4 is 7
```

```python
# Functions
print(f'{name.lower()}')
# ahmed
```

```python
# Dictionaries
print(f'The actor\'s name is {actor["name"]} and he starred in movies like {actor["movies"]}')
# The actor's name is Benedict Cumberbatch and he starred in movies like ['Doctor Strange', 'The Imitation Game', 'The Hobbit']
```

As you can see, f-strings provide the simplest syntax so far. They are also significantly faster than % strings, .format() and even concatenation due to better memory utilization.

**Template Strings**
Template strings are a bit clunky to use but are useful in the right setting. First, we have to import it from the standard library:

```python
from string import Template
greeting_temp = Template('Good $time, $name')
print(greeting_temp.substitute(time='evening', name='Ahmed'))
# Good evening, Ahmed
```

It wraps up what you could have done using a function. It's useful in situations where you have to type out the same layout for something such as an email where you need to make it personalized for each recipient for example by adding in their names and details.

**Concatenation**
Simple concatenation is probably the first way we learnt to format strings with. It can be tedious for longer strings, but can come in handy for quick one liners.

```python
print('Hello, my name is ' + name + ' and I love ' + cat + ' and ' + mouse)
# Hello, my name is Ahmed and I love Tom and Jerry
```

Thus concludes our overview of Python string formatting. Python offers a versatile range of options for every single aspect of it, and it comes in handy when handling different situations.
