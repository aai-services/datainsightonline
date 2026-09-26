---
title: "Regular Expression in Python"
author: "Aayushma Pant"
date: 2021-10-06
description: "The term \"regular expression\", is also called regex or regexp which were widely used in all different programming languages. Suppose you need to find a substring present in a given string. For..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/regular-expression-in-python
---
The term "regular expression", is also called regex or regexp which were widely used in all different programming languages.

Suppose you need to find a substring present in a given string. For example "e" in word="Apple". Then the program checks each substring and at the end when word[4]=="e" it outputs as True. So this uses "sub" which is also one of the regex expressions. Overall we can say Regrex expression is an expression that is used to parse certain words, phrases, keywords or important text from a given input.

Lets us see the use of the regular expression

```python
import re
x = re.search("apple", "There is an apple lying in the basket.")
print(x)

OUTPUT: <re.Match object; span=(12, 17), match='apple'>
```

The above example illustrates the use of the 'search' method, which searches the word "apple" in a given sentence and is found to be in span 12:17.

Similarly other expressions like square brackets, "['and']", include a character class. For example:[ect] means either an "e", an "c" or a "t". Similarly [a-zA-Z] refers to any letters, words begin in alphabetical order. The character "-" includes all characters between A to Z and a to z.

```python
x = re.search(r"M[ae]l[av][kasi][kia]a" , "Malvika is going to Maldives")
print(x)

OUTPUT: <re.Match object; span=(0, 7), match='Malvika'>
```

Similarly, there are a lot of predefined classes that are used as regex expressions. Some of them are:

```python
\d  It match with the decimal numerical digits from [0-9].
\D  It is complement of \d consisting of non numeric characters.
```
