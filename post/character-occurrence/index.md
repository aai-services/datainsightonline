---
title: "Character occurrence"
author: "ashioyajotham"
date: 2021-09-20
description: "Think of the len() function, but this method has a much scope enabling you to use of bigger strings or character occurrences. We use dictionaries iterated over by for loops under a function.In the..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/character-occurrence
---
Think of the len() function, but this method has a much scope enabling you to use of bigger strings or character occurrences. We use dictionaries iterated over by for loops under a function.

In the dictionary, we take count of characters over a loop

# Count character occurrences in a given word, phrase or sentence

def charCount(s):

# create an empty dictionary

charLib=dict()

for i in s:

if i not in charLib:

charLib[i]=0

charLib[i]+=1

return charLib

[#test](https://www.datainsightonline.com/blog/hashtags/test) function

occurrences= charCount("ASHIOYA LOVES DATA SCIENCE")

occurrences.pop(' ') # to delete space character if it is in dictionary

for char,occur in occurrences.items():

print(char+" contains "+str(occur)+" times ")

N/B The pop() is ONLY used if it's in a string otherwise it wouold be an error
