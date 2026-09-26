---
title: "Rolling a Dice Randomly"
author: "Sana Omar"
date: 2021-09-21
description: "Hello everyone, today we are gonna roll a dice randomly in several ways.First of all, we need to import randint from random package to generate random integer numbers of the Dice faces.from random..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/rolling-a-dice-randomly
---
Hello everyone, today we are gonna roll a dice randomly in several ways.

First of all, we need to import randint from random package to generate random integer numbers of the Dice faces.

```python
from random import randint
```

As we know, Dice has only 6 faces, ***6 possibilities*** starting from 1 to 6.

Thus, whenever we need to generate random rolls, we call **randint(START_VALUE, END_VALUE)** to make the starting value 1, and the ending value 6.

Dice faces do not change, so the range is always from 1 to 6.

Another important concept is the ***NUMBER of rolls*** or throws. This is not randomized by the program, instead we will explore three ways or cases in solving it.

**First way:**

Intuitively, we will first think of looping through a **for in range** function for 6 times, a throw for each face.

```python
#using loops rolling 6 times randomly
for j in range(6):
  roll = randint(1,6)
  print("You threw: " + str(roll))
```

Here, inside the loop, a **roll** variable holds the result of the throw from **randint(1,6).** Then by printing results the following will appear:

```python
You threw: 5
You threw: 1
You threw: 6
You threw: 5
You threw: 4
You threw: 6
```

**Second way:**

We define a function for randomizing the throws that return the face number.

```python
#using functions to rolling 6 times randomly
def roll_dice():
   roll = randint(1,6)
   return roll
```

Then we call it inside a loop of 6 rolls or throws:

```python
for j in range(6):
    print("You threw: " + str(roll_dice()))
```

**Third way:**

Until now, all of our throws are 6, the same number as the faces of the dice.

***What if we want to roll it for more or less than that?***

In this case, the program will ask the user to enter the number of the rolls using input function, and storing it in the **no_rolls** variable to use it in the loop function.

```python
no_rolls = input("Enter the number of rolls: " )
for j in range(int(no_rolls)):
    print("You threw: " + str(roll_dice()))
```

the output could be:

```python
Enter the number of rolls: 20
You threw: 5
You threw: 2
You threw: 2
You threw: 4
You threw: 2
You threw: 3
You threw: 2
You threw: 4
You threw: 1
You threw: 4
You threw: 3
You threw: 4
You threw: 5
You threw: 4
You threw: 1
You threw: 5
You threw: 2
You threw: 5
You threw: 1
You threw: 5
```

**Forth way:**
Until now, we thought of entering a number of rolls, we could instead prompt the user to answer a question if he wants to throw another more time or not.
We assume he is going to throw unless the entered value is 'n' or 'N', in which the loop will be stopped using break.

```python
while True:
  print("You threw: " + str(roll_dice()))
  roll_again = input("Do you want to rall again?, Enter Y for Yes, N for no")
  if roll_again == ('n' or 'N'):
    break;
```

The output could be:

```python
You threw: 1
Do you want to rall again?, Enter Y for Yes, N for noy
You threw: 3
Do you want to rall again?, Enter Y for Yes, N for noy
You threw: 6
Do you want to rall again?, Enter Y for Yes, N for nou
You threw: 2
Do you want to rall again?, Enter Y for Yes, N for non
```

***Hope this is helpful, thank you for reading so far.***
