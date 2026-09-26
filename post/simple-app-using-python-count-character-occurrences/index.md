---
title: "Counting Character Occurrences in a Phrase or Sentence using Python"
author: "abdelrahman.shaban7000"
date: 2021-09-01
description: "In this post we will deal with strings and character specifically we will count certain character occurrences in a given word or sentence or even phrases so let's start The main function In this..."
categories: ["Python"]
image: images/33c957_f327749fe24f451586939a84feb0d7b6.webp
wix-url: https://www.datainsightonline.com/post/simple-app-using-python-count-character-occurrences
---
In this post we will deal with strings and character specifically we will count certain character occurrences in a given word or sentence or even phrases so let's start

**The main function**

In this function we will implement the algorithm or how should our program count the targeted character so firstly we will see how the function looks like as here:

```python
def count_char(st,key):
    ''' This function will accept the word or phrase or sentence as first argument and
         the character which i call it key to be counted  as the second argument , and it will return the number
         of occurrences of that character in the string '''

    count=0
    for i in st:
        if i==key:
           count+=1
    return count
```

*First*: the *count_char* function takes two arguments the sentence or phrase where the character exists and the targeted character which we are seeking to count its occurrence.

*Second*: we will use the count variable which will contain the number of occurrences of the character. To access each element in the string we will loop over the entire sentence or the phrase character by character and for each character, we check if this character is the targeted character that we are interested in and if so we initialize the count variable by 1 and this goes for the entire sentence.

Finally we return the final result of the count variable

***Test the function***

Here we will give the function actual input to see the output :

```python
string=input('Enter ==> ').lower()
target=input('Targeted character ==> ').lower()

# we will count number of target charachter
print(count_char(string,target))
```

Here we took the sentence or the phrase from the user in the string variable. Also for the targeted character is in the target variable.

we pass these two variables to the *count_char* function.

Example for the output:

```python
Enter ==> Hello world I love programming
Targeted character ==> o
4
```

so we have 4 O's here.

Link to the GitHub repo  [here](https://github.com/Abdelrahman7000/datainsight-character_counter)
