---
title: "Python For Loops"
author: "amrali150"
date: 2022-02-07
description: "A for loop acts as an iterator in Python; it goes through items that are in a sequence or any other iterable item. Objects that we've learned about that we can iterate over include strings, lists..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/python-for-loops-1
---
A for loop acts as an iterator in Python; it goes through items that are in a *sequence* or any other iterable item. Objects that we've learned about that we can iterate over include strings, lists, tuples, and even built-in iterables for dictionaries, such as keys or values.
We've already seen the for statement a little bit in past lectures but now let's formalize our understanding.
Here's the general format for a for loop in Python:
for item in object: statements to do stuff

The variable name used for the item is completely up to the coder, so use your best judgment for choosing a name that makes sense and you will be able to understand when revisiting your code. This item name can then be referenced inside your loop, for example if you wanted to use if statements to perform checks.
Let's go ahead and work through several example of for loops using a variety of data object types. We'll start simple and build more complexity later on.

**Example 1**
Iterating through a list

```python
# We'll learn how to automate this sort of list in the next lecture
list1 = [1,2,3,4,5,6,7,8,9,10]
```

```python
for num in list1:
    print(num)
```

Output is:

```python
1
2
3
4
5
6
7
8
9
10
```

Great! Hopefully this makes sense. Now let's add an if statement to check for even numbers. We'll first introduce a new concept here--the modulo.

### Modulo

The modulo allows us to get the remainder in a division and uses the % symbol. For example:

```python
17 % 5
```

Output is:

```python
2
```

This makes sense since 17 divided by 5 is 3 remainder 2.

Notice that if a number is fully divisible with no remainder, the result of the modulo call is 0. We can use this to test for even numbers, since if a number modulo 2 is equal to 0, that means it is an even number!

Back to the for loops!

## **Example 2**[**¶**](http://localhost:8888/notebooks/Desktop/03-for%20Loops.ipynb#Example-2)

Let's print only the even numbers from that list!

```python
for num in list1:
    if num % 2 == 0:
        print(num)
```

Output is:

```python
2
4
6
8
10
```

We could have also put an else statement in there:

```python
for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number')
```

Output is:

```python
Odd number
2
Odd number
4
Odd number
6
Odd number
8
Odd number
10
```

## Example 3

Another common idea during a for loop is keeping some sort of running tally during multiple loops. For example, let's create a for loop that sums up the list:

```python
# Start sum at zero
list_sum = 0

for num in list1:
    list_sum = list_sum + num

print(list_sum)
```

Output is:

```python
55
```

Great! Read over the above cell and make sure you understand fully what is going on. Also we could have implemented a += to perform the addition towards the sum. For example:

```python
# Start sum at zero
list_sum = 0

for num in list1:
    list_sum += num

print(list_sum)
```

Output is:

```python
55
```

**For more examples you can reach out our notebook from** [**here**](https://github.com/Amr-Ali/Python-For-Loops/blob/main/for%20Loops.ipynb)
