---
title: "Password Generator from Username using Python"
author: "ben othmen rabeb"
date: 2021-09-06
description: "In this post, you will learn how to create a random string passwords in Python. Using a random and string module, we can write our own password generator.Steps to Create a Random String1- Import..."
categories: ["Python"]
image: images/bfaec5_069b1de04f5b476dac7a42928b826854.webp
wix-url: https://www.datainsightonline.com/post/password-generator-from-username-using-python
---
![](images/bfaec5_069b1de04f5b476dac7a42928b826854.webp)

In this post, you will learn how to create a random string passwords in Python. Using a random and string module, we can write our own password generator.

## Steps to Create a Random String

**1- Import String and Random modules**

**2- Use the string constant digits and symbols and the function upper() and lower()**

**3- Use a for loop and random.choice() function to choose characters from a source**

**4- Generate a password generator**

Let's code a function that generates a password from the username.

1- Import modules

![](images/bfaec5_5e4265cfd79d4e059eb620b82cab35aa.webp)

2- Input the username to generate the password

![](images/bfaec5_5b691ecec69841398b799237d98c7171.webp)

3- Define our function generate_password

![](images/bfaec5_9cf98d75ed2b49378cd08d2bca02f519.webp)

3-1 Convert the username to uppercase and lowercase letters.

store numbers and symbols

"digits contain '0123456789'

punctuation contain all special symbols '!”#$%&'()\*+,-./:;<=>
 @[\]^_`{|}~.' "

![](images/bfaec5_cd4d97957f0943ecbc1eb6dbcd09b941.webp)

3-2 Generate random characters from lowercase, uppercase
 username and all (numbers and symbols)

![](images/bfaec5_b77a4aa6c0f84a3a9deaf3e1c97670ac.webp)

3-3 Concatenate and return password from username, numbers and symbols

![](images/bfaec5_d3eec48b46734a1eaf99e175d5da74f5.webp)

## There is our function below

![](images/bfaec5_00af7bc5a58a4a52aa6799915415c5e0.webp)

## Let's test our funtion
![](images/bfaec5_3605fdaab4dd4e528d8bd80e3b9762da.webp)

## Output:
![](images/bfaec5_c4cebe1f0e474dd8ab2a21d04acfb152.webp)

You can find the whole project on [my Github](https://github.com/rabebbenothmen/Data-Insight2021/tree/main/Assignments)
