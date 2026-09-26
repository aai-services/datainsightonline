---
title: "Python Program to Check the Validity of Password"
author: "Alberta Johnson"
date: 2021-09-22
description: "The above picture gives an idea of what this blog is about. This blog will discuss how to check the validity of passwords. A password, sometimes called a passcode, is secret data, typically a string..."
categories: ["Python"]
image: images/1fa3fb_f0350633877d46948747c65bbeb108e2.webp
wix-url: https://www.datainsightonline.com/post/python-program-to-check-the-validity-of-password
---
![](images/1fa3fb_f0350633877d46948747c65bbeb108e2.webp)

The above picture gives an idea of what this blog is about.

This blog will discuss how to check the validity of passwords.

A **password**, sometimes called a **passcode**, is secret data, typically a string of characters, usually used to confirm a user's identity.

Now let's consider a simple app, written in python language to vheck the validity of passwords.

Primary conditions for password validation :

Minimum 8 characters.

The alphabets must be between [a-z]

At least one alphabet should be of Upper Case [A-Z]

At least 1 number or digit between [0-9].

At least 1 character from [ _ or @ or $ ].

Input : R@m@_f0rtu9e$

Output : Valid Password

Input : Rama_fortune$ Output : Invalid Password

Explanation: Number is missing

Input : Rama#fortu9e Output : Invalid Password Explanation: Must consist from _ or @ or $

Now let's write some codes to check if our password is valid;

```python
password = "R@m@_f0rtu9e$"

is_valid = True
reason = ''

while True:
    if (len(password)<8):
        is_valid = False
        reason = 'The length of the password is not up to 9 characters'
        break
    elif not re.search("[a-z]", password):
        is_valid = False
        reason = 'There is no lower case alphabet in the password'
        break
    elif not re.search("[A-Z]", password):
        is_valid = False
        reason = 'There is no upper case alphabet in the password'
        break
    elif not re.search("[0-9]", password):
        is_valid = False
        reason = 'There is no digit in the password'
        break
    elif not re.search("[_@$]", password):
        is_valid = False
        reason = 'The password requires atleast one symbol'
        break
    elif re.search("\s", password):
        is_valid = False
        reason = 'The password contains a whitespace'
        break
    else:
        break


if is_valid is False:
    print("{} , therefore it's invalid".format(reason))
else:
    print('The password {} is valid'.format(password))
```

Output :

```python
The password R@m@_f0rtu9e$ is valid
```

Conclusion

Hurray!!, as seen our password is valid. The above approach is used to check the validity of a password.
