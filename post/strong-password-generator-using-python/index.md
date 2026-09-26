---
title: "Strong Password Generator using Python"
author: "Ibrahim M. A. Nasser"
date: 2021-08-30
description: "Your passwords grant access into your own personal kingdom, so you are probably thinking 'what are the best practices to create a strong password' to protect your accounts against these..."
categories: ["Python"]
image: images/ce80af_dee30ec52302417c8c39d60bb84d6dbf.webp
wix-url: https://www.datainsightonline.com/post/strong-password-generator-using-python
---
![](images/ce80af_dee30ec52302417c8c39d60bb84d6dbf.webp)

Your passwords grant access into your own personal kingdom, so you are probably thinking 'what are the best practices to create a strong password' to protect your accounts against these cybercriminals. If your passwords were part of a breach, you will want to change them immediately.

So, what's the solution? **Uncrackable passwords**.

You have to stay away from the obvious. Never use sequential numbers or letters, and for the love of all things cyber, do not use “*password”* as your password*.* Come up with unique passwords that do not include any personal info such as your name or date of birth. If you’re being specifically targeted for a password hack, the hacker will put everything they know about you in their guess attempts.

Passwords should contain three of the four character types:

1. Uppercase letters: A-Z
2. Lowercase letters: a-z
3. Numbers: 0-9
4. Symbols: ~`!@#$%^&\*()_-+={[}]|\:;"'<,>.?/

Let's code a function that generates a strong password from the username.

1- Import Libraries

```python
import random
import string
```

2- Take the username from the user

![](images/ce80af_955c841b976c47f798be37711ea4e767.webp)

3- Let's define our function: generate_password(username)

![](images/ce80af_58c16fb36a6049fbb9222023ee90013e.webp)

4- Convert the first and last character of the username to uppercase so it contains uppercase and lowercase letters.

![](images/ce80af_bf7a13a4f43240178b6599026b6f194c.webp)

5- Store number and symbols form string library.

![](images/ce80af_e41f86e0d89c435389cc100a3cada488.webp)

That's how these variables look like

![](images/ce80af_7a3902bb0f9740c6ba1be0d47484f56e.webp)

6- Generate random numbers and symbols of 5 length

![](images/ce80af_fcc2c8d822984531848cec72f851d8fb.webp)

7- Concatenate the edited username with the random numbers and symbols and return the generated password

![](images/ce80af_8385f90f2f954308b14e01c838786a2f.webp)

**That's it!**

Here is how our function should look like:

![](images/ce80af_b0d4cc1a2874470ab36b8c717cd9c4cd.webp)

Let's test our function with new username: datainsight

![](images/ce80af_133b280c5ff64260b26865831cb18ec0.webp)

**Congratulations on building your strong password generator with python!**

You can find the whole project on my [GitHub.](https://github.com/96ibman/datainsight_datascience_program/tree/main/password_generator)
