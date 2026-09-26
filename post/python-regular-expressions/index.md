---
title: "Python Regular Expressions"
author: "Arpan Sapkota"
date: 2021-10-06
description: "The regular expressions can be defined as the sequence of characters which are used to search for a pattern in a string. The module re provides the support to use regex in the python program. The re..."
categories: ["Python"]
image: images/a8b2bc_5fb98657f40f4e419a8dedab17d11e07.webp
wix-url: https://www.datainsightonline.com/post/python-regular-expressions
---
![](images/a8b2bc_5fb98657f40f4e419a8dedab17d11e07.webp)

The regular expressions can be defined as the sequence of characters which are used to search for a pattern in a string. The module re provides the support to use regex in the python program. The re module throws an exception if there is some error while using the regular expression.

The re module must be imported to use the regex functionalities in python.

```python
import re
```

Regex Functions

The following regex functions are used in the python.

1 match - This method matches the regex pattern in the string with the optional flag. It returns true if a match is found in the string otherwise it returns false.

2 search - This method returns the match object if there is a match found in the string.

3 findall - It returns a list that contains all the matches of a pattern in the string.

4 split - Returns a list in which the string has been split in each match.

5 sub - Replace one or many matches in the string.

Forming a regular expression

A regular expression can be formed by using the mix of meta-characters, special sequences, and sets.

The findall() function

This method returns a list containing a list of all matches of a pattern within the string. It returns the patterns in the order they are found. If there are no matches, then an empty list is returned.

Consider the following example.

Example

```python
import re
str = "Who are you. Who is someone"
matches = re.findall("Who", str)
print(matches)
```

The match object

The match object contains the information about the search and the output. If there is no match found, the None object is returned.

Example

```python
import re
str = "Who are you. Who is someone"
matches = re.search("Who", str)
print(type(matches))
print(matches) #matches is the search object
```

The Match object methods

There are the following methods associated with the Match object.

span(): It returns the tuple containing the starting and end position of the match.

string(): It returns a string passed into the function.

group(): The part of the string is returned where the match is found.

Example

```python
import re
matches = re.search("Who", str)
print(matches.span())
print(matches.group())
print(matches.string)
```
