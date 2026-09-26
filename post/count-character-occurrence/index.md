---
title: "Counting Character Occurrence using Python"
author: "Omar Mohamed"
date: 2021-09-05
description: "Here in this article, we demonstrate how to get the count of the occurrence of a letter / character in a word / phrase.Here is the link for the notebook:Python Notebook: Count Character Occurrence..."
categories: ["Python"]
image: images/c4edc8_12a8da566d584ef9b11b48e70fda51f6.webp
wix-url: https://www.datainsightonline.com/post/count-character-occurrence
---
Here in this article, we demonstrate how to get the count of the occurrence of a letter / character in a word / phrase.

Here is the link for the notebook:

### [Python Notebook: Count Character Occurrence](https://github.com/omarmohamed2011/Count_characher_occurences/blob/main/Count_char_occurrences.ipynb)

![](images/c4edc8_12a8da566d584ef9b11b48e70fda51f6.webp)

First thing the code is divided into functions, each function does a specific part of the code:

1) get_string function:

```python
def get_string():
    print('Enter your input string:')
    phrase = input()
    character = 'abc'
    while len(character) >1:
        print('Enter the character to count occurrences:')
        character = input()
        if len(character) >1:
            print('Type a valid input')
   return phrase.lower(),character.lower()
```

The first function is called get_string() used to get user input of the phrase or word, and the character that needs to be counted. The phrase is an input taken from the user in a very straightforward method, however the step of getting a character from the user is a bit complicated here, as we don't have a guarantee that the user will give a one letter valid input, though the value of the character is initialized with more than one character which is definitely not the right case, then we enter a while loop that loops until user give a valid one character / letter, if not; the user gets notified that the input is not valid until condition is met and user gives a one letter to count occurrence, the function returns the phrase and the letter in a lower case to ensure comparison is done right, because comparison functions are case sensitives and will consider upper case and lower case of the same letter as different letters; ex: ( 'A' and 'a') are considered as different letters.

2) count_occurrence function:

```python
def count_occurrences(phrase,character):
    counter = 0
    for letter in phrase:
        if letter == character:
            counter +=1
    return counter
```

The function gets two inputs; the phrase and the character we need to count.

The function simply loops over all letters in the phrase, compares them to the character and increase the counter whenever the letter in the phrase is the same as the character, and returns the counter in the end.

3) print_count function:

```python
def print_count(character,count_char):
    print('The count of the letter {} in the given sentence is {}'.format(character,count_char))
```

Simply takes the character and its count and prints the character and how may times it appears.

Then we easily run the functions in the convenient order to get our result.

```python
if __name__ == '__main__':
    phrase,character = get_string()
    count_char = count_occurrences(phrase,character)
    print_count(character,count_char)
```

As easy as it looks like the code can be easily done, executed in an organized way. Hopeful that the article has taught you something, comment for any problems found and have a nice day.
