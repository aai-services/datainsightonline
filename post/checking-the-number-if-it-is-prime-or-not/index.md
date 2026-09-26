---
title: "Checking if a Number is Prime or Not with Python"
author: "Nargiz Huseynova"
date: 2021-09-21
description: "In this blog, we will use the Python programming language to write a simple application that checks if the number is prime or not.Prime numbers are special numbers, greater than 1, that have exactly..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/checking-the-number-if-it-is-prime-or-not
---
In this blog, we will use the Python programming language to write a simple application that checks if the number is prime or not.

**Prime numbers** are special numbers, greater than 1, that have exactly two factors, **themselves** and **1.**

19 is a prime number. It can only be divided by 1 and 19.

9 is not a prime number. It can be divided by 3 as well as 1 and 9.

```python
num = int(input('Enter the number: '))
```

Above code is the way to get input from the user, making it *int* data type and assigning it to a variable called *num.*

```python
# If given number is greater than 1
if num > 1:

    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):

        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")
```

Since the integer 1 is neither prime nor composite we first check the *num* to be greater than 1. If the *num* is greater than 1 then we write a for loop.

The loop starts from 2 and goes till *num/2.* Because the largest proper divisor of a number N can never be greater than N/2. Recall that *range* method does not include the second argument.

The next condition checks if the number is divisible by *i,* if yes, it prints out the message that the number is not prime, else, it says the number is prime. And the last *else* condition is a way of considering the numbers that are not greater than 1 (not prime).

Let us run the code and see an example:

```python
Enter the number:11
```

When we enter 11 as an input, the output says:

```python
11 is a prime number
```

Because 11 is only divisible by itself and 1, the output is correct.

Let us see another one:

```python
Enter the number: 86
```

When we enter 86 as an input,

```python
86 is not a prime number
```

is the result. Because 86 can be divided by 1, 2, 43, 86, it is a composite number not a prime number.

You can find the GitHub repo for the jupyter notebook and python code at this [link](https://github.com/iamNargiz/datainsight2)
