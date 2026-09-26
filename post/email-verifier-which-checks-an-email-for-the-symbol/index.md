---
title: "Email verifier, which checks an email for the @ symbol."
author: "Areeg Tarek"
date: 2021-10-12
description: "In this program, we are using the search() method of re module. so let’s see the description of it. re.search() : This method either returns None (if the pattern doesn’t match), or re.MatchObject..."
categories: ["General"]
image: images/05f47f_4568ad83dbb24626be21641fa5b15023.webp
wix-url: https://www.datainsightonline.com/post/email-verifier-which-checks-an-email-for-the-symbol
---
![](images/05f47f_4568ad83dbb24626be21641fa5b15023.webp)

In this program, we are using the search() method of re module. so let’s see the description of it.
**re.search() :** This method either returns None (if the pattern doesn’t match), or re.MatchObject contains information about the matching part of the string. This method stops after the first match, so this is best suited for testing a regular expression more than extracting data.

Let’s see the Python program to validate an Email :

```python
# Python program to validate an Email

# import re module

# re module provides support
# for regular expressions
import re

# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Define a function for
# for validating an Email


def check(email):

    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")


# Driver Code
if __name__ == '__main__':

    # Enter the email
    email = "ankitrai326@gmail.com"

    # calling run function
    check(email)

    email = "my.ownsite@our-earth.org"
    check(email)

    email = "ankitrai326.com"
    check(email)
```

Output

```python
Valid Email
Valid Email
Invalid Email
```
