---
title: "Acronym generator from words or phrases"
author: "Sakayo Toadoum Sari"
date: 2021-09-01
description: "Generally, an acronym generator will take as an input a string and will return all the first elements of words in the string as an uppercase.The first thing to do is asking the user to enter a phrase..."
categories: ["General"]
image: images/b94828_497b4ab8bf25468b94951e61be00a6b0.webp
wix-url: https://www.datainsightonline.com/post/acronym-generator-from-long-words-or-phrases
---
Generally, an acronym generator will take as an input a string and will return all the first elements of words in the string as an uppercase.

![](images/b94828_497b4ab8bf25468b94951e61be00a6b0.webp)

```python
The first thing to do is asking the user to enter a phrase using input() method in python
```

```python
user_input = input("Enter a phrase: ")
```

We have now store the phase into our variable user_input. After that, we are going to separate each word and store in a list such that we can easily iterate through. The list is assign to the variable phrase

```python
phrase = user_input.split()
```

Now we need to create our variable acronym as an empty string.

```python
acronym = ""
```

By using a for loop, we will loop our new variable word through our list phrase.

```python
for word in phrase:
    acronym = acronym + word[0].upper()
```

With acronym + word[0] we are slicing and assigning to our variable acronym which is at the beginning an empty string the first letter of the word store in phrase and using .upper() we are changing the letter into capital letter to form the acronym.

```python
print("The acronym for your phrase is ",acronym + ".")
```

The print function will print out our acronym.

Let us try it out.

```python
Enter a phrase: Artificial Intelligence
The acronym for your phrase is  AI.
```

[Source code](https://github.com/Toadoum/Data-Insight-Certification-Data-Science-program-/blob/main/Acronym%20generator%20from%20long%20words%20or%20phrases.ipynb)
