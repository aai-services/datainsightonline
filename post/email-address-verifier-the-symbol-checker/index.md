---
title: "Email Address Verifier: @ symbol checker"
author: "NaumanKhanKhattak"
date: 2021-09-22
description: "The email address format is one which must have some unique user name before @ and also have a domain name after that. In this very simple mini python project we are going to check whether there is..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/email-address-verifier-the-symbol-checker
---
The email address format is one which must have some unique user name before ***@*** and also have a domain name after that. In this very simple mini python project we are going to check whether there is any **@** symbol before domain name. The objective is how we access a string characters and check them for some specific character at desired location.

**Step: 1**

Typing the below code in your jupyter notebook or any other python IDE. It is simply getting the email address from input.

```python
e_address=input("Enter any Email address:")
print(e_address)
```

**Step: 2**

In the second we will check the input character by character to check the location of **@** symbol.

```python
verified=False
count=0
for i in range(len(e_address)):
    print(e_address[i])
    if (e_address[i]=='@')& ((i >0)&(i< len(e_address)-1)):
        verified=True
```

In above lines of code we are iterating the loop over e_address variable and then in the if statement we have given the condition to check if the **@** symbol is some where not at the ends of the given input email address.

**Step: 3**

In the last step we are just giving the message whether it is an email address or not with the following lines of code.

```python
if verified:
    print("looks like you have typed some email addree.")
else:
    print("That's not an email address.")
```

**Conclusion:**

Although this is a very naive solution for email address @ checker but the learned concept of accessing string characters and the if statements can further be used in a same way to enhance and add an extra functionality. For example to check if the domain name and user name is valid or not.
