---
title: "Manipulating Data Patterns with Python Regex"
author: "Joana Owusu-Appiah"
date: 2021-10-20
description: "This article is divided into three parts and serves as an introduction to the extensive domain of regular expressions."
categories: ["Python"]
image: images/b8e7be_1520c94be8244f9fb1cd2bb080b48a96.webp
wix-url: https://www.datainsightonline.com/post/manipulating-data-patterns-regex-python
---
![published by Omar Flores on unsplash.com](images/b8e7be_1520c94be8244f9fb1cd2bb080b48a96.webp)

*published by Omar Flores on unsplash.com*

For some reason, the area code is being altered. Consider working on a database for a school where all of the student phone numbers have the same area code. How would you modify the dataset for a student population of more than 10,000?

![](images/b8e7be_bd3134a310c34c92b0746343f84606ad.webp)

Simply separate the area codes and make the necessary modifications. This operation is made possible with a programming concept known as ***Regular Expressions*** (regex for short, which we will use throughout the post).  Typing regular expressions for the umpteenth time will be a mouthful (or should I say, 'brainful').

This article is divided into three parts and serves as an introduction to the extensive domain of regular expressions. The sections are

1. Regular expressions (definition)
2. Understanding the syntax with code examples
3. Practical applications

Let's dive into it...

## 1.1 Regular Expressions
In simple terms, regular expressions are unique strings that are used to specify a search pattern. Regex uses a specific sequence of letters to identify the presence or absence of texts and splits the pattern into one or more sub-patterns. This concept is mainly useful in data cleaning, but more on the uses would come at the latter part of this post.

Python has an in-built module for creating and manipulating regular expressions, called **re.** The general syntax for regular expression's search is typically,

Match = re.search (pattern, str)

.search - is an **re** function

pattern - characterizes the search party

str - characterizes the string that is being searched

## 1. 2. Understanding Regex
What makes up a regular expression? You sure would need a function, a pattern, and a string. Some of the widely used functions include:

- re.search(pattern, string) - Returns the first instance of the pattern in a given text. The .search () function checks within the text for the first occurrence and returns a match object or None otherwise. Example:

```python
# finds the first occurence of the pattern

poem = 'Peter Piper picked a peck of pickled peppers; A peck of pickled peppers Peter Piper picked'
re.search('picked', poem)
```

output: <re.Match object; span=(12, 18), match='picked'>

- *re.match*(pattern, str) - The match function is used to check a pattern expression against a text. The .match() function checks for the presence of a pattern only at the beginning of the text. Example:

```python
# finds the occurence of the pattern at the start of the text
poem = 'Peter Piper picked a peck of pickled peppers; A peck of pickled peppers Peter Piper picked;'
z=re.match('picked', poem)
print(z)
```

output: None

NB: The difference between the .match() and .search() is that, while they both search to match a word, the .***match()*** only considers the start of the line, and the .**search()** runs through the entire text and settles on the first word.

- *re.findall*(pattern, str) - Returns all the occurrences of a pattern in a list. .findall() differs from .search() and .match() by printing the recurring outcomes. Example

```python
# returns a list of all the times the pattern occured

poem = 'Peter Piper picked a peck of pickled peppers; A peck of pickled peppers Peter Piper picked;'
re.findall('picked', poem)
```

output : ['picked', 'picked']

- *re.split*() - Splits the input based on each occurrence of a pattern. Example:

```python
poem = 'Peter Piper picked a peck of pickled peppers; A peck of pickled peppers Peter Piper picked;'

# the '\s' splits on white spaces
re.split(r'\s', poem)
```

output : ['Peter',
 'Piper',
 'picked',
 'a',
 'peck',
 'of',
 'pickled',
 'peppers;',
 'A',
 'peck',
 'of',
 'pickled',
 'peppers',
 'Peter',
 'Piper',
 'picked;']

- re.sub(pattern, repl, str) - Replaces an old pattern with a new one. Example: *It is about to get hot in here...*

```python
poem = 'Peter Piper picked a peck of pickled peppers; A         peck of pickled peppers Peter Piper picked;'
re.sub('picked', 'chewed', poem)
```

Output: 'Peter Piper chewed a peck of pickled peppers; A peck of pickled peppers Peter Piper chewed;'

Regular expressions are regularised (:D) with the help of some special characters, metacharacters. The functions of the characters are simplified in the table below:

|  |  |  |
| --- | --- | --- |
| Name | Symbol | Use |
| \ | backslash | escapes other special characters. If the pattern is to find all dots(.), without the '\', the pattern acknowledges the (.) as a special character. |
| [] | square bracket | represents a set or range of characters we wish to match. eg [abc] represents characters from a to c |
| ^ | Caret | checks whether a string begins with a character or not |
| $ | dollar | checks for the presence or absence of a group of characters at the end of strings |
| . | dot | checks for a single character except for a new line. |
| | | OR | checks for patterns before or after the OR symbol |
| ? | question mark | checks to produce patterns before the question mark |
| \* | star/asterisk | zero or more instances of the preceding character |
| + | plus | matches one or more of the instances. |

This post was intended to be very short and precise. But let's consider another important feature; they belong to a special group and their function is to make the patterns more efficient to use. The table below gives the frequently used ones:

|  |  |
| --- | --- |
| character | description |
| \A | Returns match if the pattern is at the beginning of the string |
| ​\d | returns digits present |
| \D | returns non-digits |
| \s | checks for white spaces |
| \S | checks for non-white spaces |
| \w | Checks for all alphanumeric characters, letters, numbers, and the underscore |
| \W | Checks for non-alphanumeric characters. |

We now look at practical applications of regex in python.

## 1.3. Practical Applications
Regex is used in a variety of data processing and wrangling operations by data scientists. Data preprocessing, natural language processing, pattern matching, extracting e-mails, and web scraping are among the applications.

For this post, we will practice two of the applications here.

1. E-mail extraction

```python
# extracting e-mails

mail = """From: adwumapa27@gmail.com\
Sent: 16th October, 2021\
To: owusea15@yahoo.com\
Subject: Paper Towel Ventures\
Thank you for choosing us. For bulk purchases, email our Ghanaian correspondent through \
plemanbee1vent@gmail.com\
best,\
Joana :D"""

re.findall("[\w.-]+@[\w.-]+", mail)
```

Output: ['adwumapa27@gmail.comSent',
 'owusea15@yahoo.comSubject',
 'plemanbee1vent@gmail.combest']

The example above considered an e-mail and extracted a couple of e-mails that had been included by the sender.

2. Data Cleaning

Using a practice project on DataCamp, *The Android App Market on Google Play.*The [data](https://www.kaggle.com/lava18/google-play-store-apps?select=googleplaystore.csv) was scraped from Kaggle. After importing the dataset into a pandas data frame, some of the columns had special characters like $, \*, etc

Category Rating Reviews Size Installs Type Price \

0 ART_AND_DESIGN 4.1 159 19.0 10,000+ Free 0

1 ART_AND_DESIGN 3.9 967 14.0 500,000+ Free 0

2 ART_AND_DESIGN 4.7 87510 8.7 5,000,000+ Free 0

3 ART_AND_DESIGN 4.5 215644 25.0 50,000,000+ Free 0

4 ART_AND_DESIGN 4.3 967 2.8 100,000+ Free 0

A regex saved the situation.

```python
# List of characters to remove
chars_to_remove = ['+', ',', '$']
# List of column names to clean
cols_to_clean = ['Installs', 'Price']

# Loop for each column in cols_to_clean
for col in cols_to_clean:
    # Loop for each char in chars_to_remove
    for char in chars_to_remove:
        # Replace the character with an empty string
        apps[col] = apps[cols_to_clean].apply(lambda x: x.str.replace(r'\D', ''))

# Print a summary of the apps dataframe
print(apps.head())
```

For the code above, the line

apps[col] = apps[cols_to_clean].apply(lambda x: x.str.replace(r'\D', ''))

replaced the non-digits in the column with an empty space. As explained in the blog, the '\D' character sections the non-digits in the column and replaces them with empty spaces.

The output now looks like this:

Category Rating Reviews Size Installs Type Price \

0 ART_AND_DESIGN 4.1 159 19.0 10000 Free 10000

1 ART_AND_DESIGN 3.9 967 14.0 500000 Free 500000

2 ART_AND_DESIGN 4.7 87510 8.7 5000000 Free 5000000

3 ART_AND_DESIGN 4.5 215644 25.0 50000000 Free 50000000

4 ART_AND_DESIGN 4.3 967 2.8 100000 Free 100000

**Regex to the rescue!!!**

The complete documentation on the **re** library can be found [here](https://docs.python.org/3/library/re.html).

The notebook that contains the code examples can be found [here](https://github.com/Joana-Mansa/regular_expression).

Your comments and suggestions could shape subsequent posts. Thank you for reading.

Love,

J.
