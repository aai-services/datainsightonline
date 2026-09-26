---
title: "Count character occurrences in a given word, phase or sentence"
author: "Tahani Reesh"
date: 2021-09-21
description: "Here we will learn how to write a program in Python which prints the number of occurrences of each character in a string.There are multiple ways in Python, we are going to use Counter..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/count-character-occurrences-in-a-given-word-phase-or-sentence
---
Here we will learn how to write a program in Python which prints the number of occurrences of each character in a string.

There are multiple ways in Python, we are going to use **Counter** method.

## Introduction to Python Counter
Python provides a counter class that is the subclass of the collections modules. It is a special class of object data . The container data types that are part of the Collections module. The counter subclass is generally used for counting the hashable objects.

To make use of Counter we need to import it first as shown in the below given example:

```python
from collections import Counter
```

In the example below, a string is passed to Counter. It returns dictionary format, with key/value pair where the key is the element and value is the count. It also considers space as an element and gives the count of spaces in the string.

first lets Enter word , for example " Tahani", then a phase " due to avoiding chocolate" and then sentence " I always wanted to become a writer."

```python
from collections import Counter

# inter your text

in_txt = str(input("Enter your text"))

# using collections.Counter() to get
# count of each element in string
oup= Counter(in_str)

# printing result

print("Occurrence of all characters on your text is :\n"+ str(oup))
```

output 1:

```python
Occurrence of all characters in your text is :
 Counter({'a': 2, 'T': 1, 'h': 1, 'n': 1, 'i': 1})
```

output 2:

```python
Occurrence of all characters in your text is :
 Counter({'o': 4, ' ': 3, 'd': 2, 'e': 2, 't': 2, 'a': 2, 'i': 2, 'c': 2, 'u': 1, 'v': 1, 'n': 1, 'g': 1, 'h': 1, 'l': 1})
```

output 3:

```python
Occurrence of all characters in your text is :
 Counter({' ': 6, 'a': 4, 'e': 4, 'w': 3, 't': 3, 'o': 2, 'r': 2, 'I': 1, 'l': 1, 'y': 1, 's': 1, 'n': 1, 'd': 1, 'b': 1, 'c': 1, 'm': 1, 'i': 1})
```

and you can find the code available here in this [link](https://github.com/tahanijaber/string_Counter)
