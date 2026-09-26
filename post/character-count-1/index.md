---
title: "Character Counter using Python"
author: "ayenadykyaw1"
date: 2021-09-19
description: "In this post, you can learn how to count the number of occurrences of each character in a word or phrase or a sentence. For example: The word \"Apple\" contains A - 1 time, p - 2 times, l - 1 time and..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/character-count-1
---
In this post, you can learn how to count the number of occurrences of each character in a word or phrase or a sentence.

For example: The word "Apple" contains A - 1 time, p - 2 times, l - 1 time and e - 1 time.

The following python function can be used for this purpose.

```python
# character count function...
def charCount(s):
    # create an empty dictionary
    charLib=dict()
    for i in s:
        if i not in charLib:
            charLib[i]=0
        charLib[i]+=1
    return charLib
```

Python **dictionary** is used as a Character Count Database. "**For loop**" is used to iterate through the string ( word, phrase, or sentence).

If the character is not in dictionary yet, it will be initialized as 0 and insert into dictionary ==> **charLib[i]=0**  where **i** will be the character as well as the **key** of a dictionary whereas **0** will be the **value**.

Then, all the word count (values of each key) will be added by 1 when it is found in a word.

Finally, we will get a complete dictionary with the characters as keys and the associated count as values.

To test the function, we can just simply call the function name and pass a string parameter like this.

```python
#test function
occurrences= charCount("my name is ayeaye")
occurrences.pop(' ') # to delete space character if it is in dictionary
for char,occur in occurrences.items():
    print(char+" contains "+str(occur)+" times ")
```

If we run this, we can see the following output.

```python
m contains 2 times
y contains 3 times
n contains 1 times
a contains 3 times
e contains 3 times
i contains 1 times
s contains 1 times
```

One last thing, I used **pop()** function to delete the space count character if the string has spaces. The above dictionary will count for space also because space is also a character with length one. However, we do not usually want space. So I delete using pop function by using space as a key. The pop() function will delete the given key and its associated values and return the updated dictionary. The pop() function can return the updated dictionary if the key was found. If the key was not found, it will return the same dictionary.
