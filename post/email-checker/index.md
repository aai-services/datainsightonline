---
title: "Email Address Validity Checker using Python"
author: "ayenadykyaw1"
date: 2021-09-19
description: "Generally, to check the email address is valid, we have to look for '@' sign. Because every email address has @ sign. But specifically, we can check if the email is valid by looking at four parts..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/email-checker
---
Generally, to check the email address is valid, we have to look for '@' sign. Because every email address has @ sign. But specifically, we can check if the email is valid by looking at four parts which are name, @ sign, domain name, and top-level domain name.

For example. valid email address: [johnDoe.123@gmail.com](mailto:johnDoe.123@gmail.com)

- johnDoe.123 -- name ( can include upper case/lower case letters, digits and some special characters )
- followed by @ sign
- gmail -- domain name ( can include upper case/lower case letters, hyphen and period)
- **.**com -- top level domain ( can include at least two upper or lower case letters)

[#ref](https://www.datainsightonline.com/blog/hashtags/ref): John Pollard, What are the rules for email address syntax? – Validity Help Center ([returnpath.com](http://returnpath.com))

So as for python program to check a valid email address, use python regular expression [(https://github.com/python/cpython/tree/3.9/Lib/re.py)](https://github.com/python/cpython/tree/3.9/Lib/re.py) to make a pattern of valid email address. If the email matches with the pattern, then it will judge as a valid email address, if not it will judge as an invalid email address.

First we need to import re library.

```python
import re
```

Then, create a regex pattern

```python
pattern=r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
```

Check if the email matches with the pattern. If yes, print out as "Valid", otherwise print out as "Invalid"

```python
    if re.search(pattern,email):
        print("Valid Email")
    else:
        print("Invalid Email")
```

The complete code snippet is as follow.

```python
# Email Verifier...
import re
def emailVerifier(email):
    pattern=r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
    if re.search(pattern,email):
        print("Valid Email")
    else:
        print("Invalid Email")
```

To run this python function, just simply call the function name with one parameter which will be the email address you want to check.
