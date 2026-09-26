---
title: "Python Program to Check Prime Number"
author: "Marawan Mohamed"
date: 2022-01-30
description: "In this article an example to check whether an integer is a prime number or not using for loop and if...else statement. If the number is not prime, it's explained in output why it is not a prime..."
categories: ["Python"]
image: images/c46c85_bd13c07d54f34048baffdd8a7ac3ea10.webp
wix-url: https://www.datainsightonline.com/post/python-program-to-check-prime-number
---
![](images/c46c85_bd13c07d54f34048baffdd8a7ac3ea10.webp)

In this article an example to check whether an integer is a prime number or not using for loop and if...else statement. If the number is not prime, it's explained in output why it is not a prime number.

**Understanding Prime Number**

A positive integer greater than 1 has no other factors except 1 and the number itself is called a prime number. 2, 3, 5, 7, etc. are prime numbers as they do not have any other factors.

**Creating the App**

We will start by taking a number from the user.

![](images/c46c85_4454dc097cf946cd8872bbb72b19e499.webp)

In this program, we have checked if the num is prime or not. Numbers less than or equal to 1 are not prime numbers. Hence, we only proceed if the num is greater than 1 and check if the num is exactly divisible by any number from 2 to num - 1. If we find a factor in that range, the number is not prime, so we set a flag to True and break out of the loop.

![](images/c46c85_80ebc2fd862e4585bc64ec22438c7475.webp)

Outside the loop, we check if the flag is True or False.

- If it is True, the num is not a prime number.
- If it is False, the num is a prime number.

![](images/c46c85_8b960690352849538c42d8c19d3eb703.webp)

Great!, We have successfully made a Python Program to Check Prime Numbers. Let's see the full file,

![](images/c46c85_3e040c03f7ba4f9bb2a5b81ed06eb51f.webp)
