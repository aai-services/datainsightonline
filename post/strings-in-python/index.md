---
title: "Strings In Python"
author: "James Owusu-Appiah"
date: 2022-03-07
description: "What Is A Python String?Strings in python are enclosed in either double quotation marks or single quotation marks. They are a sequence of characters that are simply symbols. Usually, computers deal..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/strings-in-python
---
## What Is A Python String?
Strings in python are enclosed in either double quotation marks or single quotation marks. They are a sequence of characters that are simply symbols. Usually, computers deal with numbers(binary) so though we see characters they are computed and manipulated as a series of 0s and 1s. Encoding is the process of converting characters into numbers and decoding is the direct opposite of it. Unicode and ASCII are the most popular encodings used.

## Creating A Python String
Strings can be created by enclosing characters in single or double quotation marks.

```python
#A string in python
#Either double quotation or single quotations

#String in double quotation
the_string = "Hi"
print(the_string)

#String in single quotation
the_string = 'Hi'
print(the_string)
```

The output of the above code will be:

```python
Hi
Hi
```

## Accessing Characters In A String
The individual characters that make up a string are at specific positions known as indexes. The indexes start from 0 and run till the last character of the string. This is the positive style that starts from the beginning of the string to the other side. For the negative style, it starts from the last character which is at index -1 to the first character of the string.

```python
#Accessing characters of a python string
str = "Momentum"
print("The string is", str)

#Accessing the first character
print("The first character is", str[0])

#Accessing the last character
print("The last character is", str[-1])

#Accessing from the 3rd to last character
print("The 3rd to last character is", str[2:])
```

The output of the above code:

```python
The strings is Momentum
The first character is M
The last character is m
The 3rd to last character is mentum.
```

## Concatenation Of Strings
Concatenation is the joining of two or more strings into a single one. The + operator is used for concatenation in python. The \* operator is used to repeat the string a specific number of times.

```python
#Concatentation/Joining of 2 different strings
str1 = "Good"
str2 = "Morning"

#Joining with +
print("str1 + str2 =", str1+str2)

#Using *
print("str1*3", str1*3)
```

The output of the above code:

```python
str1 + str2 = GoodMorning
str1*3 GoodGoodGood
```

## Looping Through A String
Looping through a string is also known as iterating through a string. We can iterate through a loop using the **for loop.**

```python
#Iterating through a string to know the number of characters
str="Mangoes are sweet"
count = 0
for char in str:
    count+=1
print("The total number of characters are:", count)
```

The output of the above code is:

```python
The total number of characters are 17
```

## How A String Works In A Larger Program
A string serves as a data type for storing some user inputs to facilitate manipulation of the input in the program.
