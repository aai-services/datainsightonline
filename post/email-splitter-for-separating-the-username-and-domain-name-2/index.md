---
title: "Email Splitter for Separating Username from Domain Name"
author: "mrbenjaminowusu"
date: 2021-09-19
description: "This is a simple app to separate the username and domain name in an email. This app requires the user to enter an email of their choosing.First we allow the user to input their email by calling the..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/email-splitter-for-separating-the-username-and-domain-name-2
---
This is a simple app to separate the username and domain name in an email. This app requires the user to enter an email of their choosing.

First we allow the user to input their email by calling the input function as a string and assigning the output to the letter "a".

```python
a=input("PLEASE ENTER YOUR EMAIL: " )
```

Then using the if statement. if the character "@" is in the variable "a". We call the split method on the string "a" and index the first character and store it in the variable user_name. We do the same for the variable domain_name while indexing the second character. Finally we print the separated output if the statement. Else we print "email is not valid".

```python
if '@' in a:
    user_name= a.split('@')[0]
    dormain_name= a.split('@')[1]
else:
    print("your email is not valid.")
```

When the code is run it displays this output below

```python
PLEASE ENTER YOUR EMAIL: donbolingo@outlook.com
your username is: donbolingo and your domain name is: outlook.com
```
