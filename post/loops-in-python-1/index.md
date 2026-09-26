---
title: "Loops in Python"
author: "Ahmed Shebl"
date: 2022-01-25
description: "Loops enable us to alter the flow of the program so that instead of writing the same code, again and again, we can repeat the same code a finite number of times. For example, if we need to print the..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/loops-in-python-1
---
Loops enable us to alter the flow of the program so that instead of writing the same code, again and again, we can repeat the same code a finite number of times. For example, if we need to print the first 10 natural numbers then, instead of using the print statement 10 times, we can print inside a loop that runs up to 10 iterations.

Python provides two ways for executing the loops. While the two ways provide similar basic functionality, they differ in their syntax and condition checking time.

1. for Loop

2. while Loop

## 1. for Loop
For loops iterate over a given sequence. It is better to use if the number of iterations is known in advance.

```python
numbers = [2, 5, 8, 11]
for number in numbers:
    print(number)
```

output:

```python
2
5
8
11
```

We can also use it with the range() function

```python
for number in range(2, 12, 3):
    print(number)
```

output:

```python
2
5
8
11
```

## 2. While Loop
The block of statements is executed while the condition specified in the while loop is True. The while loop is used in the scenario where we don't know the number of iterations in advance.

```python
number = 2
while number < 12:
    print(number)
    number += 3
```

output:

```python
2
5
8
11
```

**break and continue statements**

break is used to exit a for loop or a while loop, whereas continue is used to skip the current block and return to the for or while statement.

```python
for x in range(10):
    if x % 3 == 0:
        continue
    print(x)
```

output:

```python
1
2
4
5
7
8
```

```python
x = 0
while x < 10:
    print(x)
    x += 1
    if x > 5:
        break
```

output:

```python
0
1
2
3
4
5
```

**Use else clause for loops**

we can use **else** for loops. When the loop condition of **for** or **while** statement fails then code part in **else** is executed. If a **break** statement is executed inside the for loop then the **else** part is skipped. Note that the **else** part is executed even if there is a **continue** statement.

```python
number = 1
while(number < 10):
    if(number % 5 == 0):
        break
    print(number)
    number += 1
else:
    print("Number value equal: " + str(number))
```

output:

```python
1
2
3
4
```

```python
for number in range(10):
    if(number % 5 == 0):
        continue
    print(number)
else:
    print("The value equal: " + str(number))
```

output:

```python
1
2
3
4
6
7
8
9
The value equal: 9
```

**Pass statement**

Used to execute an empty loop. The pass statement is useful when you don't write the implementation of a loop but you want to implement it in the future.

```python
for i in range(10):
    pass
```
