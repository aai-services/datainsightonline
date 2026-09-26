---
title: "Simple Python app: Email splitter for separating the username and domain name"
author: "TEMFACK DERICK"
date: 2021-09-10
description: "In my last Flask app, I needed to create a unique directory in /tmp directory for each user to perform some operations. In this case, as I have the email of each user when they log in, I decide to..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/trivial-python-app-email-splitter-for-separating-the-username-and-domain-name
---
In my last Flask app, I needed to create a unique directory in ***/tmp*** directory for each user to perform some operations. In this case, as I have the email of each user when they log in, I decide to create a unique directory base on that email.

The valid format of the email address consists of a set of **usernames** follow by **@** symbol and ends with **a domain name**. Know that, I split user email address based on **@** symbol and use the username to create user directory and subdirectory.

I wrote a simple function that takes an email and returns a list of usernames and domains respectively so that I can use the part I want.

```python
def split_email(email):
    return email.split('@')
```

As an email address is a string, we use the **split** function offer by the String class to split a string with a divider and return us a list of the element. Test of our function gives us the following result.

```python
split_email('test@example.com')

output : ['test', 'example.com']
```

This type of function can be useful in certain case. [This is github repo](https://github.com/tderick/email-spliter/blob/main/email%20spliter.ipynb)
