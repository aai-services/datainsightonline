---
title: "Calculating Highest Common Factor using Python"
author: "Abu Bin Fahd"
date: 2021-09-19
description: "The HCF (Highest Common Factor) of two or more numbers is the highest number among all the common factors of the given numbers.The properties of HCF are given below. • HCF of two or more numbers..."
categories: ["Python"]
image: images/7db382_24ce3ea25432468eb1e99a4374dd02a6.webp
wix-url: https://www.datainsightonline.com/post/highest-common-factor
---
![](images/7db382_24ce3ea25432468eb1e99a4374dd02a6.webp)

The HCF (Highest Common Factor) of two or more numbers is the highest number among all the common factors of the given numbers.

The properties of HCF are given below.

- HCF of two or more numbers divides each of the numbers without a remainder.
- HCF of two or more numbers is a factor of each of the numbers.
- HCF of two or more numbers is always less than or equal to each of the numbers.
- HCF of two or more prime numbers is 1 always

```python
def hcf(a, b):
    if a > b:
        smaller = b
    else:
        smaller = a

    for i in range(1, smaller+1):
        if a % i == 0 and b % i == 0:
            ans = i
    print(ans)

hcf(15, 30)
```

##### First Part

```python
def hcf(a, b):
    if a > b:
        smaller = b
    else:
        smaller = a
```

Here we define a function "hcf" which have two parameters. Firstly we found a smaller number between a & b. Because the highest common factor is never bigger than a smaller number.

##### second Part

```python
for i in range(1, smaller+1):
        if a % i == 0 and b % i == 0:
            ans = i
    print(ans)

hcf(15, 30)
```

We run a for loop 1 to the smaller number and mod the two given numbers. And when we mod the two numbers and found the value zero then we update the "ans" value.

> Theoretically,

> *15 = 1 , 3, 5, 15*

> *30 = 1, 3, 5, 6, 10, 15, 30*

> *Here the common factors are 1, 3, 5, 15*

> *And the highest is 15.*
