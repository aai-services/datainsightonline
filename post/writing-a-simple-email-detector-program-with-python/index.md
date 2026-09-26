---
title: "WRITING A SIMPLE EMAIL DETECTOR PROGRAM WITH PYTHON"
author: "ukaegbu daniel"
date: 2022-06-16
description: "Have you ever wondered how a website can tell the difference between what is an email and what is not? You probably type your email wrongly into a website or online form and the program outputs..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/writing-a-simple-email-detector-program-with-python
---
Have you ever wondered how a website can tell the difference between what is an email and what is not? You probably type your email wrongly into a website or online form and the program outputs "wrong email please check or re-enter the email.

We all have been there before, This is possible because this software is developed with programs that can differentiate between what's an email and what is not. This software is written in a way that searches for specific characters that are characteristics of an email such as @, Gmail, mail, yahoo, etc. If this program can find these characters the websites process your request. if not, the program outputs an error calling your attention to the wrong input which in turn means that you check and correct it. This program can be written in just a few lines of code. However advanced and sophisticated software utilizes artificial intelligence for this. Below is a short tutorial on how to write this program in python.

```python
#in this tutorial we are going to write a simple program used in validating an email
#First we import re module which helps with provides support for regular expression
import re
#next we make a regular expression for validating an email
regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#Define a function for email checking
def Check(email):
    #we pass a regular expression and the email into the full match method()
    if(re.fullmatch(regex,email)):
        print('Valid email')

    else:
        print ('Invalid email')
 #checking a program
email='Ukaegbudaniel33@gmail.com'
Check(email)
```
