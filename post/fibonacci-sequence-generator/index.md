---
title: "Fibonacci Sequence Generator"
author: "Thiha Naung"
date: 2021-09-03
description: "Fibonacci sequence is sequence of numbers and each number is the sum of the two preceding ones, starting from 0 and 1. For example 5 fibonacci sequence numbers are 0,1,1,2,3 in which 0 + 1 = 1 , 1 +..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/fibonacci-sequence-generator
---
Fibonacci sequence is sequence of numbers and each number is the sum of the two preceding ones, starting from 0 and 1. For example 5 fibonacci sequence numbers are 0,1,1,2,3 in which 0 + 1 = 1 , 1 + 1 = 2, 2 + 3 = 5, etc.
In python, it can easily be written as follow.
Here you can read more about[**fibonacci sequnce**](https://en.wikipedia.org/wiki/Fibonacci_number)**.**

Let's write the code.

```python
def fibonacci(length):
    a, b = 0,1
    lst = [0,1]
    for i in range(length-2):
        a, b = b, a+b
        lst.append(b)
    return(lst)
```

Second-line is to assign the first 2 numbers and put them into a list.

Make a 'for' loop for the required length. In the loop, the second number from the previous loop is assigned to the first number of the present loop and the sum of the first and second numbers from the previous loop is assigned to the second number of the present loop. Then, append to the list.

Let's check it out.

```python
print(fibonacci(10))
> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

print(fibonacci(30))
> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229]
```

That's all. You can enter any number for the required sequence.
