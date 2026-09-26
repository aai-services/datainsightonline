---
title: "Python Concepts: Loops"
author: "mrbenjaminowusu"
date: 2021-10-08
description: "Loop statements execute a single statement or group of statements multiple times. The statements are executed sequentially. The first statement in a function is executed first, then the second and so..."
categories: ["Python"]
image: images/996a18_8129cf594fc245dba09ca7fca64dd89f.webp
wix-url: https://www.datainsightonline.com/post/python-concepts-loops-1
---
Loop statements execute a single statement or group of statements multiple times. The statements are executed sequentially. The first statement in a function is executed first, then the second and so on. There may be instances when you need to execute a block of code multiple times.

There are two types of python loops. The **while** and **for** loops.

**while Loop Statements**

A while loop statement repeatedly executes a target of statement as long as a given condition is true. The statement may be a single statement or block of statements with a uniform indent. The loop iterates while the loop is true. Once the loop becomes false, the program moves the line immediately following the loop. The syntax of a while loop is below

```python
while expression:
    statement(s)
```

A key point of the while loop is that when the condition is tested and the result is false, the loop never runs. The loop body will be skipped and the first statement after the loop will be executed.

An example of a while loop is below. In the example, the variable number is assigned to the integer 0. The block of code in the while loop executes repeatedly until the variable number is no longer less than 10. With each iteration, the current value of the variable number is displayed with the print function and then increased by 1. It is increased by 1 in order not to be trapped in an infinite loop where the variable number is always less than 10.

```python
number=0
while number < 10:
    print(number, ' is less than 10.')
    number +=1
print('Done')
```

when the above code is executed, it produces the following results:

```python
0  is less than 10.
1  is less than 10.
2  is less than 10.
3  is less than 10.
4  is less than 10.
5  is less than 10.
6  is less than 10.
7  is less than 10.
8  is less than 10.
9  is less than 10.
Done
```

**The** Infinite **Loop**

An infinite loop occurs if a condition never becomes FALSE. This results in a loop that never ends. An example of an infinite loop is below:

```python
x=1
while x==1:
    print('the number is: ', x)
```

when the above code is executed, it produces the following result. The program goes in an infinite loop and never stops. You have to interrupt the kernel with the keyboard shortcut by double-tapping I.

```python
the number is:  1
the number is:  1
the number is:  1
the number is:  1
the number is:  1
the number is:  1
the number is:  1
the number is:  1
the number is:  1
the number is:  1
the number is:  1
the number is:  1
the number is:  1
the number is:  1
the number is:  1
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-4-cc397fc0c698> in <module>      2 x=1      3 while x==1:----> 4     print('the number is: ', x)
```

**Using else statement with while loop**

Python supports having else statement associated with a loop statement.

In a while loop, an else statement is executed when the condition becomes false.

The example below shows the combination of a while loop and an else statement. As long as the condition is less than 10, the print statement is executed. Otherwise, the else statement gets executed.

```python
number=0
while number < 10:
    print(number, ' is less than 10.')
    number +=1
else:
    print(number, ' is not less than 10')
```

This produces the following output

```python
0  is less than 10.
1  is less than 10.
2  is less than 10.
3  is less than 10.
4  is less than 10.
5  is less than 10.
6  is less than 10.
7  is less than 10.
8  is less than 10.
9  is less than 10.
10  is not less than 10
```

**for Loop Statements**

The for statement is used to iterate over items of any sequence, such as strings and lists. The syntax of a for loop is below:

```python
for iterating_var in sequence:
    statement(s)
```

The loop takes on each successive value in the sequence, and the statements in the body of the loop are executed once for each value.

The following example shows a for loop on a string:

```python
fruit= 'mangoes'
for f in fruit:
    print('the index of ['+ f + '] is '+ str(fruit.index(f)))
```

This produces the following output that prints an iteration of all the letters in mangoes.

```python
the index of [m] is 0
the index of [a] is 1
the index of [n] is 2
the index of [g] is 3
the index of [o] is 4
the index of [e] is 5
the index of [s] is 6
```

**Using else statement with for loop**

When using the else statement in a for loop, the else statement is executed when the loop has exhausted iterating the list.

An example of a for loop with an else statement is below. The else statement is executed after the iteration of the elements in the list.

```python
items_in_fridge = ['vegetables','water', 'juice', 'meat', 'fruits']
for item in items_in_fridge:
    print('fridge contains: '+ item)
else:
    print("All items in the fridge are accounted for.")
```

**Nested loops**

Nested loops allow the use of a loop inside another loop. The inner or outer loop can be any type, such as a while loop or a for loop. The syntax for both nested while and loops are below.

```python
for iterating_var in sequence:
    for iterating_var in sequence:
        statement(s)
    statement(s)
```

```python
    while expression:
        while expression:
            statement(s)
        statement(s)
```

An example of a nested for loop is below. A list of countries is executed with a nested for loop.

```python
countries=['ghana','nigeria','england','norway', 'brasil']
for country in countries:
    for letter in country:
        print(letter.upper())
```

**Loop Control Statements**

The loop control statements change the execution from its normal sequence. There are three loop control statements. Break, continue and pass statements.

**Break Statement:** It is used to exit a while loop or a for a loop. It terminates the looping & transfers execution to the statement next to the loop. The following example illustrates the execution of the break statement.

```python
items_in_fridge = ['vegetables','water', 'juice', 'meat', 'fruits']
for item in items_in_fridge:
    if item == 'meat':
        break
    print('fridge contains: '+ item)
```

When the above code is executed, it produces the following output. The items in the list before the string meat are executed. The string meat and fruit are not executed because of the break statement.

```python
fridge contains: vegetables
fridge contains: water
fridge contains: juice
```

**Continue statement:** It is used to skip over the current iteration of any loop. When a continue statement is encountered in a loop, the python interpreter ignores the rest of the statements in the loop body for the current iteration and returns the program execution to the very first statement in the loop body. The following example illustrates the execution of the continue statement in a loop.

```python
items_in_fridge = ['vegetables','water', 'juice', 'meat', 'fruits']
for item in items_in_fridge:
    if item == 'meat':
       continue
    print('fridge contains: '+ item)
```

When the code above is executed, it produces the following output. All items in the list before and after the string meat are executed.

```python
fridge contains: vegetables
fridge contains: water
fridge contains: juice
fridge contains: fruits
```

**Pass statement: T**he pass statement is considered as no operation statement, which means it consumes the execution cycle like a valid python statement but nothing happens actually when the pass is executed. It is generally used to indicate “null” or unimplemented functions and loops body. The example below illustrates a pass statement.

```python
items_in_fridge = ['vegetables','water', 'juice', 'meat', 'fruits']
for item in items_in_fridge:
    if item == 'meat':
       pass
       print("There is no meat")

    print('fridge contains: '+ item)
```

When the above code is executed, The following output is produced. The pass statement is called on the string 'meat'.The code jump over the current iteration and rather prints the string "There is no meat".

```python
fridge contains: vegetables
fridge contains: water
fridge contains: juice
There is no meat
fridge contains: meat
fridge contains: fruits
```

References

[python-tutorial/loops](https://www.w3adda.com/python-tutorial/python-loop-control-statements)

[Python Tutorial (tutorialspoint.com)](https://www.tutorialspoint.com/python/index.htm)
