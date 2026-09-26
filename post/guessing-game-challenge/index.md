---
title: "Guessing Game Challenge"
author: "amrali150"
date: 2022-01-23
description: "Let's use while loops to create a guessing game.The Challenge:Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:1. If a player's guess is less..."
categories: ["General"]
wix-url: https://www.datainsightonline.com/post/guessing-game-challenge
---
Let's use while loops to create a guessing game.

The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
2. On a player's first turn, if their guess is

   - within 10 of the number, return "WARM!"
   - further than 10 away from the number, return "COLD!"
3. On all subsequent turns, if a guess is

   - closer to the number than the previous guess return "WARMER!"
   - farther from the number than the previous guess, return "COLDER!"
4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!

#### First, pick a random integer from 1 to 100 using the random module and assign it to a variable.

Note: random.randint(a,b) returns a random integer in range [a, b], including both end points.

```python
import random
num = random.randint(1,100)
```

#### Next, print an introduction to the game and explain the rules.

```python
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
```

#### Output is :

```python
WELCOME TO GUESS ME!
I'm thinking of a number between 1 and 100
If your guess is more than 10 away from my number, I'll tell you you're COLD
If your guess is within 10 of my number, I'll tell you you're WARM
If your guess is farther than your most recent guess, I'll say you're getting COLDER
If your guess is closer than your most recent guess, I'll say you're getting WARMER
LET'S PLAY!
```

#### Create a list to store guesses
```python
guesses = [0]
```

#### Write a while loop that asks for a valid guess. Test it a few times to make sure it works.

```python
while True:

    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    break
```

Output is :

```python
I'm thinking of a number between 1 and 100.
  What is your guess? 500
OUT OF BOUNDS! Please try again:
I'm thinking of a number between 1 and 100.
  What is your guess? 50
```

#### Write a while loop that compares the player's guess to our number. If the player guesses correctly, break from the loop. Otherwise, tell the player if they're warmer or colder, and continue asking for guesses.

```python
while True:

    # we can copy the code from above to take an input
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    # here we compare the player's guess to our number
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break

    # if guess is incorrect, add guess to the list
    guesses.append(guess)

    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section

    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')

    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
```

Output is:

```python
I'm thinking of a number between 1 and 100.
  What is your guess? 50
COLD!
I'm thinking of a number between 1 and 100.
  What is your guess? 75
WARMER!
I'm thinking of a number between 1 and 100.
  What is your guess? 85
WARMER!
I'm thinking of a number between 1 and 100.
  What is your guess? 92
COLDER!
I'm thinking of a number between 1 and 100.
  What is your guess? 80
WARMER!
I'm thinking of a number between 1 and 100.
  What is your guess? 78
COLDER!
I'm thinking of a number between 1 and 100.
  What is your guess? 82
WARMER!
I'm thinking of a number between 1 and 100.
  What is your guess? 83
COLDER!
I'm thinking of a number between 1 and 100.
  What is your guess? 81
CONGRATULATIONS, YOU GUESSED IT IN ONLY 9 GUESSES!!
```
