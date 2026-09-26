---
title: "Try and Except Structure in Python"
author: "Shawon Shariff"
date: 2021-10-06
description: "The Python try…except statement catches an exception. It is used to test code for an error which is written in the “try” statement. If an error is encountered, the contents of the “except” block are..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/try-and-except-structure-in-python
---
The Python try…except statement catches an exception. It is used to test code for an error which is written in the “try” statement. If an error is encountered, the contents of the “except” block are run.

**This is a way to eliminate or catch a traceback.**

- We surround a dangerous section of code with **try and except.**
- If ***try*** works, then ***except*** is skipped
- If ***try*** fails to work, then the ***except*** section is executed.

**Now, what is the dangerous section of code?**

- It's the section where our code might blow up into some errors like traceback. For example, **user input**.

When we accept input from the users, they can enter any kind of values that may or may not be a problem for our code. To avoid situations like traceback, we often handle this using ***Try and Except*** structure.

```python
#Here we are accepting a number from user.
num = input('Enter a number: ')
try:
    convert_num = int(num) # converting string into numeric
except:
    convert_num = -1

if convert_num >= 0:
    print('Nice work. You have entered ', convert_num)
else:
    print('Invalid Input')
```

Enter a number: 1234

```python
Output:
Nice work. You have entered 1234
```

Enter a number: abcd

```python
Output:
Invalid Input
```
