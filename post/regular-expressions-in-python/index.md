---
title: "Regular Expressions in Python"
author: "Nargiz Huseynova"
date: 2021-10-06
description: "A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. And it can be used to check if the string contains the specified search pattern or not. The Python Programming..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/regular-expressions-in-python
---
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. And it can be used to check if the string contains the specified search pattern or not. The Python Programming language has a built-in package called *re* which can be used to work with regular expressions. Simply you can use the *import* keyword to import this package. When you import the *re* module you can start using its functionalities.

#### The search() function

Let us take a simple example to search the string to see if it starts with "The" and ends with "Azerbaijan". Here is the code snippet.

```python
import re
text = "The match in Azerbaijan"
x = re.search('^The.*Azerbaijan$',text)
print(x)
```

"^" and "$" signs mean starts with and ends with respectively. "." indicates any character except newlines, and "\*" means zero or more occurrences.

The regular expression module offers a set of functions that allows you to search a string for a match. In this example, we used a search function that returns a match object if there is a match anywhere in the string. When we run the above code we get:

```python
<re.Match object; span=(0, 23), match='The match in Azerbaijan'>
```

This is our reference. If you want to see if the searching process is matching or not you can use the if conditional like below.

```python
if x:
    print("Yes! We have a match!")
else:
    print("No match")
```

In this example we have a match for x, so the test expression for the if statement is true and we get as a result:

```python
Yes! We have a match!
```

#### The findall() function
Let us take another look at the *findall()* function of *re*.

```python
#findall() function
txt = "The rain in Azerbaijan"
x = re.findall("ai", txt)
print(x)
```

The *findall()* function returns a list containing all matches.

```python
['ai', 'ai']
```

The list contains the matches in the order they are found. If no matches are found, an empty list is returned:

```python
x = re.findall("Brazil", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
```

```python
[]
No match
```

#### The split() function

The split() function returns a list where the string has been split at each match:

```python
x = re.split("\s", txt)
print(x)
```

When we run the above code we get:

```python
['The', 'rain', 'in', 'Azerbaijan']
```

You can control the number of occurrences by specifying the maxsplit parameter:

```python
x = re.split("\s", txt, 1)
print(x)
```

Here we split the string only at the first occurrence:

```python
['The', 'rain in Azerbaijan']
```

#### The sub() Function
The sub() function replaces the matches with the text of your choice:

```python
x = re.sub("\s", "%", txt)
print(x)
```

We replace every white-space character with the "%" sign:

```python
The%rain%in%Azerbaijan
```

You can control the number of replacements by specifying the count parameter:

```python
x = re.sub("\s", "%", txt, 2)
print(x)
```

```python
The%rain%in Azerbaijan
```

Regular Expressions are widely used for validation purposes, like email validation, url validation, phone number validation and so on.

You can find the jupyter notebook and python script of this code in this [link](https://github.com/iamNargiz/Py_concepts_RegEx).
