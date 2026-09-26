---
title: "Prime Numbers"
author: "Mahmoud Abdullah"
date: 2021-10-10
description: "A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers.The function below checks if a number is prime by checking if it is a multiple of..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/prime-numbers
---
A **prime number** (or a **prime**) is a [natural number](https://en.wikipedia.org/wiki/Natural_number) greater than 1 that is not a [product](https://en.wikipedia.org/wiki/Product_(mathematics)) of two smaller natural numbers.

The function below checks if a number is prime by checking if it is a multiple of any number smaller than it:

```python
def is_prime(number):
    if number <= 1:
        return False

    for factor in range(2, number):
        if not number % factor:
            return False

    return True
```

You might have noticed that the primality check the function is_prime we developed before is somewhat slow for large numbers. This is because we are doing a ton of extra work checking every possible factor of the tested number. We will use two optimizations to make a is_prime_fast function.

The first optimization takes advantage of the fact that two is the only even prime. Thus we can check if a number is even and as long as its greater than 2, we know that it is not prime.

Our second optimization takes advantage of the fact that when checking factors, we only need to check odd factors up to the square root of a number. Consider a number *𝑛*

decomposed into factors *𝑛*=*𝑎𝑏*. There are two cases, either *𝑛* is prime and without loss of generality, *𝑎*=*𝑛*, *𝑏*=1 or *𝑛* is not prime and *𝑎*,*𝑏*≠*𝑛*,1. In this case, if

So we only need to check all possible values of *𝑏* and we get the values of *𝑎* for free! This means that even the simple method of checking factors will increase in complexity as a square root compared to the size of the number instead of linearly.

Lets write the function to do this and check the speed! is_prime_fast will take a number and return whether or not it is prime.

```python
import math

def is_prime_fast(number):
    if number <= 1:
        return False

    for factor in range(2, math.isqrt(number)+1):
        if not number % factor:
            return False
    return True

for n in range(10000):
    assert is_prime(n) ==  is_prime_fast(n)
```

Making sure it finds the same primes as the original function:

```python
>>> for n in range(10000):
...     assert is_prime(n) == is_prime_fast(n)
```

Now we will develop an even faster method which is known as the Sieve of Eratosthenes (although it will be more expensive in terms of memory). The Sieve of Eratosthenes is an example of dynamic programming, where the general idea is to not redo computations we have already done (read more about it [here](https://en.wikipedia.org/wiki/Dynamic_programming)). We will break this sieve down into several small functions.

The method works as follows (see [here](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) for more details)

1. Generate a list of all numbers between 0 and N; mark the numbers 0 and 1 to be not prime
2. Starting with *𝑝*=2 (the first prime) mark all numbers of the form *𝑛𝑝* where *𝑛*>1 and *𝑛𝑝* <= *𝑁* to be not prime (they can't be prime since they are multiples of 2!)
3. Find the smallest number greater than *𝑝* which is not marked and set that equal to *𝑝*, then go back to step 2. Stop if there is no unmarked number greater than *𝑝* and less than *𝑁*+1

We will break this up into a few functions, our general strategy will be to use a Python list as our container although we could use other data structures. The index of this list will represent numbers.

The functions used in this algorithm are as follows

- list_true Make a list of true values of length *𝑛*+1 where the first two values are false (this corresponds with step 1 of the algorithm above)

```python
def list_true(n):
    return [False, False] + [True] * (n-1)
```

- mark_false takes a list of booleans and a number *𝑝.* Mark all elements 2*𝑝*,3*𝑝*,...*𝑛* false (this corresponds with step 2 of the algorithm above)

```python
def mark_false(bool_list, p):
    for i in range(2*p, len(bool_list), p):
        bool_list[i] = False
    return bool_list
```

- find_next Find the smallest True element in a list which is greater than some *𝑝* (has index greater than *𝑝* (this corresponds with step 3 of the algorithm above)

```python
def find_next(bool_list, p):
    for i in range(p+1, len(bool_list)):
        if bool_list[i]:
            return i

    return None
```

- prime_from_list Return indices of True values

```python
def prime_from_list(bool_list):
    return [index for index, bool_ in enumerate(bool_list) if bool_]
```

The main function will be as below:

```python
def sieve(n):
    bool_list = list_true(n)
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
    return prime_from_list(bool_list)
```

For example to get the prime numbers below 20:

```python
>>> sieve(20)
[2, 3, 5, 7, 11, 13, 17, 19]
```

## Resources:

- [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming)
- [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
