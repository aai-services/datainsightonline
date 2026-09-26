---
title: "Email Splitter App"
author: "Shawon Shariff"
date: 2021-09-21
description: "This is a simple python app that takes a lists of emails and separate the username and the domain name.1. First let's create a list with some dummy emails.2. Create a for loop to visit each email..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/email-splitter-app
---
This is a simple python app that takes a lists of emails and separate the username and the domain name.

1. First let's create a list with some dummy emails.
2. Create a for loop to visit each email from the list.
3. Each time the loop executes, it will split the email into two separate parts based on '@'
4. The first part is the username and the second part is the domain name. And the program will print it out.

**Code :**

```python
lst = ["random1@gmail.com","random2@yahoo.com"]
for i in lst:
    split = i.split('@')
    domain = split[1]
    user = split[0]
    print("username : ",user)
    print("domain : ", domain)
    print("\n")
```

**Output :**

username : random1

domain : gmail.com

username : random2

domain : yahoo.com
