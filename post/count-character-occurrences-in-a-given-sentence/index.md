---
title: "Count character occurrences in a given sentence using python"
author: "Eman Mahmoud"
date: 2021-09-22
description: "In this post we learn how count characters, special characters #*&@.... and spaces occurrences in a given word, phrase or sentence.Get word, phrase or sentence from user.sentence = input (\"Enter..."
categories: ["Python"]
image: images/41e56a_d8b32b9df85848e7974ce8d19dfd4498.webp
wix-url: https://www.datainsightonline.com/post/count-character-occurrences-in-a-given-sentence
---
![](images/41e56a_d8b32b9df85848e7974ce8d19dfd4498.webp)

In this post we learn how count characters, special characters #\*&@.... and spaces occurrences in a given word, phrase or sentence.

### Get word, phrase or sentence from user.
```python
sentence = input ("Enter sentence :")
```

### Function Count character occurrences in a given word, phrase or sentence.
```python
def count_characters(sentence):
    length = len(sentence)
    count = {'count':1}
    for i in range(length):
        if sentence[i] in count.keys():
            count[sentence[i] ] += 1
        else:
            count[sentence[i] ] = 1
    del count["count"]
    return count
```

*- length is a number of characters in sentence including spcial character @ $ #... and spaces.*

*- creat dictionary keys are characters and values are count of characters.*

*- count in beging has key 1 if I put count empty it is occure an error in if statement .*

*- for loop all string sentence from first character sentence[0] to last character sentence[lenght-1] as string in python is an array and order start from zero not one.*

*- if element sentence[i] in keys if element sentence[i] in not in keys creat new keys neme's sentence[i] and put value by one increase this value.*

*- delete from dictionary key count.*

### **Call function save it's return in** variable result

```python
result = count_characters(sentence)
```

### Display dictionary using loop
```python
for key in result :print(key , " : " , result[key])
```

**you can git code and see run of the code click here** https://github.com/eman888991/Data-Insight.git
