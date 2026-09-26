---
title: "Acronym generator from long words"
author: "Jihed 503"
date: 2021-09-14
description: "In this tutorial, you will learn how to write acronym generator using python.What is an acronym ?An acronym is a word formed from the initial letter or letters of each of the successive parts or..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/acronym-generator-from-long-words
---
In this tutorial, you will learn how to write acronym generator using python.

### What is an acronym ?
An acronym is a word formed from the initial letter or letters of each of the successive parts or major parts of a compound term.

![](images/2e83aa_e204fe00efc04d909914d09d7d6c5864.webp)

#### Step 1:
First, we will define the acronym generator function which will take a string argument.

```python
def acronym_generator(s):
```

#### Step 2:

Then, we make a list containing the string words.

```python
s_list = s.split()
```

#### Step 3:

Finally, we should implement a for loop to iterate on the list to concatenate the first character of each word to the acronym string.

```python
acr = "" #initialising the acronym
for i in s_list:
    acr += i[0]
```

then, we return acr

```python
return acr
```

#### Let's apply this code !

```python
acronym_generator("North Atlantic Treaty Organization")
'NATO'
```

another one

```python
acronym_generator("as soon as possible")
'asap'
```

#### [**source code**](https://github.com/Jihed503/data_insight/blob/main/acronym_generator.ipynb)
