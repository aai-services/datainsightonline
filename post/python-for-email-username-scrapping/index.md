---
title: "Python for Email Username Scrapping"
author: "Sabin Panta"
date: 2022-05-09
description: "Many times on our journey to learn to program, the tutorial might get hectic and you wanna do something for fun. For fun, I mean to use your python coding and link it with the activities in your..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-for-email-username-scrapping
---
Many times on our journey to learn to program, the tutorial might get hectic and you wanna do something for fun. For fun, I mean to use your python coding and link it with the activities in your daily life. When the code executes, it brings delight to your face whether it's a code of 1200 lines or a simple "email extraction code".
The procedure to scrap emails can be as follows:

1. Checking for validation of given input.
2. Use of regression expression.
3. Printing the necessary output.

First, the user is allowed to input the string using 'input' function of python and store it under a variable name.

Email=input("Enter the email address:")
if(len(Email.split('@'))==2):
 username=Email.split('@')[0]
 domain=Email.split('@')[1].split('.')[0]
 print("Username:",username)
 print("Domain name:",domain)
else:
 print("Invalid input")

A conditional statement 'if' in this code is used for testing whether the string belongs to the valid data. Split returns a list value as an output. If the email format is "firstname@domain", the string gets split into a list containing two elements as [firstname, domain], thus having two elements only and the condition holds true and the code runs further. Suppose by mistake the email gets entered as "firstname@domain@org", then the 'len' function which counts the element returns 3 values and the code doesn't run.

You might get a bit confused with the usage of [0] after split and the usage of two split in the second 'domain' variable. First, split returns the set of list when given a parameter to split the given string. To access each element we used list name along with the position of the elements. In first variable Username, [0] returns first element. The first split in the second variable split email into username and rest of the elements after '@' and [1] extract second elements in the list. But we aren't interested in any elements after '.'. For example, we need to only extract Gmail from ["gmail.com".](http://gmail.com) Thus, the program successfully splits the given email into the username and its domain.
Thank you for reading.
