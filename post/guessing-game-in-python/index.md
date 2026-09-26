---
title: "Guessing Game in python"
author: "Omnia Sayed"
date: 2021-09-21
description: "Guessing game becomes an interesting technique which can be implemented by English teachers to teach speaking. Beside rising so much fun, guessing games is believed could increase the students’..."
categories: ["Python"]
wix-url: https://www.datainsightonline.com/post/guessing-game-in-python
---
Guessing game becomes an interesting technique which can be implemented by English teachers to teach speaking. Beside rising so much fun, guessing games is believed could increase the students’ speaking skill.

This is going to be a simple guessing game where the computer will generate a random number between 1 to 10, and the user has to guess it in 5 tries.

**follow the step in a game:**

First Step:

Make import to random

import random

number = random.randint(1, 10)

**Second Step:**

Ask a user its name.

player_of_name = input("Hello, What's your name?")

number_of_guess = 0

print('okay! '+ player_of_name+ ' I am Guessing a number between 1 and 10:')

**Third Step:**

Make a loop and put condition of a game

while number_of_guess < 5:

guess = int(input())

number_of_guess += 1

if guess < number:

print('Your guess is too low')

if guess > number:

print('Your guess is too high')

if guess == number:

break

**Fourth Step:**

if guess equal random number we told a player number of tries

and if he can't guess we also told him number of tries and he can't guess more than 5 tries

if guess == number:

print('You guessed the number in ' + str(number_of_guess) + ' tries!')

else:

print('You did not guess the number, The number was ' + str(number))

**Finally the output:**

```python
Hello, What's your name?Omnia
okay! Omnia I am Guessing a number between 1 and 10:
3
Your guess is too low
6
Your guess is too high
5
You guessed the number in 3 tries!
```
