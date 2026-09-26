---
title: "Guess The Number Game"
author: "Caleb Atiemo - Keseku"
date: 2021-09-16
description: "Guessing games are fun. Why don't we try one? Ready?Let's match on. The python code below illustrates how to play the gameGuess The Number GameWe first of all import the modules we are going to need..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/guess-the-number-game-1
---
Guessing games are fun. Why don't we try one? Ready?

Let's match on. The python code below illustrates how to play the game

## Guess The Number Game

We first of all import the modules we are going to need for the game. We will be using the random module

```python
import random
```

The below code takes an input from the user and stores it in a variable, name. This is intended to save the name of the user.

```python
name = input('Please enter your name: ')
```

The ‘introduction’ variable contains a welcome message to the Guess The Number Game.

```python
introduction = 'Hello ' + name + ', you are welcome to the guessing game'
```

This line prints the ‘introduction’ variable

```python
print(introduction)
```

Guess count and correct guesses of **0** are initialized and the guess limit set to **5**.

```python
guess_count = 0
correct_guess = 0
guess_limit = 5
```

This block of code utilizes a while loop. The condition for the code to run is when the guess count is less than the guess limit. Within the loop, an a numeral input between **0** and **5** is taken from the user and converted to 'integer'. The input is stored as 'guess'. The computer generates a random number between the same range and stores it as 'hidden_number'. A comparison between 'guess' and 'hidden_number' is done. If both are the same, a sentence affirming a correct guess with the 'hidden_number' is printed and the number of correct guesses is increased by 1. If both numbers are different, a sentence affirming a wrong guess with the 'hidden_number' is printed. The guess number is updated to reflect the number of games played. The loop stopes when the condition is invalidated, ie 'guess_count' is greater than 'guess_limit'

```python
while guess_count < guess_limit:
    guess = int(input('Please guess a number between 0 and 5: '))
    hidden_number = random.randint(0,5)
    if guess == hidden_number:
        print('You guessed correctly. The hidden number is ' + str(hidden_number))
        correct_guess += 1
    else:
        print('You guessed wrongly. The hidden number is ' + str(hidden_number) + '. Try again')
    guess_count += 1
```

This block of code simply displays the number of correct guesses at the end of the game

```python
if correct_guess == 1:
    print('You have come to the end of the game. You had ' + str(correct_guess) + ' correct guess')
else:
    print('You have come to the end of the game. You had ' + str(correct_guess) + ' correct guesses')
```

Here is a [link](https://github.com/catiemokeseku/Guess-The-Number-Game.git) to the repo on github
