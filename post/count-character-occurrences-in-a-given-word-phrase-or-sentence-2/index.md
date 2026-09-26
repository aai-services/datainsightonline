---
title: "Count character occurrences in a given word, phrase or sentence"
author: "aya abdalsalam"
date: 2022-01-08
description: "Count how many times character found in phrase or a sentence"
categories: ["General"]
image: images/d803c7_e2b32648dfa24bbb8559c0ad5ae7a3b8.webp
wix-url: https://www.datainsightonline.com/post/count-character-occurrences-in-a-given-word-phrase-or-sentence-2
---
we will count how many times an character appears in a word or a phrase or a sentence

There is many ways to count occurrences of a character I will introduce some of them

1. for loop

2. count()

3. regular expression

4. pandas library

## For loop
using for loop is a good way to count number of occurrence of a character in a word or sentence

```python
def countWord(word):
    count = 0
    for i in word:
        if i == charToCount:
            count = count + 1
    print("Your character " + charToCount + " is found " + str(count) + " Times")
word = input('Enter your word : ')
charToCount = input('Enter Your character : ')
countWord(word)
```

output:

```python
Enter your word : Working From home is good
Enter Your character : i
Your character i is found 2 Times
```

## count()
using count function can help you , it will return how many times this character is found in this string or sentence

```python
def countWord(word):
    print("Your character " + charToCount + " is found " + str(word.count(charToCount))+ " Times")

word = input('Enter your word:  ')
charToCount = input('Enter Your character : ')
countWord(word)
```

output:

```python
Enter your word: Working From home is good
Enter Your character: i
Your character i is found 2 Times
```

## Regular Expression
regular expression is a way to search in a string and make matching and by matching you can use many function such as **find()** , **findall()** and **search()** in regular expression you need to import its library which called **re**

```python
import re
def countWord(word):
    print("Your character " + charToCount + " is found " + str(len(re.findall(charToCount, word))) +" Times")
word = input('Enter your word :  ')
charToCount = input('Enter Your character : ')
countWord(word)
```

output:

```python
Enter your word:  Working From home is good
Enter Your character: i
Your character i is found 2 Times
```

## Pandas Library
There is a function in pandas called **value_counts** by it It will count every character count in a new line . You need to pass string as a series object and you need to import pandas

```python
import pandas as pd
def countWord(word):
    print(pd.Series(list(word)).value_counts())
word = input('Enter your word ')
countWord(word)
```

output:

```python
Enter your word Working From home is good
o    5
     4
r    2
i    2
g    2
m    2
W    1
k    1
n    1
F    1
h    1
e    1
s    1
d    1
dtype: int64
```
