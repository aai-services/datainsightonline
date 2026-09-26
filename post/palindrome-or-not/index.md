---
title: "Checking if a Word is Palindrome with Python"
author: "Shawon Shariff"
date: 2021-09-21
description: "This is a simple python app that will tell you wether your text is a palindrome or not.In this program, I have used the build-in reversed function to reverse the string.Steps:1. First we define a..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/palindrome-or-not
---
This is a simple python app that will tell you wether your text is a palindrome or not.

In this program, I have used the build-in reversed function to reverse the string.

**Steps**:

1. First we define a function called **ispalindrome()**
2. In this function, it first takes the input as an argument and lowercase the alphabets using pythons **lower()** method. Then it reverse the string using **reversed()** method.
3. Then we compare the string with the reversed string and if they match it prints positive and negative otherwise.

**Code**:

```python
def isPalindrome(s):
# Using predefined function to reverse to string print(s)
    str = s.lower()
    rev =''.join(reversed(str))
# Checking if both string are equal or not

    if (str == rev):
        print ("Yes. The word "+str+" is a Palindrome")

    else:
        print ("No. The word "+str+" is NOT a palindrome")

s = input()
ans = isPalindrome(s)
```

**Output:**

madam

Yes. The word madam is a palindrome.
