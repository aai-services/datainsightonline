---
title: "LOOPS"
author: "Blessing Oluwadaara"
date: 2021-10-17
description: "Loops are important in data science as they help you to execute a block of code repeatedly. You will often come face to face with situations where you would need to use a piece of code over and over..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/loops
---
Loops are important in data science as they help you to execute a block of code repeatedly. You will often come face to face with situations where you would need to use a piece of code over and over but you don't want to write the same line of code multiple times.

## Types of Loops

- A **for** loop is a loop that runs for a preset number of times.
- A **while** loop is a loop that is repeated as long as an expression is true. An expression is a statement that has a value.

## Loop Control Statements

A statement that alters the execution of a loop from its designated sequence is a loop control statement.

- A **break** statement inside a loop terminates the loop immediately.
- A **continue** statement jumps to the next iteration of the loop, skipping any code in between.

WHILE LOOP

The while loop is one of the first loops that you'll probably encounter when you're starting to learn how to program. It is arguably also one of the most intuitive ones to understand: if you think of the name of this loop, you will quickly understand that the word "while" has got to do something with "interval" or a "period of time". As you already know by now, the word "loop" refers to a piece of code that you execute repeatedly.

With all of this in mind, you can easily understand the following definition of the while loop:

A while loop is a programming concept that, when it's implemented, executes a piece of code over and over again while a given condition still holds true.

The above definition also highlights the three components that you need to construct the while loop in Python:

- The while keyword;
- A condition that transates to either True or False; And
- A block of code that you want to execute repeatedly

That's all it takes!

```python
#WHILE LOOP
# Take user input
number = 2
# Condition of the while loop
while number < 5 :
    print("Hey you!")
     # Increment the value of the variable "number by 1"
      number = number+1
```

The code example above is a very simple while loop: if you think about it, the three components about which you read before are all present: the while keyword, followed by a condition that translates to either True or False (number < 5) and a block of code that you want to execute repeatedly

FOR LOOP

You can tackle the for loop in the same way as the while loop. As you probably would have expected, the "for" component in "for loop" refers to something that you do for a certain number of times.

If you keep all the above in mind, you can easily define the for loop as follows:

A for loop is a programming concept that, when it's implemented, executes a piece of code over and over again "for" a certain number of times, based on a sequence.

In contrast to the while loop, there isn't any condition actively involved - you just execute a piece of code repeatedly for a number of times. In other words, while the while loop keeps on executing the block of code contained within it only till the condition is True, the for loop executes the code contained within it only for a specific number of times. This "number of times" is determined by a sequence or an ordered list of things.

The following pieces are all that you need in order to create a for loop:

- The for keyword
- A variable
- The in keyword
- The sequence you want to loop through
- The code that you want to execute repeatedly

```python
#FOR LOOP
# Print "How you doing?" 5 times
for number in range(5):
    print("How you doing?")
```

As you can see, the components that you saw in the above section return in this small example of a for loop in Python: the for keyword, the variable number, the in keyword, the range() function and the code that you want to execute multiple times, print("How you doing?").
