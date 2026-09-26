---
title: "Acronym Generator in Python"
author: "Thiha Naung"
date: 2021-09-03
description: "The acronym is a word (such as NATO, radar, or laser) formed from the initial letter or letters of each of the successive parts or major parts of a compound term. Let's generate an acronym in python..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/acronym-generator-in-python-1
---
The acronym is a word (such as *NATO, radar*, or *laser*) formed from the initial letter or letters of each of the successive parts or major parts of a compound term.

Let's generate an acronym in python.

First, define function.

```python
def acronym(letter):
    lst = letter.split(" ")
    if len(lst) < 3:
        return("Letter should be 3 or more words.")
    else:
        first_words = [i[0] for i in lst if i not in ['of','on','as']]
        return(f"Acronym for '{letter}' is '{''.join(first_words).upper()}'")
```

- The Second-line of code is to split the letters at spaces.

- Then, if the length of the letter is less than 3, it will return "Letter should be 3 or more words.

- If the length of the letter is 3 or more, from the list of each word, preposition words are removed and take the first character and append to list named 'first_words'. Words that want to be removed, can add as you wish.

- Then join each word from the list and make them into uppercase.

Let's see the results.

```python
print(acronym("north atlantic treaty organization"))
> Acronym for 'north atlantic treaty organization' is 'NATO'

print(acronym("united states of america"))
> Acronym for 'united states of america' is 'USA'

print(acronym("machine learning"))
> Letter should be 3 or more words.
```

Yes, it works. That's all.

Here's my GitHub link for that.

[Github](https://github.com/thihanaung-thnn/data_insight/blob/main/notebooks/acronym.ipynb)
