---
title: "How to validate an email address using Python"
author: "chalamohamed93"
date: 2022-09-22
description: "Email is a method of exchanging messages between people using. It is a widely-used communication medium that can also be used for signing up in the application. Keeping this in mind, lots of invalid..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/how-to-validate-an-email-address-using-python
---
Email is a method of exchanging messages between people using. It is a widely-used communication medium that can also be used for signing up in the application. Keeping this in mind, lots of invalid emails can cause the use of high bandwidth resulting in an increase in cost. So, the email field should be verified. **Python** has a couple of methods to verify whether an email is valid or not.

In this post we will introduce one of the way to verify and validate Emails :

***Using Python Regex***

Python has a module named ***re*** (regular expression or regex). The re module provides a set of powerful regular expression facilities, which allows you to quickly check whether a given string matches a given pattern (using the match function), or contains such a pattern (using the search function).

We can simply call in our program as:

import re

To verify email, we will use re module one of the function called *search,* in the following code, we are utilising the re module along with the search() method (built-in function) include inside verify_email function which return a True or False and has one argument should be a string.

def verify_email(email):
 """function to verify email patterns"""
 verify = re.search(pattern, email)

 # check if verify email returns
 # Match email or None
 if verify:
 print("A valid email")
 else:
 print("Invalid one")

Finally, we should ask the user to enter an Email address, with the input built-in function and use the function above (verify_email) to validate the email.

email = input("Please write your email address :")
verify_email(email)
