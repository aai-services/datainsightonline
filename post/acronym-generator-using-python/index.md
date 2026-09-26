---
title: "Acronym generator using Python"
author: "Rashidat Sikiru"
date: 2021-09-13
description: "An acronym generator generates a word from a phrase using keyword abbreviations. Individual letters from the words contained in a phrase are used to create a new word, which we refer to as acronym..."
categories: ["Python"]
image: images/3053d2_237e3a86cad742c3a8882e144d2343f7.webp
wix-url: https://www.datainsightonline.com/post/acronym-generator-using-python
---
![](images/3053d2_237e3a86cad742c3a8882e144d2343f7.webp)

An acronym generator generates a word from a phrase using keyword abbreviations. Individual letters from the words contained in a phrase are used to create a new word, which we refer to as acronym.

## How an acronym generator works?
An Acronym Generator will take a String as an input and it will return the initials of all the words in the String.

## How to build an acronym generator?
### Step 1
To begin with , we need a phrase or word from the user. We can do that using **input()** method.

```python
user_input = input("Enter a phrase: ")
```

We have stored the user input in a **user_input** variable.

### Step 2
Now that we have stored our user input, we must ignore words like **'of' , 'and'**  from the user input as most of the time, these words are not considered for acronyms.

Also, we need to separate each word and store it individually in a form of a list so that we can easily iterate through it.

```python
phrase =(user_input.replace('of','')).replace('and','').split()
```

In the **user_input.replace()** , we are using **.replace()** function to ignore 'of' and 'and' from the input, if any.

Then we are using **.split()** function to break down the string into individual words and store them as a list in **phrase** variable.

### Step 3
We need an empty string variable to store our acronym. Let's quickly create one.

```python
acronym = ""
```

### Step 4
Now let's create a for loop which will help iterate through the **phrase** variable

```python
for word in phrase:
    acronym = acronym + word[0].upper()
```

In **acronym = acronym + word[0]**, we are slicing off the first letter of words stored in **phrase** using slicing operator and adding it to our **acronym** variable.

We are also using **.upper()** function to capitalize the acronyms.

### Step 5
Lastly, just add a **print** statement which will print out the acronym as our output.

```python
print("The acronym of " + " " + user_input + " " + "is" + " :" + " " + acronym)
```
