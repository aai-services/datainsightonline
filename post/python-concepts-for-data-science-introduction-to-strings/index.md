---
title: "Python Concepts for Data Science: Introduction to Strings"
author: "Caleb Atiemo - Keseku"
date: 2021-10-04
description: "Words play a vital role in how we communicate, so it is in the right sense that we would want our computers to be able to work with words and sentences as well.In Python, something like a word or..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-concepts-for-data-science-introduction-to-strings
---
Words play a vital role in how we communicate, so it is in the right sense that we would want our computers to be able to work with words and sentences as well.

In Python, something like a word or sentence is known as a string. A string is a sequence of characters contained within a pair of 'single quotes' or "double quotes". A string can contain any letters, numbers, symbols and spaces.

In this post, our objective is to learn more about strings and how they are treated in Python. We will learn how to slice strings, select specific characters from strings, iterate through strings and use strings in conditional statements. Now let's zoom in.

A string can be thought of as a list of characters. Like any other list, each character in a string has an index. Consider the string:

```python
name = 'Kwame'
```

Specific letters from this string can be selected using the index. Let’s say we decide to select the first letter of the string.

```python
print(name[0])
```

This would output:

```python
K
```

What about the third letter?

```python
  print(name[2])
>>a
```

Not only can a single character be selected from a string, but entire chunks of characters can also be selected. This can be done with the following syntax:

```python
string[first_index:last_index]
```

This process is known as slicing. When a string is sliced, a new string that starts at the first_index and ends at (but excludes) the last_index is created. An example would be:

```python
print(name[1:4])
```

This would result in:

```python
wam
```

There can also have open-ended selections. If the first index isn't included, the slice starts at the beginning of the string and if we remove the second index the slice continues to the end of the string. Here are some examples:

```python
print(name[:3])
print(name[2:])
```

These lines result in:

```python
Kwa
ame
```

We can also *concatenate*, or combine, two existing strings together into a new string. Consider the following two strings:

```python
firstname = 'Nana'
lastname = 'Yaw'
```

A new string is formed by concatenating the above strings as follows:

```python
fullname = firstname + lastname
print(fullname)
```

The resulting concatenation will be:

```python
NanaYaw
```

Notice that there are no spaces added here. We have to manually add in the spaces when concatenating strings if we want to include them.

```python
fullname = firstname + ' ' + lastname
print(fullname)
```

And the result is:

```python
Nana Yaw
```

Python comes with some built-in functions for working with strings. One of the most commonly used of these functions is len() and this returns the number of characters in a string:

```python
  print(len(name))
>>5
```

If you are taking the length of a string with spaces, the spaces are counted as well.

```python
  print(len(fullname))
>>8
```

len() comes in handy when we are trying to select characters from the end of a string which has an index of len(string_name) - 1. The following line of code will return the last character in the string.

```python
  print(fullname[len(fullname)-1])
>>w
```

Because strings are lists, that means we can iterate through them using 'for' or 'while' loops. This opens up a whole range of possibilities of ways that can be manipulated to analyze strings. Let's take a look

```python
for letter in fullname:
    print(letter)
```

This will iterate through each letter in fullname word and will print it as follows:

```python
N
a
n
a

Y
a
w
```

When we iterate through a string we perform an action with each character. By including conditional statements inside of these iterations, we can manipulate the characters extra. Let's analyze what the following code does:

```python
counter = 0
for letter in fullname:
    if letter == 'a':
        counter += 1
print(counter)
```

This code will count the number of 'a; in fullname. First, a counter is initialized to zero. The 'for' loop iterates through each character in fullname and compares it to the letter 'a'. Each time a character equals 'a' the code will increase the variable counter by one. Once all characters have been checked, the code will print the counter, telling us how many 'a' are in fullname.

Another method to determine if a character is in a string is using the keyword 'in'. 'in' checks if one string is part of another string. Here is how the syntax looks like:

```python
substring in string
```

This is a boolean expression that is True if the substring is in the string.

Here is the [link](https://github.com/catiemokeseku/Strings.git) to the repo on GitHub
